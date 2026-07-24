# Design System — ForgeDocs

## Objetivo

Este documento estabelece os princípios de design, identidade visual e padrões de interface do ForgeDocs.

Seu objetivo é garantir consistência estética, previsibilidade dos componentes e uma experiência de usuário uniforme durante toda a evolução da aplicação.

Todas as decisões relacionadas à interface do ForgeDocs devem seguir os princípios e padrões definidos neste documento.

---

# Filosofia

O ForgeDocs é uma suíte desktop profissional.

A interface deve transmitir:

- Simplicidade
- Clareza
- Confiabilidade
- Produtividade
- Sobriedade

O objetivo é reduzir distrações para que o conteúdo seja sempre o protagonista.

---

# Inspirações

O Design System do ForgeDocs é inspirado em aplicações desktop modernas.

Principais referências:

- Linear
- Bitwarden
- TeamViewer
- Visual Studio Code
- Raycast

Cada referência contribui com aspectos específicos:

| Produto | Principal Contribuição |
|----------|------------|
| TeamViewer | Sidebar sóbria e espaçamento |
| Bitwarden | Navegação hierárquica recolhível |
| Linear | Tipografia e refinamento visual |
| VS Code | Estrutura da aplicação |
| Raycast | Minimalismo |

---

# Princípios

## Simplicidade

A interface deve conter apenas elementos necessários.

Evitar:

- excesso de cores
- excesso de bordas
- excesso de sombras
- excesso de informações

---

## Consistência

Todos os componentes devem compartilhar:

- cores
- tipografia
- espaçamentos
- estados
- comportamento

---

## Hierarquia Visual

A atenção do usuário deve seguir esta ordem:

1. Conteúdo
2. Ferramentas
3. Navegação
4. Elementos secundários

---

## Espaçamento

A interface deve respirar.

Sempre privilegiar espaços em branco em vez de aumentar a quantidade de elementos.

---

# Paleta

Tema padrão:

Dark

A aplicação utilizará apenas uma cor primária para destaque.

Estados:

- Normal
- Hover
- Ativo
- Desabilitado

---

# Tipografia

Objetivos:

- Alta legibilidade
- Pouco contraste visual
- Hierarquia clara

Regras:

- títulos destacados
- textos secundários discretos
- descrições curtas

---

# Sidebar

A Sidebar é a navegação principal da aplicação.

Ela deve permanecer fixa durante toda a utilização.

## Estrutura

ForgeDocs

↓

Início

↓

Grupos recolhíveis

- Converter
- Editar
- Otimizar
- Segurança

↓

Área administrativa

- Configurações
- Feedback
- Ajuda
- Sobre

---

## Características

- largura aproximada de 250 px
- fundo levemente diferente do conteúdo
- poucos separadores
- ícones minimalistas
- muito espaço em branco

---

# Navegação

A navegação segue estrutura hierárquica.

Exemplo:

Converter

↓

Word → PDF

↓

Execução da ferramenta

Os grupos permanecem recolhidos até interação do usuário.

---

# Ícones

Todos os ícones devem utilizar a mesma biblioteca.

Características:

- lineares
- minimalistas
- monocromáticos

Evitar:

- ícones coloridos
- estilos diferentes
- excesso de detalhes

---

## Conversões

Ferramentas de conversão devem utilizar a representação:

Origem → Destino

Exemplo:

Word → PDF

PDF → Word

Excel → PDF

A navegação deve privilegiar o formato de origem, facilitando a identificação da ferramenta.

---

# Componentes

Os componentes devem ser reutilizáveis.

Exemplos:

- FeatureCard
- SidebarItem
- SidebarGroup
- PrimaryButton
- SecondaryButton
- Dialog
- ProgressBar

---

# Estados

Todos os componentes devem implementar estados consistentes.

- Normal
- Hover
- Focus
- Active
- Disabled

---

# Animações

As animações devem ser discretas.

Priorizar:

- expansão dos grupos
- transições suaves
- mudanças de estado

Evitar animações chamativas.

---

# Visão de Design

O ForgeDocs deve transmitir a sensação de uma suíte desktop moderna, profissional e confiável.

A interface deve ser elegante, discreta e funcional, priorizando produtividade em vez de efeitos visuais.

---

> **Nota**
>
> Este documento é evolutivo e será atualizado conforme novas decisões de design forem consolidadas durante o desenvolvimento do ForgeDocs.