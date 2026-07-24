# ForgeDocs Design System

**Versão:** 2.0  
**Status:** Estável  
**Última atualização:** 2026-07-24

---

# Índice

1. Introdução
2. Objetivos
3. Filosofia
4. Personalidade da Marca
5. Princípios de Design
6. Inspirações
7. Identidade Visual
8. Design Tokens
9. Sistema de Cores
10. Tipografia
11. Espaçamento
12. Grid e Layout
13. Bordas e Raios
14. Elevação
15. Iconografia
16. Motion
17. Componentes
18. Estados
19. Acessibilidade
20. UX Writing
21. Convenções
22. Evolução do Design System

---

# 1. Introdução

## Objetivo

O Design System do ForgeDocs define a linguagem visual oficial da aplicação.

Seu propósito é garantir consistência entre todas as telas, componentes e fluxos de interação, estabelecendo padrões reutilizáveis para desenvolvimento e futuras evoluções do produto.

Este documento representa a fonte oficial para todas as decisões relacionadas ao design da interface.

Sempre que houver divergência entre implementações, este documento prevalece.

---

## Escopo

Este documento contempla:

- identidade visual;
- princípios de design;
- sistema tipográfico;
- sistema de cores;
- componentes visuais;
- tokens de interface;
- convenções de nomenclatura;
- diretrizes de acessibilidade.

Não contempla regras específicas de implementação de telas. Essas pertencem ao documento **UI Guidelines**.

---

# 2. Objetivos

O Design System busca atingir cinco objetivos principais.

## Consistência

Todos os componentes devem compartilhar a mesma linguagem visual.

O usuário nunca deve perceber diferenças de estilo entre módulos distintos da aplicação.

---

## Escalabilidade

Novas funcionalidades devem ser capazes de reutilizar componentes existentes, evitando duplicação de interface.

---

## Manutenibilidade

Mudanças visuais devem ocorrer de forma centralizada.

Sempre que possível, alterações devem acontecer através de Design Tokens, evitando modificações individuais em componentes.

---

## Clareza

Cada elemento visual deve possuir uma função claramente identificável.

Elementos decorativos sem propósito devem ser evitados.

---

## Produtividade

O design deve reduzir o esforço cognitivo do usuário, permitindo foco total na tarefa executada.

---

# 3. Filosofia

ForgeDocs é uma suíte desktop profissional voltada para produtividade.

A interface deve transmitir:

- simplicidade;
- estabilidade;
- confiabilidade;
- precisão;
- organização;
- eficiência.

O conteúdo sempre possui prioridade sobre elementos gráficos.

A interface existe para facilitar o trabalho do usuário, nunca para competir por atenção.

---

# 4. Personalidade da Marca

O ForgeDocs adota uma identidade visual baseada em sobriedade e confiança.

A aplicação deve ser percebida como:

- moderna;
- profissional;
- discreta;
- técnica;
- robusta.

Evita-se qualquer característica associada a interfaces lúdicas, excessivamente coloridas ou voltadas ao entretenimento.

---

# 5. Princípios de Design

## Minimalismo Funcional

Todo elemento deve possuir um propósito claro.

Se um componente não agrega valor à experiência do usuário, sua existência deve ser reconsiderada.

---

## Hierarquia Visual

A atenção do usuário deve seguir a seguinte prioridade:

1. Conteúdo
2. Ação principal
3. Navegação
4. Informações secundárias
5. Elementos decorativos

---

## Consistência

Componentes equivalentes devem possuir aparência e comportamento equivalentes.

O usuário não deve precisar reaprender a utilizar uma funcionalidade semelhante.

---

## Performance Percebida

A interface deve transmitir rapidez.

Feedbacks visuais imediatos são preferíveis a longos períodos sem resposta.

---

## Desktop First

Todas as decisões de interface priorizam utilização em computadores com teclado e mouse.

---

# 6. Inspirações

O ForgeDocs não replica a identidade visual de nenhuma aplicação específica.

Sua linguagem visual é resultado da combinação de referências consolidadas no mercado.

| Produto | Principal influência |
|----------|----------------------|
| Linear | Tipografia e refinamento visual |
| Raycast | Minimalismo |
| Visual Studio Code | Estrutura geral da aplicação |
| Bitwarden | Navegação hierárquica |
| TeamViewer | Sidebar e organização espacial |

