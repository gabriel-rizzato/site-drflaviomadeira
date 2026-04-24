# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Landing page para Dr. Flávio Madeira, urologista especialista em cirurgia robótica em Goiânia (CRM-GO 14184). O objetivo da página é converter visitantes em agendamentos via WhatsApp.

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
- `fork01` — desenvolvimento ativo; fazer PR para `main` ao concluir
- `historico/fork-lp-cirurgiarobotica` — arquivo de versões anteriores ao GitHub (não editar)

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
