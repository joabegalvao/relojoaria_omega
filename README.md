# Relojoaria Omega | Landing page

Página única, estática, em HTML, CSS e JavaScript puro. Não há etapa de build
nem dependências de execução: basta servir a pasta.

## Como visualizar

```bash
# na raiz do projeto
python3 -m http.server 4183
# abra http://localhost:4183
```

Qualquer servidor estático funciona (Nginx, Apache, Netlify, Vercel, Hostinger).
Publique `index.html` e a pasta `assets/`. A pasta `tools/` não precisa ir para
o servidor.

### Materiais de origem

Os arquivos enviados pelo cliente ficam reunidos na pasta
`materiais-de-origem/`, que não faz parte do repositório: ela existe só na
pasta local do projeto e é ignorada pelo git. As imagens que o site usa já
estão prontas em `assets/img`.

```
materiais-de-origem/
  logo/          omega_logo_nova.png (branco, usado na página)
                 omega_logo.png (prateado em relevo, primeira versão recebida, não usado)
  fotos/         oito capturas de tela do Instagram da loja
  avaliacoes/    fotos de perfil de quem avaliou
```

Só é preciso ter os originais para rodar `tools/optimize-images.py`, ou seja,
para trocar ou reprocessar uma foto.

## Repositório

| Item | Valor |
| --- | --- |
| Endereço | `git@github.com:joabegalvao/relojoaria_omega.git` |
| Página | https://github.com/joabegalvao/relojoaria_omega |
| Visibilidade | pública (conferida em 30/09/2026) |
| Branch | `main` |

O repositório guarda só o que o site precisa para funcionar e ser mantido:
`index.html`, `assets/`, `tools/`, `README.md` e `.gitignore`.

```bash
git clone git@github.com:joabegalvao/relojoaria_omega.git
```

Um clone novo abre e publica o site normalmente. Só não roda o script de
imagens, que depende da pasta `materiais-de-origem/`.

## Dados do cliente

Recebidos em 30/09/2026.

| Dado | Valor |
| --- | --- |
| Nome | Omega (Relojoaria Omega) |
| Segmento | Relojoaria e joalheria |
| Produtos e serviços | Relógios, joias, óculos, manutenção e confecção. Destaque também para canetas de diversas marcas, tipos e modelos |
| Frases da marca | "Tradição e confiança há mais de 70 anos" e "Presentes que encantam e marcam momentos" |
| Objetivo | Landing page com qualidade premium, para divulgar a marca |
| WhatsApp | (44) 99906-3468 |
| Telefone | (44) 3030-3468 |
| Instagram | https://www.instagram.com/omegarelojoaria_mga/ |
| Endereço | Avenida Brasil, 4077, Maringá, PR, 87013-000 |

O briefing trazia "Público-alvo: mães e pais de bebês", texto que sobrou do
projeto anterior desta série (loja de bebês). Não foi considerado.

### Conferido no Google

Em 30/09/2026, o Google Maps mostrava o perfil "Omega Relojoaria e Joalheria"
na Av. Brasil, 4077, Centro, Maringá, 87013-000, com nota 4,3 e 141
avaliações. O briefing não informou nota, e a página não cita nota nem número
de avaliações. O mapa incorporado é carregado pelo endereço, e não pelo nome
da loja, para não exibir a nota dentro do quadro.

### Avaliações como foram recebidas

- **Martin Eikmeier:** Excelente experiência! Levei meu Seiko automático para
  manutenção e o resultado foi excelente.
- **Douglas Furtado:** Lugar de confiança e qualidade para realizar troca de
  bateria de relógio. O atendimento foi excelente. Para quem quer presentear
  e/ou adquirir um novo relógio do tipi tradicional, há uma grande variedade
  de produto.
- **Sergio Menezes:** Sou cliente a muitos anos mesmo. Sempre volto pela
  confiança nos produtos e pela atendimento nota dez.

Na página, foram corrigidos só erros de digitação: "tipi" virou "tipo",
"a muitos anos" virou "há muitos anos", "pela atendimento" virou "pelo
atendimento", "e/ou" virou "ou" e "variedade de produto" virou "variedade de
produtos". O sentido não mudou.

## Estratégia

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Uma relojoaria com mais de 70 anos na Avenida Brasil, que vende, dá manutenção e confecciona |
| Principal objeção | "Compro um relógio em qualquer lugar. Por que aqui, e quem cuida dele depois?" |
| Conversão prioritária | Conversa no WhatsApp |
| Ação secundária | Ligar ou visitar a loja |
| Ação de apoio | Seguir o Instagram @omegarelojoaria_mga |