Cada referência contribui apenas com conceitos, nunca com reprodução direta de elementos visuais.

---
# 7. Identidade Visual

## Visão Geral

A identidade visual do ForgeDocs foi projetada para transmitir profissionalismo, estabilidade e clareza.

A interface prioriza a produtividade, reduzindo distrações visuais e direcionando a atenção do usuário para o conteúdo e para as tarefas executadas.

Todos os elementos visuais devem seguir uma linguagem uniforme, baseada em poucos elementos gráficos, alto nível de consistência e excelente legibilidade.

---

## Tema Principal

O ForgeDocs adota **Dark Mode** como tema padrão.

A escolha do tema escuro reduz o contraste excessivo durante longos períodos de utilização e proporciona uma aparência mais técnica e moderna.

O suporte ao tema claro poderá ser implementado futuramente sem alterar a estrutura do Design System.

---

## Linguagem Visual

A interface deve transmitir:

- organização;
- simplicidade;
- precisão;
- estabilidade;
- elegância discreta.

Evita-se:

- gradientes chamativos;
- excesso de sombras;
- excesso de bordas;
- excesso de animações;
- cores saturadas.

---

## Identidade dos Componentes

Todos os componentes devem seguir o mesmo padrão visual.

Características obrigatórias:

- cantos arredondados;
- espaçamentos consistentes;
- alinhamento rigoroso;
- contraste suficiente para leitura;
- estados visuais previsíveis.

---

# 8. Design Tokens

## Objetivo

Design Tokens representam os valores fundamentais utilizados por toda a interface.

Nenhum componente deve utilizar valores "mágicos" diretamente no código.

Sempre que possível, todos os componentes devem consumir tokens centralizados.

Os tokens garantem:

- consistência;
- reutilização;
- facilidade de manutenção;
- futura implementação de múltiplos temas.

---

## Categorias

O ForgeDocs organiza seus tokens nas seguintes categorias:

- Colors
- Typography
- Spacing
- Radius
- Borders
- Icons
- Motion

---

## Convenção de Nomeação

Todos os tokens devem utilizar nomes descritivos.

Exemplos:

BACKGROUND_DEFAULT

SURFACE_DEFAULT

SURFACE_HOVER

TEXT_PRIMARY

TEXT_SECONDARY

TEXT_DISABLED

ACCENT_PRIMARY

ACCENT_HOVER

SUCCESS

WARNING

ERROR

BORDER_DEFAULT

BORDER_ACTIVE

### Nunca utilizar nomes genéricos como:

color1

darkGray

blue2

greenLight

A nomenclatura deve representar a função do token e não sua aparência.

---

## 8.1 Tokens de Espaçamento

Todos os espaçamentos da interface devem utilizar os tokens definidos abaixo.

É proibida a utilização de valores numéricos diretamente nos componentes, salvo quando tecnicamente justificado.

| Token | Valor | Utilização |
|--------|------:|------------|
| SPACING_NONE | 0 px | Sem espaçamento |
| SPACING_XS | 4 px | Ajustes mínimos |
| SPACING_SM | 8 px | Distâncias curtas |
| SPACING_MD | 16 px | Espaçamento padrão |
| SPACING_LG | 24 px | Separação entre grupos |
| SPACING_XL | 32 px | Separação entre seções |
| SPACING_XXL | 48 px | Grandes áreas |

---

Exemplo

✔ Correto

padding = SPACING_LG

✘ Incorreto

padding = 24

---
## 8.2 Tokens de Radius

Os cantos arredondados seguem uma escala padronizada.

| Token | Valor | Utilização |
|--------|------:|------------|
| RADIUS_NONE | 0 px | Elementos estruturais |
| RADIUS_SM | 4 px | Inputs |
| RADIUS_MD | 8 px | Botões |
| RADIUS_LG | 12 px | Cards |
| RADIUS_XL | 16 px | Diálogos |

---

## 8.3 Tokens de Elevação

A aplicação utiliza elevação mínima.

As sombras não devem substituir contraste e espaçamento.

| Token | Utilização |
|--------|------------|
| ELEVATION_NONE | Elementos comuns |
| ELEVATION_LOW | Menus |
| ELEVATION_MEDIUM | Dialogs |
| ELEVATION_HIGH | Modais críticos |
---

