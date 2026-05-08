# lp-drflavio-cirurgia-robotica

Landing page de conversão para Dr. Flávio Madeira — urologista especialista em cirurgia robótica em Goiânia (CRM: 9165/GO).

## Objetivo

Converter visitantes em agendamentos via WhatsApp, com foco em pacientes com indicação de cirurgia robótica (câncer de próstata, câncer de rim, reconstruções complexas).

## Stack

- HTML puro + Tailwind CSS via CDN
- JavaScript vanilla inline
- Sem build, sem npm, sem framework

## Como usar

Abrir `index.html` diretamente no navegador. Nenhuma instalação necessária.

## Branches

| Branch | Uso |
|---|---|
| `main` | Versão publicada/estável |
| `fork02` | Desenvolvimento ativo |
| `historico/fork-lp-cirurgiarobotica` | Arquivo histórico (não editar) |

## Estrutura

```
lp-drflavio-cirurgia-robotica/
├── index.html              ← página principal (CSS e JS inline)
├── assets/
│   ├── icons/              ← sprite SVG + icons.json
│   └── img/                ← imagens em WebP e originais
└── botao_wpp/              ← variantes isoladas do botão WhatsApp
```

## Documentação

- [CLAUDE.md](CLAUDE.md) — estrutura da página, padrões de código, rastreamento do modal
- [DESIGN.md](DESIGN.md) — tokens de design, componentes, animações
