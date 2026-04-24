# CONTEXTO DO PROJETO

## Arquivo principal
- `05 - Criando-site-Dr.-Flavio-Madeira.html`

## Funcionalidade atual
- Página estática em HTML com Tailwind via CDN.
- Navegação fixa no topo com CTA de WhatsApp.
- Hero com proposta de valor, subtítulo, CTA principal e imagem de destaque.
- Seções estruturadas:
  - O que é
  - Como funciona
  - Indicações
  - Vantagens
  - Cirurgia robótica no Brasil
  - Recuperação e pós-operatório
  - Sobre o Dr. Flávio
  - Depoimentos
  - CTA final
  - Footer
- Elemento flutuante fixo do WhatsApp no canto inferior direito.

## Funcionalidade de rastreamento / links
- Captura parâmetros `gclid`, `gbraid` ou `wbraid` da URL.
- Armazena valor em `localStorage` com timestamp.
- Expira após 90 dias.
- Atualiza todos os links com classe `whatsapp-link` para usar:
  - `https://wa.me/556232387800?text=...`
- Usa o atributo `data-text` para gerar o texto padrão de cada link.
- Inclui código para abrir o link em nova aba com `target="_blank"` e `rel="noopener"`.

## Itens pendentes
- Substituir imagens placeholder pelo ativo final:
  - `/wp-content/uploads/hero-dr-flavio.webp`
  - `/wp-content/uploads/como-funciona.webp`
  - `/wp-content/uploads/recuperacao.webp`
  - `/wp-content/uploads/dr-flavio-perfil.webp`
- Revisar textos e credenciais com o cliente.
- Ajustar SEO e metadados finais.
- Validar no servidor / ambiente do WordPress.

## Sugestão de uso da memória de contexto
- Atualizar o arquivo sempre que houver mudança relevante no layout, conteúdo ou rastreamento.
- Manter no repositório para consulta rápida.
- Usar commits claros ao fazer alterações.
- Registrar próximos passos e decisões importantes.