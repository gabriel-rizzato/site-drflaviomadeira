# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Landing page para Dr. Flávio Madeira, urologista especialista em cirurgia robótica em Goiânia (CRM: 9165/GO | RQE 5858). O objetivo da página é converter visitantes em agendamentos via WhatsApp.

## Stack

- HTML puro + Tailwind CSS via CDN (sem build, sem npm, sem framework)
- JavaScript vanilla inline no próprio HTML
- Sem testes automatizados

Para visualizar, basta abrir `index.html` diretamente no navegador.

## Estrutura

- `index.html` — página principal e única (todo CSS customizado e JS estão inline)
- `assets/icons/` — SVGs de ícones; `sprite.svg` é o sprite consolidado; `icons.json` lista os ícones disponíveis
- `assets/img/` — imagens em WebP (`img_webp/`) e originais (`originais/`)
- `botao_wpp/` — componentes isolados do botão flutuante de WhatsApp (duas variantes: padrão e mini-mobile)
- `meta.ia/` — versão gerada/explorada via Meta AI, usada como referência

## Branches

- `main` — versão estável/publicada
- `fork02` — branch de desenvolvimento ativo (atual); fazer PR para `main` ao concluir
- `historico/fork-lp-cirurgiarobotica` — arquivo de versões anteriores ao GitHub (não editar)

## Seções do index.html (ordem)

1. **Header** — logo, nome do médico, CRM, botão "Agendar Avaliação" (desktop)
2. **Hero** — headline, subtítulo, CTA WhatsApp + link âncora para #vantagens, social proof (+400 cirurgias)
3. **O que é Cirurgia Robótica** — fundo `darkblue`, 4 cards: Tecnologia, Minimamente Invasiva, Visão, Recuperação
4. **Sobre o Médico** — foto, credenciais, stats (400+ cirurgias, 15+ anos), tags de associações, técnicas realizadas (Da Vinci, HoLEP, Rezum), painel colapsável de formação acadêmica, card de locais de atendimento (IRG, Einstein, online)
5. **Indicações** — fundo `darkblue`, 3 cards: Câncer de Próstata, Câncer de Rim, Reconstruções Complexas
6. **Depoimentos** — 4 cards com relatos reais de pacientes
7. **9 Vantagens** (`id="vantagens"`) — fundo `darkblue`, grid 3 colunas, botão CTA
8. **Como Funciona** (`id="como-funciona"`) — passo a passo dos 4 braços robóticos + imagem
9. **CTA Final** — fundo `darkblue`, botão WhatsApp
10. **Footer** — créditos Eleva Soluções / Gabriel Rizzato
11. **Botão flutuante WhatsApp** — canto inferior direito, tooltip hover
12. **Modal WhatsApp** — formulário com campos: nome, telefone (com máscara), motivo (select), mensagem

## Modal WhatsApp — Rastreamento

O modal gera um ticket de rastreamento a partir de parâmetros de UTM/clique:
- Lê `gclid`, `fbclid`, `ttclid` ou `msclkid` da URL ou `localStorage`
- Extrai 6 caracteres (posições 26–32) e anexa como `*id: XXXXXX*` na mensagem do WhatsApp
- Número de destino: `5562999789482`

## Design Tokens

Definidos no `tailwind.config` inline do `index.html`:

```js
colors: { primary: '#0a66c2', darkblue: '#0a2540' }
fontFamily: { sans: ['Inter', 'sans-serif'] }
```

## Padrões do Projeto

- Animações de entrada: classes `.reveal`, `.reveal-left`, `.reveal-right` ativadas por IntersectionObserver
- CTA principal: `onclick="openWaModal()"` abre modal de WhatsApp para agendamento
- Imagens responsivas: versão mobile e desktop declaradas via `block md:hidden` / `hidden md:block`
- Respeitar `@media (prefers-reduced-motion)` já configurado no CSS global
- Formação acadêmica: painel colapsável via `toggleFormacao()` com animação `max-height` + `opacity`