## 8.4 Tokens de Ícones

Todos os ícones seguem tamanhos padronizados.

| Token | Valor |
|--------|------:|
| ICON_XS | 12 px |
| ICON_SM | 16 px |
| ICON_MD | 20 px |
| ICON_LG | 24 px |
| ICON_XL | 32 px |

---
## 8.5 Tokens Tipográficos

| Token | Peso | Tamanho | Uso |
|--------|------|---------|-----|
| HERO_TITLE | ExtraBold | 44 px | Hero |
| DISPLAY | Bold | 36 px | Destaques |
| PAGE_TITLE | Bold | 30 px | Títulos |
| SECTION_TITLE | SemiBold | 24 px | Seções |
| BODY | Regular | 16 px | Texto |
| BODY_MEDIUM | Medium | 16 px | Destaques |
| CAPTION | Medium | 13 px | Legendas |
| BUTTON | SemiBold | 15 px | Botões |
| NAVIGATION | Medium | 15 px | Sidebar |
| NAVIGATION_ACTIVE | SemiBold | 15 px | Item ativo |

---
## 8.6 Tokens de Cor

## Background

BACKGROUND_DEFAULT

BACKGROUND_SECONDARY

---

## Surface

SURFACE_DEFAULT

SURFACE_HOVER

SURFACE_ACTIVE

---

## Text

TEXT_PRIMARY

TEXT_SECONDARY

TEXT_DISABLED

---

## Accent

ACCENT_PRIMARY

ACCENT_HOVER

ACCENT_ACTIVE

---

## Borders

BORDER_DEFAULT

BORDER_ACTIVE

---

## Status

SUCCESS

WARNING

ERROR

INFO

---

# 9. Sistema de Cores

## Filosofia

O sistema de cores do ForgeDocs é baseado em uma paleta reduzida.

As cores existem para comunicar estado, hierarquia e ação.

Jamais devem ser utilizadas apenas como elemento decorativo.

---

## Estrutura

As cores estão organizadas em cinco grupos.

### Background

Responsável pelo fundo principal da aplicação.

Utilizado em:

- janela principal;
- páginas;
- áreas de trabalho.

---

### Surface

Utilizado em elementos posicionados sobre o fundo principal.

Exemplos:

- cards;
- sidebar;
- painéis;
- diálogos.

---

### Text

Define toda a hierarquia textual da aplicação.

Categorias previstas:

TEXT_PRIMARY

TEXT_SECONDARY

TEXT_TERTIARY

TEXT_DISABLED

---

### Accent

Representa ações primárias.

Utilizado em:

- botões principais;
- links;
- seleção;
- indicadores ativos.

---

### Significado dos Termos

**STATUS:** Representam feedback visual ao usuário.

**SUCCESS:** Indica que uma operação foi concluída com sucesso.

**WARNING:** Indica uma situação que requer atenção, mas que não impede a continuidade da operação.

**ERROR:** Indica uma falha que impede ou compromete a execução da operação.

**INFO:** Indica uma informação complementar ou informativa ao usuário.

---

## Regras

Nunca utilizar uma cor diretamente. Sempre utilizar um token.

### Exemplo:

✔ correto

ACCENT_PRIMARY

✘ incorreto

#3B82F6

---

As cores nunca devem comunicar significado sozinhas.

Sempre devem ser acompanhadas por:

- texto;
- ícone;
- indicador visual.

---

# 10. Tipografia

## Família Tipográfica

Fonte oficial: **Host Grotesk**

A família tipográfica foi escolhida por oferecer excelente legibilidade, ampla variedade de pesos e aparência moderna adequada a aplicações desktop.

Todas as telas devem utilizar exclusivamente esta família.

---

## Escala Tipográfica

| Token | Peso | Tamanho | Utilização |
|--------|------|---------|------------|
| Hero | ExtraBold | 44 px | Hero Banner |
| Display | Bold | 36 px | Grandes destaques |
| Page Title | Bold | 30 px | Títulos de páginas |
| Section Title | SemiBold | 24 px | Seções |
| Body | Regular | 16 px | Texto principal |
| Body Medium | Medium | 16 px | Destaques leves |
| Caption | Medium | 13 px | Legendas |
| Button | SemiBold | 15 px | Botões |
| Navigation | Medium | 15 px | Sidebar |
| Navigation Active | SemiBold | 15 px | Item ativo |