## Seções da página

| Ordem | Seção | Âncora | Conteúdo |
| --- | --- | --- | --- |
| 1 | Cabeçalho | | Logo, navegação e CTA de WhatsApp. Fixo no topo |
| 2 | Hero | `#inicio` | "Tradição e confiança há mais de 70 anos", dois botões, foto da fachada e três fatos (70+ anos, 4 linhas, 1 endereço) |
| 3 | Produtos | `#produtos` | As quatro linhas (relógios, joias, óculos, canetas) e um mosaico de três fotos |
| 4 | Relógios | `#relogios` | Cinco fotos de relógios publicadas pela loja, com legendas curtas |
| 5 | Manutenção e confecção | `#manutencao` | Troca de bateria, manutenção de automáticos, confecção e a avaliação de Martin em destaque |
| 6 | Avaliações | `#avaliacoes` | Três depoimentos, o de Sergio em destaque |
| 7 | Onde fica | `#onde-fica` | Endereço, WhatsApp, telefone, Instagram e mapa |
| 8 | Chamada final | | "Presentes que encantam e marcam momentos", WhatsApp e telefone |
| 9 | Rodapé | | Endereço, contato e redes sociais |

Componente de apoio: botão flutuante de WhatsApp, no canto inferior direito,
em todas as telas.

## Estrutura de arquivos

```
index.html                       conteúdo e SEO
assets/css/styles.css            estilos (tokens de cor e tipografia no topo)
assets/js/main.js                menu e revelação na rolagem
assets/img/                      imagens otimizadas (geradas pelo script)
assets/fonts/                    Crimson Pro e Inter (arquivos locais)
tools/optimize-images.py         gera assets/img a partir dos originais
materiais-de-origem/             arquivos do cliente (só na pasta local, fora do git)
```

## Imagens recebidas e como foram usadas

As oito fotos são capturas de tela de publicações do Instagram, todas com
texto da arte por cima (nome da loja, "Mais de 70 anos", nomes de coleção,
telefone). O script recorta só a parte com a foto, sem texto. **Nenhuma
imagem é ampliada**, e um teste automático confere que nenhuma aparece na
página acima do tamanho real.

| Arquivo | Conteúdo | Recorte final | Onde aparece |
| --- | --- | --- | --- |
| `Screenshot ... 092428.png` | Fachada da loja, na esquina | 673 x 545 | hero e imagem de compartilhamento |
| `Screenshot ... 092453.png` | Relógio de aço com mostrador verde | 662 x 560 | mosaico de "Produtos" e seção "Relógios" |
| `Screenshot ... 092528.png` | Canetas pretas | 709 x 590 | mosaico de "Produtos" |
| `Screenshot ... 092442.png` | Mulher de óculos | 376 x 829 | mosaico de "Produtos" |
| `Screenshot ... 092548.png` | Par de relógios dourados | 885 x 887 | "Relógios", foto grande |
| `Screenshot ... 092609.png` | Relógio dourado | 660 x 589 | "Relógios" |
| `Screenshot ... 092616.png` | Relógio esportivo azul | 665 x 629 | "Relógios" |
| `Screenshot ... 092504.png` | Relógio com pulseira de couro | 663 x 551 | "Relógios" |

Observações:

- As marcas dos relógios aparecem nos mostradores das fotos (são as artes da
  própria loja), mas a página não cita marca nenhuma em texto, porque o
  briefing não informou quais marcas a loja vende.
- A foto da mulher de óculos parece imagem de banco ou de fabricante, não da
  loja. Vale confirmar o direito de uso (veja Pendências).
