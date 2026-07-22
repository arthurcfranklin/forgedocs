# Arquitetura do ForgeDocs

## 1. Visão geral

O **ForgeDocs** é uma aplicação desktop para Windows destinada ao processamento, organização, conversão e proteção de documentos.

A aplicação será desenvolvida em Python, utilizando CustomTkinter para a interface gráfica e bibliotecas especializadas para manipulação de PDFs, documentos Office e imagens.

O projeto adota uma arquitetura modular, com separação clara entre:

- interface gráfica;
- regras de negócio;
- serviços de processamento;
- configurações;
- utilitários;
- testes.

Essa divisão tem como objetivo facilitar a manutenção, os testes, a evolução das funcionalidades e o reaproveitamento de componentes.

---

## 2. Princípios arquiteturais

A arquitetura do ForgeDocs será orientada pelos seguintes princípios:

### 2.1 Separação de responsabilidades

Cada módulo deve possuir uma responsabilidade principal bem definida.

A interface gráfica não deve executar diretamente operações de conversão, organização ou processamento de arquivos.

### 2.2 Processamento local

Todas as operações deverão ser realizadas localmente no computador do usuário.

O ForgeDocs não dependerá de:

- APIs externas;
- serviços em nuvem;
- envio de arquivos para servidores;
- conexão permanente com a internet.

### 2.3 Modularidade

Cada grupo de funcionalidades será desenvolvido em módulos independentes.

Exemplos:

- conversão;
- organização de PDFs;
- otimização;
- OCR;
- segurança.

### 2.4 Reutilização

Componentes visuais, validadores, manipuladores de arquivos e serviços compartilhados devem ser reutilizáveis.

### 2.5 Escalabilidade

A estrutura deve permitir a inclusão de novas ferramentas sem exigir alterações extensas nos módulos existentes.

### 2.6 Tratamento de erros

Erros internos não devem encerrar a aplicação inesperadamente.

As exceções devem ser:

- capturadas;
- registradas em log;
- apresentadas ao usuário de forma compreensível;
- tratadas na camada adequada.

---

## 3. Estrutura do projeto

A estrutura inicial do ForgeDocs é organizada da seguinte forma:

```text
forgedocs/
│
├── app/
│   ├── core/
│   ├── services/
│   │   ├── conversion/
│   │   ├── optimization/
│   │   ├── organization/
│   │   └── security/
│   │
│   └── ui/
│       ├── components/
│       └── pages/
│
├── assets/
│   ├── icons/
│   └── images/
│
├── docs/
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

Essa estrutura poderá evoluir conforme novas necessidades forem identificadas.

---

## 4. Camadas da aplicação

## 4.1 Camada de entrada

Arquivo principal:

```text
main.py
```

Responsabilidades:

- iniciar a aplicação;
- configurar o ambiente inicial;
- instanciar a classe principal;
- iniciar o loop da interface.

O arquivo `main.py` não deve conter:

- regras de negócio;
- lógica de conversão;
- manipulação direta de documentos;
- componentes visuais complexos.

Exemplo esperado:

```python
from app.ui.application import ForgeDocsApp


def main() -> None:
    app = ForgeDocsApp()
    app.mainloop()


if __name__ == "__main__":
    main()
```

---

## 4.2 Camada Core

Diretório:

```text
app/core/
```

Responsável pelos elementos fundamentais e compartilhados da aplicação.

Estrutura planejada:

```text
app/core/
├── config.py
├── constants.py
├── exceptions.py
├── logging_config.py
└── paths.py
```

### `config.py`

Responsável por configurações gerais da aplicação.

Exemplos:

- tema padrão;
- dimensões da janela;
- preferências do usuário;
- idioma;
- comportamento inicial.

### `constants.py`

Responsável por valores constantes.

Exemplos:

- nome da aplicação;
- número da versão;
- nomes de páginas;
- formatos suportados;
- mensagens padronizadas.

### `exceptions.py`

Responsável pelas exceções específicas do ForgeDocs.

Exemplos:

- arquivo inválido;
- formato não suportado;
- falha de conversão;
- arquivo protegido;
- dependência indisponível.

### `logging_config.py`

Responsável pela configuração do sistema de logs.

Os logs deverão registrar:

- inicialização da aplicação;
- operações executadas;
- erros;
- falhas de processamento;
- informações relevantes para diagnóstico.

### `paths.py`

Responsável por centralizar caminhos utilizados pela aplicação.

Exemplos:

- diretório de assets;
- diretório de logs;
- diretório temporário;
- arquivos de configuração;
- recursos empacotados.

---

## 4.3 Camada de serviços

Diretório:

```text
app/services/
```

Responsável pelas regras de negócio e operações de processamento.

A camada de serviços não deve depender diretamente de componentes da interface gráfica.

---

### 4.3.1 Conversão

Diretório:

```text
app/services/conversion/
```

Responsabilidades planejadas:

- Word para PDF;
- Excel para PDF;
- PowerPoint para PDF;
- imagens para PDF;
- Markdown para PDF;
- extração de conteúdo;
- conversões entre formatos suportados.

Cada conversor deverá possuir uma interface clara e isolada.

Exemplo:

```python
class WordToPdfConverter:
    def convert(self, source_path: str, output_path: str) -> None:
        ...
