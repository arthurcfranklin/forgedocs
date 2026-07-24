# Engineering Guidelines

**Versão:** 1.0  
**Status:** Stable  
**Atualização:** 24/07/2026

---

## Objetivo

Este documento estabelece as diretrizes de engenharia para o desenvolvimento do ForgeDocs, definindo padrões de implementação, organização do código e boas práticas adotadas no projeto.

Enquanto o **Coding Standards** define como o código deve ser escrito, este documento define como as funcionalidades devem ser implementadas dentro da arquitetura da aplicação.

---

# 1. Filosofia de Desenvolvimento

O ForgeDocs adota uma filosofia de desenvolvimento baseada em simplicidade, consistência e escalabilidade.

Toda implementação deve priorizar:

- simplicidade;
- legibilidade;
- reutilização;
- desacoplamento;
- responsabilidade única;
- manutenção facilitada.

O objetivo é construir uma aplicação que permaneça organizada mesmo após anos de evolução.

---

# 2. Relação com os Demais Documentos

Cada documento possui uma responsabilidade específica.

| Documento | Responsabilidade |
|------------|------------------|
| Architecture | Organização geral da aplicação |
| Coding Standards | Convenções de escrita |
| Design System | Identidade visual |
| UI Guidelines | Construção da interface |
| Engineering Guidelines | Implementação das funcionalidades |

Nenhum documento substitui outro.

---

# 3. Estrutura do Projeto

A organização da aplicação deve respeitar a seguinte estrutura.

```text
ForgeDocs/
├── app/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── ui/
│       ├── dialogs/
│       ├── views/
│       └── widgets/
├── assets/
├── docs/
├── tests/
├── main.py
└── requirements.txt
```

Cada diretório possui responsabilidade única.

Evitar armazenar arquivos em diretórios cujo propósito não corresponda à sua função.

---

# 4. Organização dos Arquivos

Sempre que possível, um arquivo Python deve seguir a seguinte estrutura.

```text
Imports

↓

Constantes

↓

Enums

↓

Classes

↓

Funções auxiliares

↓

Execução (quando aplicável)
```

Essa organização deve permanecer consistente em toda a aplicação.

---

# 5. Indentação e Formatação

Toda implementação deve seguir as seguintes convenções.

## Identação

- utilizar quatro espaços;
- nunca utilizar TAB;
- manter alinhamento consistente.

---

## Comprimento de Linha

Recomenda-se limitar as linhas a aproximadamente 100 caracteres.

Quando necessário, realizar quebra lógica da expressão.

---

## Espaçamento

Utilizar linhas em branco para separar blocos conceitualmente distintos.

Evitar arquivos excessivamente compactos ou excessivamente espaçados.

---

## Imports

Os imports devem seguir a seguinte ordem.

```text
Bibliotecas padrão

↓

Bibliotecas de terceiros

↓

Módulos internos
```

Cada grupo deve ser separado por uma linha em branco.

---

# 6. Convenções de Nomeação

## Classes

Utilizar PascalCase.

Exemplo:

```python
PDFConverterView
```

---

## Widgets

Sempre terminar com:

```text
Widget
```

Exemplo:

```python
FileCardWidget
```

---

## Dialogs

Sempre terminar com:

```text
Dialog
```

Exemplo:

```python
SettingsDialog
```

---

## Services

Sempre terminar com:

```text
Service
```

Exemplo:

```python
ConversionService
```

---

## Exceptions

Sempre terminar com:

```text
Error
```

Exemplo:

```python
FileValidationError
```

---

## Variáveis

Utilizar snake_case.

Exemplo:

```python
selected_file
```

---

## Constantes

Utilizar UPPER_CASE.

Exemplo:

```python
DEFAULT_OUTPUT_PATH
```

---

## Métodos Privados

Sempre iniciar com "_".

Exemplo:

```python
_validate_input()
```

---

# 7. Estrutura das Classes

A organização recomendada é:

```text
Classe

↓

__init__()

↓

Propriedades

↓

Métodos Públicos

↓

Métodos Privados
```