- As legendas da seção "Relógios" ("Trabalho", "Fim de semana", "Para os
  dois") seguem os títulos das publicações da loja.

### Logo

Foram recebidas duas versões, ambas em PNG de 1334 x 1179 px com fundo
transparente. A primeira, prateada em relevo, serviu para definir a paleta. A
segunda, branca e plana, foi enviada durante o projeto com o pedido de usá-la,
e é a que está na página (cabeçalho, rodapé, ícones e imagem de
compartilhamento). O script só recorta a margem vazia e gera os tamanhos
usados. Os ícones do site colocam o logo sobre o grafite da página.

## Como atualizar o conteúdo

| O que mudar | Onde |
| --- | --- |
| Textos e endereço | `index.html` (seções comentadas) |
| Número e mensagem do WhatsApp | `index.html`: procure por `wa.me/` (8 ocorrências). O texto vem depois de `?text=`, com espaços escritos como `%20` e acentos codificados |
| Telefone | `index.html`: procure por `tel:` (3 ocorrências) e o bloco JSON-LD no `<head>` |
| Mapa | `index.html`: procure por `google.com/maps` (4 ocorrências, uma delas no `<iframe>`) |
| Cores e fontes | `assets/css/styles.css`, bloco `:root` |
| Linhas de produto | `index.html`, lista `lines` na seção "PRODUTOS" |
| Fotos de relógios | `index.html`, seção "RELÓGIOS": copie um bloco `<figure class="watch">` |
| Fotos | substitua o original, ajuste a lista `PHOTOS` de `tools/optimize-images.py` e rode o script |
| Avaliações | `index.html`, seções "MANUTENÇÃO" (destaque) e "AVALIAÇÕES". Fotos de perfil: lista `AVATARS` do script |

Mensagens de WhatsApp, conforme o ponto da página:

| Onde | Mensagem |
| --- | --- |
| Cabeçalho, hero, "Onde fica", rodapé e botão flutuante | Olá! Vi o site da Relojoaria Omega e quero mais informações. |
| Seção "Relógios" | ... quero saber sobre um relógio. |
| Seção "Manutenção e confecção" | ... quero saber sobre manutenção. |
| Chamada final | ... quero ajuda para escolher um presente. |

Para gerar as imagens (requer Pillow e a pasta `materiais-de-origem/`):

```bash
python3 tools/optimize-images.py
```

Se a proporção de uma foto mudar, atualize `width` e `height` da tag `<img>`
correspondente no `index.html`, para não haver salto de layout.

### Título do hero

O título tem três linhas ("Tradição e / confiança / há mais de 70 anos."), e o
tamanho da letra é calculado para a última linha caber na coluna em qualquer
tela. Se o texto mudar, confira a quebra em 320 px e em 900 px de largura. A
regra está em `.hero__title`, no `styles.css`. O mesmo vale para a chamada
final (`.closing__title`).

### Cache do navegador

Os arquivos de estilo e script são chamados com versão: `styles.css?v=1` e
`main.js?v=1`. Ao alterar um deles, aumente o número no `index.html` para que
os visitantes recebam a versão nova.

## Identidade visual

Direção: relojoaria tradicional, sóbria e escura, como a fachada da loja
(letreiro preto com o logo em prata). O dourado vem dos relógios das fotos e
do "70 anos" das artes da loja.

| Token | Cor | Origem |
| --- | --- | --- |
| `--graphite` | `#141416` | fundo do letreiro da fachada: hero, chamada final e rodapé |
| `--charcoal` | `#1F1F22` | grafite um pouco mais claro: seção "Manutenção" |
| `--silver` | `#E5E4E5` | prata do logo original: textos sobre o escuro |
| `--gold` | `#C9A24A` | dourado dos relógios: botões e rótulos sobre o escuro |
| `--gold-300` | `#DFC07A` | dourado clareado: destaques dos títulos sobre o escuro |
| `--gold-700` | `#7F611B` | dourado escurecido: destaques e rótulos sobre fundo claro |
| `--cream`, `--white` | `#F6F1E8`, `#FDFBF7` | fundos claros das seções, alternados |
| `--ink`, `--ink-soft` | `#1C1B19`, `#5D5952` | textos sobre fundo claro |
| `--whatsapp` | `#25D366` | verde oficial do WhatsApp, usado só no botão flutuante |

Tipografia: Crimson Pro (títulos, com o destaque em itálico dourado) e Inter
(textos). Sem gradientes, sem efeitos de vidro, sem emojis como ícones.

## Decisões de conteúdo

- Só foram usados dados fornecidos: nome, linhas de produto, frases da marca,
  endereço, telefones, Instagram, fotos e avaliações. Não há preços, marcas,
  prazos, garantias ou promessas inventadas.
- "Há mais de 70 anos" vem do briefing e da arte da fachada publicada pela
  loja. A página não diz o ano de fundação.
- "Troca de bateria e manutenção de relógios automáticos" vem das avaliações
  de Douglas e Martin, e a página diz isso ("são os serviços que os clientes
  mais citam nas avaliações").
- "Confecção" está no briefing sem detalhe. A página só convida a contar pelo
  WhatsApp o que a pessoa tem em mente.
- "Confirme o horário de atendimento pelo WhatsApp antes de vir" está na
  página porque o horário não foi informado.
- As fotos de perfil trazem um selo laranja com estrela, que já vem no arquivo
  recebido.
- Avaliações sem estrelas desenhadas e sem nota, porque nenhuma nota foi
  informada.
- O mapa é um mapa do Google incorporado, carregado pelo endereço. Ele só
  carrega quando o visitante chega perto da seção.
- Não há formulário, porque não existe destino de envio definido.
- A foto do hero não tem legenda.
- O ícone do botão flutuante é escuro sobre o verde, e não branco, para manter
  contraste suficiente.

## Testes realizados

Executados em 30/09/2026, em Chromium automatizado (Playwright).

- Revisão visual das capturas de tela: página inteira em 390 e 1440 px e
  primeira tela em 320, 768 e 1024 px.
- Sem rolagem horizontal e com o título do hero em três linhas (duas em
  768 px) nos tamanhos 320, 360, 390, 480, 600, 768, 820, 900, 1024, 1200,
  1440 e 1920 px.
- Sem erros de console e sem imagens quebradas.
- 41 verificações automáticas aprovadas: menu no celular (toque, Esc, toque
  fora, foco), âncoras, botão flutuante de WhatsApp (posição, nome acessível,
  sem cobrir o texto do rodapé), fotos sem ampliação acima do tamanho real,
  mapa com título e carregamento adiado, revelação na rolagem, link de pular
  para o conteúdo, foco visível, destino e atributos de todos os links, quatro
  mensagens de WhatsApp, hierarquia de títulos e atributos das imagens, sem
  travessões, emojis ou textos de exemplo.
- O mapa foi aberto no teste e mostrou o marcador na Av. Brasil, 4077.
- Página utilizável sem JavaScript.
- Animações desligadas quando o sistema pede movimento reduzido.
- Contraste AA em todos os textos (mínimo de 5,1:1).
- Carga inicial no celular de 563 KB, medida em tela de densidade 3x, sem
  saltos de layout (CLS 0). Página inteira: 571 KB, sem contar o mapa.
- O mapa do Google soma cerca de 1,8 MB, baixados só quando o visitante chega
  à seção "Onde fica".

Não testado: Safari, Firefox e aparelhos físicos. Dos links externos, foi
conferido apenas o endereço, não o conteúdo de destino. Também não foi
verificado se o número responde no WhatsApp.

## Histórico de ajustes

| Ajuste | Arquivos |
| --- | --- |
| Versão inicial da página | todos |
| Logo trocado pela versão branca enviada pelo cliente | `tools/optimize-images.py`, `assets/img`, `index.html` |

## Créditos e licenças

- Logo, fotos, avaliações e fotos de perfil: fornecidos pelo cliente.
- Ícones: criados para este projeto. Ícone do WhatsApp: Simple Icons (CC0).
- Crimson Pro e Inter: SIL Open Font License 1.1, obtidas do Google Fonts e
  hospedadas localmente.
- Mapa: Google Maps, incorporado.

## Pendências que dependem do cliente

- **Fotos originais, sem texto e em alta resolução.** As recebidas são
  capturas de tela de posts, recortadas para tirar o texto. Prioridade: a
  fachada (hoje com 673 px de largura), o interior da loja, joias e canetas.
- **Fotos de joias.** A linha "Joias" não tem foto; hoje ela aparece só em
  texto.
- **Direito de uso da foto da mulher de óculos.** Parece imagem de banco ou de
  fabricante. Se não houver licença, trocar por uma foto dos óculos da loja.
- **Marcas vendidas.** Se a loja quiser citar marcas, informar a lista. Hoje
  elas só aparecem dentro das fotos.
- **Ano de fundação**, para trocar "há mais de 70 anos" por uma data exata, se
  for o caso.
- Horário de funcionamento e formas de pagamento.
- Detalhes de confecção e de manutenção (o que é feito na loja, prazos,
  orçamento).
- Mais avaliações, com autorização de uso do nome e da foto.
- Domínio de publicação, para completar `og:image` com URL absoluta e adicionar
  `link rel="canonical"`.
- Fotos de perfil das avaliações têm 72 x 72 px. Ficam nítidas no tamanho usado
  (48 px), mas não podem ser ampliadas.
