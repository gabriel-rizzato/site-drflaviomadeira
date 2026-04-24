# DESIGN.md — System Design Reference

## Cores
| Token | Hex | Uso |
|---|---|---|
| `primary` | `#0a66c2` | CTAs, links, destaques, ícones |
| `darkblue` | `#0a2540` | Fundo de seções escuras |
| slate-900 | Tailwind | Títulos |
| slate-700/600 | Tailwind | Texto de corpo |
| slate-200/100 | Tailwind | Bordas e fundos suaves |

## Tipografia
- Fonte: **Inter** (Google Fonts) — pesos 400, 500, 600, 700, 800
- H1: `text-[40px] lg:text-6xl font-extrabold tracking-tight`
- H2 seções: `text-3xl lg:text-4xl font-bold`
- Corpo: `text-lg text-slate-700 leading-relaxed`
- Labels/badges: `text-sm font-semibold`

## Componentes

### Botão primário
```html
bg-[#0a66c2] text-white px-7 py-3.5 rounded-xl font-semibold
hover:bg-[#0957a5] shadow-lg shadow-[#0a66c2]/25 hover:-translate-y-0.5 transition-all
```

### Botão secundário
```html
bg-white text-slate-800 px-7 py-3.5 rounded-xl font-semibold
border border-slate-200 hover:bg-slate-50 transition-all
```

### Badge / pill
```html
bg-white/85 backdrop-blur-md text-[#0a66c2] border border-[#0a66c2]/20
px-4 py-1.5 rounded-full text-sm font-semibold shadow-sm
```

### Card de stat
```html
bg-slate-50 rounded-xl p-4 border border-slate-100
```

## Animações
- Entrada: `.reveal` (fade + translateY), `.reveal-left`, `.reveal-right` — ativadas por IntersectionObserver
- Delays: `.reveal-delay-1` a `.reveal-delay-4` (110ms steps)
- Respeita `prefers-reduced-motion`

## Layout
- Container: `max-w-7xl mx-auto px-6 lg:px-8`
- Seções: `py-24` padrão
- Seções escuras: `bg-[#0a2540] text-white`
- Seções claras: `bg-white` ou `bg-slate-50`

## CTA principal
Todo botão de agendamento chama `onclick="openWaModal()"` — abre modal de WhatsApp.