```

---

### 4.3.2 Organização

Diretório:

```text
app/services/organization/
```

Responsabilidades planejadas:

- mesclar PDFs;
- dividir PDFs;
- extrair páginas;
- remover páginas;
- reordenar páginas;
- rotacionar páginas.

---

### 4.3.3 Otimização

Diretório:

```text
app/services/optimization/
```

Responsabilidades planejadas:

- compressão de PDFs;
- otimização de imagens;
- redução de tamanho;
- controle de qualidade;
- análise de arquivos.

---

### 4.3.4 Segurança

Diretório:

```text
app/services/security/
```

Responsabilidades planejadas:

- aplicação de senha;
- remoção autorizada de senha;
- criação de marca d'água;
- assinatura digital;
- validação de arquivos protegidos.

---

## 4.4 Camada de interface

Diretório:

```text
app/ui/
```

Responsável pela interação entre o usuário e os serviços da aplicação.

Estrutura planejada:

```text
app/ui/
├── application.py
├── theme.py
├── components/
└── pages/
```

---

### `application.py`

Responsável pela janela principal do ForgeDocs.

Deverá controlar:

- criação da janela;
- dimensões;
- navegação;
- carregamento das páginas;
- gerenciamento do layout principal;
- inicialização dos componentes globais.

---

### `theme.py`

Responsável pelos padrões visuais da aplicação.

Exemplos:

- cores;
- fontes;
- tamanhos;
- espaçamentos;
- bordas;
- estilos de componentes.

---

## 4.5 Componentes reutilizáveis

Diretório:

```text
app/ui/components/
```

Responsável por elementos visuais reutilizados em diferentes páginas.

Componentes planejados:

```text
app/ui/components/
├── sidebar.py
├── navigation_button.py
├── page_header.py
├── tool_card.py
├── file_selector.py
├── progress_panel.py
├── notification.py
└── status_bar.py
```

A criação de componentes reutilizáveis evita duplicação de código e mantém a identidade visual consistente.

---

## 4.6 Páginas

Diretório:

```text
app/ui/pages/
```

Cada página deve representar uma área funcional da aplicação.

Estrutura inicial planejada:

```text
app/ui/pages/
├── home_page.py
├── conversion_page.py
├── pdf_organization_page.py
├── optimization_page.py
├── ocr_page.py
├── security_page.py
└── settings_page.py
```

As páginas devem:

- montar a interface;
- coletar entradas do usuário;
- chamar os serviços adequados;
- apresentar resultados;
- exibir mensagens de erro ou sucesso.

As páginas não devem implementar diretamente as operações de processamento.

---

## 5. Fluxo de execução

O fluxo geral de uma operação será:

```text
Usuário
   ↓
Interface gráfica
   ↓
Validação de entrada
   ↓
Serviço correspondente
   ↓
Processamento local
   ↓
Resultado ou exceção
   ↓
Interface gráfica
   ↓
Mensagem ao usuário
```

Exemplo de conversão:

```text
Usuário seleciona um arquivo Word
   ↓
A interface valida o arquivo
   ↓
O serviço WordToPdfConverter é chamado
   ↓
O documento é convertido localmente
   ↓
O arquivo PDF é salvo
   ↓