---

## Hierarquia

A leitura deve seguir esta sequência:

Hero

↓

Título da Página

↓

Título da Seção

↓

Texto Principal

↓

Legenda

Nunca inverter esta hierarquia.

---

## Pesos

Light: **Utilizado apenas em casos excepcionais.**

Regular: **Texto padrão.**

Medium: **Ênfase leve.**

SemiBold: **Navegação e títulos intermediários.**

Bold: **Títulos principais.**

ExtraBold: **Exclusivamente Hero Banner.**

---

## Regras

Evitar utilizar mais de três pesos diferentes na mesma tela.

Evitar excesso de texto em Bold.

Utilizar o tamanho da fonte como principal mecanismo de hierarquia, recorrendo ao peso apenas como reforço.

Todas as fontes devem ser obtidas através do módulo `typography.py`, evitando definições locais nos componentes.

# 11. Sistema de Espaçamento

## Objetivo

O sistema de espaçamento define as distâncias padronizadas entre elementos da interface.

Sua principal finalidade é garantir consistência visual, melhorar a legibilidade e facilitar a organização dos componentes em toda a aplicação.

Todo espaçamento utilizado no ForgeDocs deve seguir uma escala previamente definida.

---

## Princípios

O espaçamento deve:

- criar uma hierarquia visual clara;
- separar grupos de informações relacionadas;
- evitar poluição visual;
- proporcionar equilíbrio entre conteúdo e espaço em branco.

O espaço vazio faz parte da interface e deve ser tratado como um elemento de design.

---

## Escala Base

Toda a interface utiliza uma escala baseada em múltiplos de 4 pixels.

| Token | Valor | Utilização |
|--------|------:|------------|
| XS | 4 px | Ajustes mínimos |
| SM | 8 px | Distâncias curtas |
| MD | 16 px | Espaçamento padrão |
| LG | 24 px | Separação entre grupos |
| XL | 32 px | Separação entre seções |
| XXL | 48 px | Grandes blocos de conteúdo |

---

## Aplicações

### Componentes

Espaçamento interno:

16 px

---

### Cards

Padding interno:

24 px

Distância entre cards:

16 px

---

### Seções

Distância vertical:

32 px

---

### Página

Margem externa:

32 px

---

## Regras

Nunca utilizar valores arbitrários.

Sempre utilizar um dos valores definidos na escala.

Caso seja necessário um novo espaçamento, ele deverá ser incorporado ao Design System antes de ser utilizado na interface.

---

# 12. Grid e Layout

## Objetivo

O sistema de layout organiza os componentes da interface de forma consistente.

Todas as páginas devem seguir uma estrutura previsível, permitindo que o usuário encontre rapidamente as informações desejadas.

---

## Estrutura Geral

A estrutura padrão da aplicação é composta por:

Sidebar

↓

Header

↓

Área de Conteúdo

↓

Componentes

↓

Status Bar (quando aplicável)

---

## Layout Principal

A Sidebar permanece fixa durante toda a utilização.

O conteúdo principal ocupa o espaço restante da janela.

Não devem existir múltiplas barras laterais competindo pela atenção do usuário.

---

## Área de Conteúdo

A área principal deve priorizar:

- clareza;
- espaçamento;
- alinhamento;
- leitura contínua.

Evitar agrupamentos excessivamente densos de componentes.

---

## Organização das Páginas

Toda página deve conter:

1. Cabeçalho
2. Descrição (quando necessária)
3. Área principal
4. Ações secundárias
5. Rodapé técnico (quando aplicável)

---

## Responsividade

Embora seja uma aplicação desktop, a interface deve adaptar-se corretamente ao redimensionamento da janela.

Os componentes devem:

- preservar alinhamentos;
- evitar sobreposição;
- respeitar margens mínimas;
- reorganizar o conteúdo quando necessário.

---

# 13. Bordas e Raios

## Objetivo

Os raios de borda contribuem para uma aparência moderna e uniforme.

Todos os componentes devem compartilhar a mesma linguagem visual.

---

## Diretrizes

Os cantos arredondados devem ser discretos.

Evitar:

- cantos excessivamente arredondados;
- mistura de estilos.

---

## Aplicação

Utilizar bordas arredondadas em:

- cards;
- botões;
- campos de entrada;
- diálogos;
- menus.

Evitar bordas arredondadas em elementos puramente estruturais.

---

## Bordas

As bordas devem possuir baixo contraste.

Seu objetivo é organizar a interface, não chamar atenção.

Sempre utilizar tokens definidos pelo sistema de cores.

---

# 14. Elevação

## Objetivo

O ForgeDocs utiliza elevação de forma mínima.

A interface não depende de sombras para estabelecer hierarquia.

---

## Princípios

Priorizar:

- contraste entre superfícies;
- espaçamento;
- alinhamento.

Sombras devem ser utilizadas apenas quando realmente agregarem compreensão visual.

---

## Utilização

A elevação poderá ser aplicada em:

- menus flutuantes;
- caixas de diálogo;
- popovers;
- tooltips.

Cards comuns não necessitam de sombras perceptíveis.

---

# 15. Iconografia

## Objetivo

Os ícones complementam o texto e aceleram o reconhecimento das funcionalidades.

Eles nunca substituem completamente a informação textual.

---

## Biblioteca

Toda a aplicação deve utilizar uma única biblioteca de ícones.

Misturar bibliotecas diferentes compromete a consistência visual.

---

## Características

Os ícones devem ser:

- lineares;
- monocromáticos;
- minimalistas;
- facilmente reconhecíveis.

---

## Tamanho

Os tamanhos utilizados devem seguir uma escala consistente.

Evitar variações desnecessárias.

---

## Utilização

Os ícones podem ser utilizados em:

- Sidebar;
- Botões;
- Cards;
- Menus;
- Alertas;
- Diálogos;
- Barras de ferramentas.

---

## Regras

Ícones não devem ser utilizados como elemento decorativo.

Sempre que possível, devem acompanhar um rótulo textual, principalmente em funcionalidades críticas.

Ícones devem comunicar ações e estados, nunca substituir completamente a navegação textual.

---
# 16. Motion

## Objetivo

As animações do ForgeDocs existem para comunicar mudanças de estado, reforçar a hierarquia visual e fornecer feedback imediato ao usuário.

As animações nunca devem existir apenas por efeito estético.

---

## Princípios

Toda animação deve ser:

- rápida;
- discreta;
- previsível;
- consistente.

A interface deve transmitir fluidez, sem comprometer a produtividade.

---

## Aplicações

Animações podem ser utilizadas em:

- expansão e recolhimento da Sidebar;
- abertura de diálogos;
- alteração de estados dos botões;
- carregamento de componentes;
- notificações;
- indicadores de progresso.

---

## Evitar

Não utilizar animações para:

- movimentar grandes áreas da interface;
- alterar continuamente a posição de componentes;
- chamar atenção do usuário sem necessidade.

---

## Duração

As transições devem permanecer curtas.

Recomendação:

| Tipo | Duração |
|-------|---------:|
| Hover | 100–150 ms |
| Clique | 80–120 ms |
| Expansão | 200–250 ms |
| Diálogo | 200–300 ms |

---

## Feedback

Toda ação iniciada pelo usuário deve apresentar alguma resposta visual em até 100 ms.

---

# 17. Componentes

## Objetivo

Os componentes representam os blocos reutilizáveis da interface.

Todo novo elemento visual deve ser desenvolvido a partir de componentes reutilizáveis, evitando duplicação de código e inconsistências visuais.

---

## Componentes previstos

### Navegação

- Sidebar
- SidebarGroup
- SidebarItem
- SidebarFooter

---

### Estrutura

- PageHeader
- Section
- Toolbar
- Divider

---

### Conteúdo

- FeatureCard
- InfoCard
- StatusCard
- EmptyState

---

### Ações

- PrimaryButton
- SecondaryButton
- IconButton

---

### Entrada

- TextField
- SearchField
- ComboBox
- CheckBox
- Switch

---

### Feedback

- Dialog
- Toast
- ProgressBar
- StatusBadge

---

## Regras

Todo componente deve possuir:

- responsabilidade única;
- documentação;
- reutilização;
- nomenclatura consistente;
- estados definidos.

---

## Estados obrigatórios

Sempre que aplicável:

- Default
- Hover
- Focus
- Active
- Disabled
- Loading

---

# 18. Estados

## Objetivo