Evitar alternar constantemente entre métodos públicos e privados.

---

# 8. Responsabilidade das Camadas

## Views

Responsáveis apenas pela interface.

Não devem conter regras de negócio.

---

## Services

Responsáveis pela lógica da aplicação.

Devem executar:

- processamento;
- conversões;
- manipulação de arquivos;
- integrações.

Não devem acessar diretamente componentes da interface.

---

## Widgets

Representam componentes reutilizáveis.

Devem possuir responsabilidade única.

---

## Dialogs

Representam interações temporárias.

Não devem conter lógica permanente da aplicação.

---

## Core

Contém infraestrutura compartilhada.

Exemplos:

- logging;
- configuração;
- exceções;
- utilidades.

---

# 9. Tratamento de Exceções

Toda exceção deve possuir tratamento adequado.

Sempre que possível:

- capturar exceções específicas;
- registrar informações relevantes;
- apresentar mensagens compreensíveis ao usuário.

Evitar:

```python
except:
```

Sempre capturar exceções explicitamente.

---

# 10. Logging

O ForgeDocs utiliza logging como principal mecanismo de rastreabilidade.

Utilizar:

```python
logger.debug()
```

para diagnóstico.

---

```python
logger.info()
```

para operações concluídas.

---

```python
logger.warning()
```

para situações inesperadas.

---

```python
logger.error()
```

para falhas recuperáveis.

---

```python
logger.exception()
```

para exceções.

Jamais utilizar print() para depuração permanente.

---

# 11. Threads

Toda operação potencialmente demorada deve ser executada em segundo plano.

Exemplos:

- OCR;
- compressão;
- conversão;
- leitura de documentos;
- exportações.

A interface nunca deve bloquear durante essas operações.

---

# 12. Comunicação entre UI e Services

A interface deve solicitar operações aos Services.

Os Services retornam resultados.

Os Services nunca atualizam diretamente componentes gráficos.

Essa separação reduz acoplamento e facilita testes.

---

# 13. Reutilização

Antes de implementar uma solução, verificar:

- existe um Service semelhante?
- existe um Widget semelhante?
- existe uma função utilitária equivalente?

Sempre priorizar reutilização.

---

# 14. Configurações

Configurações persistentes devem permanecer centralizadas.

Evitar valores fixos distribuídos pelo código.

Toda configuração compartilhada deve possuir origem única.

---

# 15. Internacionalização

Sempre que possível, evitar textos diretamente espalhados pelo código.

Preparar a aplicação para futura localização.

---

# 16. Testabilidade

Toda funcionalidade deve ser implementada considerando futuras rotinas de teste.

Evitar dependências desnecessárias entre módulos.

Quanto menor o acoplamento, maior a facilidade de validação.

---

# 17. Checklist de Desenvolvimento

Antes de concluir uma implementação, verificar:

- [ ] Responsabilidade única.
- [ ] Reutilização de componentes.
- [ ] Logging adequado.
- [ ] Tratamento de exceções.
- [ ] Nomenclatura consistente.
- [ ] Código legível.
- [ ] Nenhuma regra de negócio na View.
- [ ] Nenhum valor mágico no código.
- [ ] Comentários apenas quando realmente necessários.
- [ ] Compatibilidade com o Design System e UI Guidelines.

---

# 18. Processo de Revisão

Estas diretrizes devem evoluir juntamente com o ForgeDocs.

Sempre que um novo padrão de implementação for adotado, deve-se avaliar sua incorporação neste documento.

O objetivo é preservar consistência técnica ao longo de toda a evolução da aplicação.

---

# Considerações Finais

As Engineering Guidelines representam a referência oficial para implementação de funcionalidades no ForgeDocs.

Seu propósito é garantir que toda nova contribuição mantenha os mesmos padrões de organização, qualidade e manutenibilidade estabelecidos para o projeto.

A qualidade da aplicação depende não apenas das funcionalidades implementadas, mas também da consistência com que elas são desenvolvidas.