A interface informa o resultado
```

---

## 6. Dependências entre camadas

A direção das dependências deverá seguir este fluxo:

```text
UI → Services → Core
```

A camada Core pode ser utilizada por todas as demais.

A camada de serviços não deve depender da camada de interface.

Direção permitida:

```text
app/ui/ → app/services/
app/ui/ → app/core/
app/services/ → app/core/
```

Direção não permitida:

```text
app/services/ → app/ui/
app/core/ → app/ui/
```

Essa regra reduz o acoplamento e facilita testes automatizados.

---

## 7. Tratamento de arquivos

As operações com arquivos devem seguir as seguintes diretrizes:

- validar a existência do arquivo;
- validar a extensão;
- verificar permissões de leitura e escrita;
- evitar sobrescrita sem confirmação;
- utilizar caminhos absolutos quando necessário;
- remover arquivos temporários;
- preservar o arquivo original;
- registrar erros em log.

Por padrão, operações destrutivas não devem alterar diretamente o arquivo de origem.

---

## 8. Operações demoradas

Conversões, OCR e compressões podem exigir processamento significativo.

Essas operações não devem bloquear a interface principal.

No futuro, deverão utilizar:

- threads;
- filas de processamento;
- tarefas em segundo plano;
- indicadores de progresso;
- opção de cancelamento, quando tecnicamente possível.

A interface não deverá aparentar travamento durante operações demoradas.

---

## 9. Logs

O ForgeDocs deverá registrar eventos em arquivos locais.

Estrutura prevista:

```text
logs/
└── forgedocs.log
```

Informações que podem ser registradas:

- data e horário;
- nível do evento;
- módulo;
- operação;
- resultado;
- mensagem de erro;
- traceback em falhas inesperadas.

Dados sensíveis ou conteúdo dos documentos não devem ser registrados.

---

## 10. Configurações do usuário

Configurações futuras poderão ser armazenadas localmente.

Exemplos:

- tema;
- diretório de saída padrão;
- comportamento de sobrescrita;
- qualidade de compressão;
- preferências de interface;
- última página acessada.

Essas informações poderão ser armazenadas em arquivo JSON ou formato semelhante.

---

## 11. Testes

Diretório:

```text
tests/
```

Os testes deverão priorizar:

- serviços;
- validadores;
- utilitários;
- manipulação de caminhos;
- tratamento de exceções;
- operações com arquivos.

Estrutura planejada:

```text
tests/
├── unit/
├── integration/
└── fixtures/
```

A interface gráfica poderá receber testes específicos posteriormente.

---

## 12. Empacotamento

O ForgeDocs será distribuído como aplicação executável para Windows.

Ferramenta planejada:

```text
PyInstaller
```

O empacotamento deverá considerar:

- assets;
- ícones;
- bibliotecas nativas;
- caminhos relativos;
- dependências do sistema;
- arquivos temporários;
- logs;
- configuração do executável.

O código deve evitar dependências rígidas do diretório de desenvolvimento.

---

## 13. Segurança e privacidade

A arquitetura deve preservar o princípio de processamento local.

Diretrizes:

- nenhum arquivo será enviado automaticamente para a internet;
- nenhum conteúdo será coletado sem autorização;
- nenhum documento será armazenado externamente;
- arquivos temporários deverão ser removidos;
- logs não deverão armazenar conteúdo confidencial;
- credenciais e senhas não deverão ser registradas;
- operações sensíveis deverão exigir confirmação.

---

## 14. Evolução prevista

A arquitetura poderá evoluir para suportar:

- sistema de plugins;
- processamento em lote;
- histórico de operações;
- fila de tarefas;
- atualizações automáticas;
- internacionalização;
- interface multilíngue;
- assinatura digital avançada;
- templates de processamento;
- perfis de configuração;
- suporte a novos formatos.

As evoluções devem preservar a separação entre interface, serviços e núcleo da aplicação.

---

## 15. Decisões atuais

Até o momento, foram definidas as seguintes decisões:

- Python 3.13 como linguagem principal;
- CustomTkinter para interface;
- processamento 100% local;
- arquitetura modular;
- separação entre UI e regras de negócio;
- suporte inicial ao Windows;
- empacotamento futuro com PyInstaller;
- licença MIT;
- documentação em português;
- commits seguindo Conventional Commits.

---

## 16. Status do documento

Este documento representa a arquitetura inicial do ForgeDocs.

Ele deverá ser revisado sempre que houver mudanças relevantes na estrutura, nas responsabilidades dos módulos ou no fluxo da aplicação.