Todos os componentes devem responder visualmente às interações do usuário.

Estados consistentes tornam a interface previsível e reduzem o esforço cognitivo.

---

## Default

Estado inicial.

Nenhuma interação ocorreu.

---

## Hover

Indica que o cursor encontra-se sobre o componente.

O Hover deve ser sutil.

---

## Focus

Representa navegação por teclado.

O indicador de foco nunca deve ser removido.

---

## Active

Representa interação ativa durante o clique.

---

## Selected

Representa itens atualmente selecionados.

---

## Disabled

O componente permanece visível, porém indisponível.

Deve comunicar claramente sua indisponibilidade.

---

## Loading

Operações demoradas devem impedir múltiplas execuções simultâneas.

Sempre apresentar feedback visual.

---

## Success

Comunica conclusão bem-sucedida.

---

## Warning

Comunica situação que exige atenção.

---

## Error

Comunica falha ou interrupção.

---

## Empty

Representa ausência de dados.

Sempre apresentar orientação clara ao usuário.

---

# 19. Acessibilidade

## Objetivo

O ForgeDocs deve ser utilizável pelo maior número possível de pessoas.

Embora seja uma aplicação desktop, princípios de acessibilidade devem ser considerados desde o início do desenvolvimento.

---

## Diretrizes

Priorizar:

- contraste adequado;
- tipografia legível;
- ícones compreensíveis;
- áreas clicáveis confortáveis;
- navegação previsível.

---

## Navegação

Sempre que possível:

- suporte à navegação por teclado;
- ordem lógica de foco;
- atalhos consistentes.

---

## Texto

Evitar:

- textos excessivamente longos;
- mensagens ambíguas;
- jargões desnecessários.

---

## Ícones

Ícones críticos devem possuir descrição textual.

Nunca depender exclusivamente da cor para transmitir significado.

---

# 20. UX Writing

## Objetivo

O ForgeDocs adota uma linguagem objetiva, técnica e amigável.

Todo texto da interface deve auxiliar o usuário na realização da tarefa.

---

## Princípios

As mensagens devem ser:

- claras;
- curtas;
- diretas;
- consistentes.

---

## Botões

Utilizar verbos de ação.

Exemplos:

✔ Converter

✔ Salvar

✔ Exportar

✘ OK

✘ Executar Processo

---

## Mensagens de Erro

Informar:

- o que ocorreu;
- quando possível, por que ocorreu;
- como resolver.

---

## Mensagens de Sucesso

Devem confirmar a conclusão da operação.

Exemplo:

Documento convertido com sucesso.

---

## Placeholders

Placeholders complementam o campo.

Nunca substituem um rótulo.

---

# 21. Convenções

## Objetivo

Padronizar nomenclaturas utilizadas durante o desenvolvimento.

---

## Componentes

Utilizar PascalCase.

Exemplos:

HeroBanner

PrimaryButton

SidebarItem

StatusBadge

---

## Arquivos

Utilizar snake_case.

Exemplos:

hero_banner.py

primary_button.py

status_badge.py

---

## Tokens

Sempre em UPPER_CASE.

Exemplos:

TEXT_PRIMARY

BACKGROUND_DEFAULT

SPACING_MD

---

## Classes

PascalCase.

---

## Funções

snake_case.

---

## Constantes

UPPER_CASE.

---

## Variáveis

snake_case.

---

# 22. Evolução do Design System

## Objetivo

Garantir que o Design System permaneça consistente durante toda a evolução do ForgeDocs.

---

## Inclusão de novos componentes

Todo novo componente deve:

- possuir finalidade clara;
- reutilizar tokens existentes;
- seguir a identidade visual;
- possuir documentação.

---

## Inclusão de novos tokens

Novos tokens somente devem ser criados quando não houver um equivalente existente.

Duplicações devem ser evitadas.

---

## Alterações

Mudanças em tokens existentes devem considerar o impacto sobre toda a aplicação.

Sempre que possível, alterações devem ser centralizadas.

---

## Compatibilidade

O Design System deve permanecer compatível com versões anteriores sempre que tecnicamente viável.

Mudanças incompatíveis deverão ser documentadas.

---

## Revisões

Este documento é evolutivo.

Sempre que novas decisões de design forem consolidadas, este documento deverá ser atualizado antes da implementação definitiva.