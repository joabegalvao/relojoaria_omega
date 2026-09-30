#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.
"""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
AVATAR_SRC = SOURCES / "avaliacoes"
# Versão branca enviada pelo cliente durante o projeto; a prateada em relevo
# (omega_logo.png) fica guardada, mas não é usada na página.
LOGO_SRC = SOURCES / "logo" / "omega_logo_nova.png"
OUT = ROOT / "assets" / "img"

GRAPHITE = (20, 20, 22)  # #141416, fundo escuro da página

# Nada é ampliado: a maior versão gerada é a do recorte original.
WIDTHS = (360, 540)

# nome de saída -> (arquivo em materiais-de-origem/fotos, área usada)
# A área é (esquerda, topo, direita, base) em pixels do original. As artes
# do Instagram trazem texto sobre a foto; o recorte fica só na parte com o
# produto. As bordas irregulares da captura ficam de fora.
PHOTOS = {
    "fachada": ("Screenshot 2026-09-30 092428.png", (3, 310, 676, 855)),
    "relogio-aco-mostrador-verde": ("Screenshot 2026-09-30 092453.png", (3, 330, 665, 890)),
    "relogio-pulseira-de-couro": ("Screenshot 2026-09-30 092504.png", (3, 340, 666, 891)),
    "relogio-dourado": ("Screenshot 2026-09-30 092609.png", (3, 300, 663, 889)),
    "relogio-esportivo-azul": ("Screenshot 2026-09-30 092616.png", (3, 260, 668, 889)),
    "par-de-relogios": ("Screenshot 2026-09-30 092548.png", (3, 3, 888, 890)),
    "canetas": ("Screenshot 2026-09-30 092528.png", (3, 150, 712, 740)),
    "oculos": ("Screenshot 2026-09-30 092442.png", (338, 3, 714, 832)),
}

# Fotos de perfil: nome de saída -> arquivo em materiais-de-origem/avaliacoes
AVATARS = {
    "avaliacao-martin-eikmeier": "Martin Eikmeier.png",
    "avaliacao-douglas-furtado": "Douglas Furtado.png",
    "avaliacao-sergio-menezes": "Sergio Menezes.png",
}


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def save_set(im: Image.Image, name: str) -> None:
    for width in WIDTHS:
        if width < im.width:
            resize_to_width(im, width).save(
                OUT / f"{name}-{width}.webp", "WEBP", quality=82, method=6
            )
    im.save(OUT / f"{name}-{im.width}.webp", "WEBP", quality=82, method=6)
    # fallback JPEG para navegadores sem WebP
    im.save(OUT / f"{name}-{im.width}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print(f"{name}: {im.width}x{im.height}")


def build_photos() -> None:
    for name, (source, area) in PHOTOS.items():
        save_set(Image.open(SRC / source).convert("RGB").crop(area), name)


def build_logo() -> None:
    """O logo veio em PNG de 1334x1179 px, branco sobre fundo transparente.
    O script só recorta a margem vazia e gera os tamanhos usados na página."""
    logo = Image.open(LOGO_SRC).convert("RGBA")
    box = logo.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
    margin = 12
    mark = logo.crop((
        max(0, box[0] - margin), max(0, box[1] - margin),
        min(logo.width, box[2] + margin), min(logo.height, box[3] + margin),
    ))
    for width in (640, 240):
        out = resize_to_width(mark, width)
        out.save(OUT / f"logo-relojoaria-omega-{width}.png", optimize=True)
        out.save(OUT / f"logo-relojoaria-omega-{width}.webp", "WEBP", quality=92, method=6)
    print(f"logo-relojoaria-omega: {mark.width}x{mark.height} (salvo em 640 e 240)")

    # Ícones: o logo sobre o fundo escuro da página
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        tile = Image.new("RGB", (512, 512), GRAPHITE)
        fitted = mark.resize((460, round(mark.height * 460 / mark.width)), Image.LANCZOS)
        tile.paste(fitted, ((512 - fitted.width) // 2, (512 - fitted.height) // 2), fitted)
        tile.resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)


def build_avatars() -> None:
    """Mantém o tamanho e a transparência originais (72x72 px)."""
    for name, source in AVATARS.items():
        im = Image.open(AVATAR_SRC / source).convert("RGBA")
        im.save(OUT / f"{name}.png", optimize=True)
        im.save(OUT / f"{name}.webp", "WEBP", quality=90, method=6)
        print(f"{name}: {im.width}x{im.height}")


def build_social_card() -> None:
    """Imagem de compartilhamento (1200x630): logo à esquerda e fachada à direita."""
    card = Image.new("RGB", (1200, 630), GRAPHITE)

    source, area = PHOTOS["fachada"]
    photo = Image.open(SRC / source).convert("RGB").crop(area)
    photo = ImageOps.fit(photo, (620, 630), Image.LANCZOS, centering=(0.5, 0.5))
    card.paste(photo, (580, 0))

    logo = Image.open(OUT / "logo-relojoaria-omega-640.png").convert("RGBA")
    logo = resize_to_width(logo, 400)
    card.paste(logo, ((580 - 400) // 2, (630 - logo.height) // 2), logo)

    card.save(OUT / "compartilhamento.jpg", "JPEG", quality=86, optimize=True, progressive=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_logo()
    build_avatars()
    build_social_card()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
