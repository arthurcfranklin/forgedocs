# Padrões de Desenvolvimento do ForgeDocs

## 1. Objetivo

Este documento define os padrões de desenvolvimento adotados no ForgeDocs.

O objetivo é manter o código:

- consistente;
- legível;
- previsível;
- modular;
- testável;
- fácil de manter.

Todos os novos módulos, componentes, serviços e testes deverão seguir estas diretrizes.

---

## 2. Referências principais

O projeto seguirá, sempre que aplicável:

- PEP 8 para estilo de código Python;
- PEP 257 para docstrings;
- PEP 484 para type hints;
- Conventional Commits para mensagens de commit;
- princípios de Clean Code;
- separação de responsabilidades;
- baixo acoplamento entre módulos.

Essas referências poderão ser adaptadas às necessidades específicas do projeto.

---

## 3. Versão do Python

Versão principal:

```text
Python 3.13
```

O código deverá aproveitar recursos modernos da linguagem, sem comprometer clareza ou compatibilidade com o empacotamento para Windows.

---

## 4. Codificação dos arquivos

Todos os arquivos de código e documentação deverão utilizar:

```text
UTF-8
```

Isso garante compatibilidade adequada com caracteres acentuados e documentação em português.

---

## 5. Idioma do projeto

### Código-fonte

Os nomes técnicos deverão ser escritos em inglês.

Exemplos:

```python
source_path
output_path
convert_document
file_validator
application_config
```

### Documentação
A documentação principal do repositório será escrita em português.

### Interface
Os textos exibidos ao usuário deverão ser escritos em português, com possibilidade de internacionalização futura.

### Comentários e docstrings
Podem ser escritos em português, desde que sejam claros, objetivos e consistentes.

---

## 6. Convenções de nomenclatura

## 6.1 Arquivos e módulos

Utilizar `snake_case`.

Exemplos:

```text
application.py
logging_config.py
file_selector.py
pdf_organization_page.py
```

Evitar:

```text
Application.py
loggingConfig.py
pdf-organization.py
```

---

## 6.2 Variáveis

Utilizar `snake_case`.

```python
source_file = "document.docx"
output_directory = "exports"
conversion_result = None
```

Os nomes devem indicar claramente a finalidade da variável.

Evitar nomes genéricos como:

```python
data
item
value
temp
obj
```

Esses nomes só devem ser utilizados quando o contexto for evidente e limitado.

---

## 6.3 Funções e métodos

Utilizar `snake_case`.

```python
def validate_file_path() -> bool:
    ...


def convert_to_pdf() -> None:
    ...


def load_user_settings() -> dict[str, object]:
    ...
```

Os nomes devem começar preferencialmente com verbos.

Exemplos:

- `create`
- `load`
- `save`
- `validate`
- `convert`
- `remove`
- `update`
- `get`
- `set`
- `build`
- `show`
- `hide`

---

## 6.4 Classes

Utilizar `PascalCase`.

```python
class ForgeDocsApp:
    ...


class WordToPdfConverter:
    ...


class FileValidationError(Exception):
    ...
```

---

## 6.5 Constantes

Utilizar `UPPER_SNAKE_CASE`.

```python
APP_NAME = "ForgeDocs"
APP_VERSION = "0.1.0-alpha"
DEFAULT_WINDOW_WIDTH = 1280
DEFAULT_WINDOW_HEIGHT = 760
SUPPORTED_PDF_EXTENSIONS = {".pdf"}
```

---

## 6.6 Variáveis privadas

Utilizar um sublinhado inicial quando o atributo ou método for de uso interno.

```python
self._current_page = None
self._load_settings()
```

O uso de dois sublinhados deve ser evitado, salvo quando houver justificativa técnica clara.

---

## 7. Organização de imports

Os imports deverão ser organizados em três grupos:

1. biblioteca padrão;
2. bibliotecas externas;
3. módulos internos do projeto.

Exemplo:

```python
from pathlib import Path
from typing import Final

import customtkinter as ctk
from PIL import Image

from app.core.constants import APP_NAME
from app.services.conversion.word_to_pdf import WordToPdfConverter
```

Cada grupo deve ser separado por uma linha em branco.

### Regras adicionais

- evitar imports com `*`;
- remover imports não utilizados;
- preferir imports absolutos;
- evitar imports circulares;
- manter os imports no topo do arquivo, salvo necessidade técnica justificada.

Evitar:

```python
from app.core.constants import *
```

---

## 8. Type hints

O uso de type hints será obrigatório em:

- funções públicas;
- métodos públicos;
- serviços;
- validadores;
- interfaces entre camadas;
- retornos relevantes.

Exemplo:

```python
from pathlib import Path


def validate_source_file(source_path: Path) -> bool:
    return source_path.exists() and source_path.is_file()
```

Outro exemplo:

```python
def convert_document(
    source_path: Path,
    output_path: Path,
) -> Path:
    ...
```

Evitar deixar tipos ambíguos quando eles puderem ser definidos claramente.

---

## 9. Uso de `pathlib`

O projeto deverá utilizar preferencialmente `pathlib.Path` para manipulação de caminhos.

Recomendado:

```python
from pathlib import Path

source_path = Path("documents") / "arquivo.docx"
```

Evitar:

```python
source_path = "documents\\arquivo.docx"
```

Benefícios:

- melhor legibilidade;
- maior segurança;
- manipulação multiplataforma;
- integração com APIs modernas do Python.

---

## 10. Docstrings

Funções, classes e métodos públicos deverão possuir docstrings quando sua finalidade não for imediatamente óbvia.

Formato recomendado:

```python
def validate_file_extension(
    file_path: Path,
    allowed_extensions: set[str],
) -> bool:
    """Valida se a extensão de um arquivo pertence à lista permitida.

    Args:
        file_path: Caminho do arquivo que será validado.
        allowed_extensions: Extensões aceitas pela operação.

    Returns:
        True quando a extensão é permitida; caso contrário, False.
    """
```

As docstrings devem explicar:

- responsabilidade;
- parâmetros;
- retorno;
- exceções relevantes.

Evitar docstrings que apenas repitam o nome da função.

Exemplo inadequado:

```python
def load_config() -> None:
    """Carrega a configuração."""
```

---

## 11. Comentários

Comentários devem explicar o motivo de uma decisão, não apenas descrever o código.

Bom exemplo:

```python
# O diretório temporário é separado por operação para evitar colisões
# durante execuções simultâneas.
operation_temp_dir = temp_root / operation_id
```

Exemplo desnecessário:

```python
# Incrementa o contador
counter += 1
```

Comentários obsoletos devem ser removidos.

Código comentado não deve permanecer no repositório sem justificativa.

---

## 12. Funções e métodos

Funções devem possuir responsabilidade única.

Recomendações:

- evitar funções excessivamente longas;
- evitar muitos níveis de indentação;
- extrair validações para funções específicas;
- evitar múltiplos efeitos colaterais;
- manter retornos previsíveis;
- preferir parâmetros explícitos.

Exemplo:

```python
def convert_word_to_pdf(
    source_path: Path,
    output_path: Path,
) -> Path:
    validate_source_file(source_path)
    ensure_output_directory(output_path.parent)

    return _execute_word_conversion(source_path, output_path)
```

---

## 13. Classes

Classes deverão representar responsabilidades claras.

Uma classe não deve acumular:

- interface gráfica;
- processamento de documentos;
- validação;
- persistência;
- logs;
- configurações.

Exemplo de separação correta:

```text
ConversionPage
    ↓
WordToPdfService
    ↓
FileValidator
```

A classe `ConversionPage` não deve implementar diretamente a conversão.

---

## 14. Componentes de interface

Componentes visuais devem:

- possuir responsabilidade única;
- ser reutilizáveis;
- receber dependências por parâmetro quando necessário;
- não executar processamento pesado;
- não acessar diretamente arquivos sem uma camada intermediária;
- seguir as diretrizes de `ui-guidelines.md`.

Exemplo:

```python
class ToolCard(ctk.CTkFrame):
    def __init__(
        self,
        master: ctk.CTkBaseClass,
        title: str,
        description: str,
        command: callable,
    ) -> None:
        ...
```

---

## 15. Separação entre UI e serviços

A interface deverá apenas:

- capturar entradas;
- validar dados simples;
- chamar serviços;
- apresentar resultados;
- exibir feedback.

A camada de serviços deverá:

- executar regras de negócio;
- processar documentos;
- validar operações;
- lançar exceções específicas;
- retornar resultados estruturados.

Fluxo esperado:

```text
UI
↓
Serviço
↓
Core
```

Não permitido:

```text
Serviço
↓
UI
```

---

## 16. Tratamento de exceções

Nunca utilizar blocos `except` genéricos sem tratamento adequado.

Evitar:

```python
try:
    convert_document()
except:
    pass
```

Também evitar:

```python
try:
    convert_document()
except Exception:
    print("Erro")
```

Recomendado:

```python
try:
    result_path = conversion_service.convert(source_path, output_path)
except UnsupportedFormatError as error:
    logger.warning("Formato não suportado: %s", error)
    raise
except ConversionError as error:
    logger.error("Falha durante a conversão: %s", error)
    raise
```

Exceções inesperadas devem ser registradas com traceback.

---

## 17. Exceções customizadas

As exceções específicas deverão herdar de uma exceção-base do projeto.

Exemplo:

```python
class ForgeDocsError(Exception):
    """Exceção-base para erros controlados do ForgeDocs."""


class FileValidationError(ForgeDocsError):
    """Erro relacionado à validação de arquivos."""


class UnsupportedFormatError(ForgeDocsError):
    """Erro gerado quando um formato não é suportado."""


class ConversionError(ForgeDocsError):
    """Erro ocorrido durante uma conversão."""
```

Isso permite tratamento mais previsível entre as camadas.

---

## 18. Logging

O projeto deverá utilizar o módulo `logging`.

Evitar:

```python
print("Erro ao converter arquivo")
```

Recomendado:

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Conversão iniciada: %s", source_path)
logger.warning("Arquivo de saída já existe: %s", output_path)
logger.error("Falha na conversão: %s", error)
```

### Níveis recomendados

- `DEBUG`: informações detalhadas de diagnóstico;
- `INFO`: operações relevantes;
- `WARNING`: situações inesperadas, porém recuperáveis;
- `ERROR`: falhas controladas;
- `CRITICAL`: falhas que comprometem a aplicação.

Conteúdo confidencial de documentos não deve ser registrado.

---

## 19. Mensagens ao usuário

Mensagens apresentadas na interface devem ser:

- claras;
- curtas;
- orientadas à solução;
- livres de stack traces;
- livres de linguagem excessivamente técnica.

Exemplo adequado:

```text
Não foi possível converter o documento.

Verifique se o arquivo está aberto em outro programa e tente novamente.
```

Exemplo inadequado:

```text
COMError 0x800A175D em DispatchEx Word.Application
```

Detalhes técnicos deverão permanecer nos logs.

---

## 20. Validação de arquivos

Toda operação deverá validar, quando aplicável:

- existência;
- extensão;
- permissões;
- tamanho;
- integridade;
- caminho de saída;
- risco de sobrescrita;
- formato compatível.

As validações compartilhadas devem ficar em módulos reutilizáveis.

---

## 21. Arquivos temporários

Arquivos temporários deverão:

- utilizar diretório controlado;
- possuir nomes únicos;
- ser removidos ao final;
- ser removidos também em caso de falha;
- nunca substituir o arquivo original sem confirmação.

Quando necessário, utilizar `try/finally`.

```python
temporary_file = create_temporary_file()

try:
    process_file(temporary_file)
finally:
    remove_temporary_file(temporary_file)
```

---

## 22. Configurações

Configurações não devem ser espalhadas pelo código.

Valores compartilhados deverão ficar em:

```text
app/core/config.py
app/core/constants.py
```

Evitar valores mágicos:

```python
window.geometry("1280x760")
```

Preferir:

```python
window.geometry(f"{DEFAULT_WINDOW_WIDTH}x{DEFAULT_WINDOW_HEIGHT}")
```

---

## 23. Segurança

O código deverá seguir estas regras:

- não registrar senhas em logs;
- não armazenar credenciais em texto puro;
- não remover proteção de arquivos sem autorização explícita;
- não sobrescrever arquivos silenciosamente;
- não enviar documentos pela internet;
- não executar comandos externos sem validação;
- não confiar em extensões sem validar o conteúdo quando necessário.

---

## 24. Testes

Os testes deverão utilizar `pytest`.

Estrutura planejada:

```text
tests/
├── unit/
├── integration/
└── fixtures/
```

### Convenções

Arquivos:

```text
test_file_validator.py
test_word_to_pdf.py
test_paths.py
```

Funções:

```python
def test_should_accept_existing_pdf_file() -> None:
    ...


def test_should_reject_unsupported_extension() -> None:
    ...
```

Os nomes devem indicar:

- cenário;
- comportamento esperado.

---

## 25. Testabilidade

Serviços deverão ser projetados para permitir testes isolados.

Evitar:

- dependências globais;
- caminhos fixos;
- chamadas diretas à interface;
- acesso ao sistema operacional em todos os métodos;
- criação interna rígida de dependências.

Preferir:

- parâmetros explícitos;
- funções puras;
- classes pequenas;
- injeção de dependências quando útil;
- interfaces claras.

---

## 26. Formatação automática

Ferramentas planejadas:

```text
Ruff
Black
```

Responsabilidades:

- `Ruff`: análise estática, imports e problemas comuns;
- `Black`: formatação consistente do código.

Essas ferramentas serão adicionadas ao projeto em uma etapa posterior.

---

## 27. Qualidade estática

Ferramenta planejada:

```text
mypy
```

O `mypy` poderá ser utilizado futuramente para validar os type hints e reduzir erros de tipagem.

A adoção poderá ocorrer de forma gradual.

---

## 28. Dependências

Novas dependências deverão ser adicionadas apenas quando houver necessidade concreta.

Antes de incluir uma biblioteca, avaliar:

- manutenção;
- compatibilidade com Python 3.13;
- compatibilidade com Windows;
- licença;
- tamanho;
- segurança;
- impacto no executável;
- necessidade real.

Após instalar uma dependência:

```powershell
pip freeze > requirements.txt
```

No futuro, o projeto poderá separar dependências de produção e desenvolvimento.

---

## 29. Commits

O projeto utiliza Conventional Commits.

Formatos principais:

```text
feat: nova funcionalidade
fix: correção de erro
docs: documentação
refactor: reorganização sem alteração funcional
test: criação ou alteração de testes
chore: configuração ou manutenção
style: alteração exclusivamente visual ou de formatação
perf: melhoria de desempenho
build: empacotamento ou build
ci: integração contínua
```

Exemplos:

```text
feat: add sidebar navigation
fix: handle invalid PDF path
docs: update project roadmap
refactor: separate conversion service
test: add file validation tests
chore: configure Ruff
```

### Regras

- escrever em inglês;
- utilizar letras minúsculas;
- usar modo imperativo;
- ser claro e específico;
- evitar mensagens genéricas.

Evitar:

```text
update
changes
fix
test
ajustes
alterações
```

---

## 30. Escopo dos commits

Cada commit deve representar uma alteração lógica.

Não misturar, no mesmo commit:

- nova funcionalidade;
- refatoração extensa;
- alteração de documentação não relacionada;
- correção independente;
- mudança visual sem relação com o código.

Commits pequenos facilitam:

- revisão;
- rastreabilidade;
- reversão;
- manutenção do histórico.

---

## 31. Branches

Enquanto o projeto estiver em desenvolvimento individual inicial, a branch principal será:

```text
main
```

Conforme o projeto crescer, poderão ser utilizadas branches como:

```text
feat/sidebar-navigation
feat/word-to-pdf
fix/output-file-overwrite
docs/update-roadmap
```

O uso de branches deverá ser adotado quando trouxer benefício real ao fluxo.

---

## 32. Pull requests

Pull requests poderão ser utilizados futuramente para:

- revisar alterações;
- documentar decisões;
- executar automações;
- validar testes;
- organizar contribuições externas.

Durante a fase inicial e individual, commits diretos na `main` são aceitáveis, desde que revisados antes do push.

---

## 33. Revisão antes do commit

Antes de cada commit:

```powershell
git status
git diff
```

Quando houver arquivos preparados:

```powershell
git diff --staged
```

Também deverão ser verificados:

- funcionamento da aplicação;
- imports;
- erros de sintaxe;
- arquivos acidentalmente adicionados;
- dados sensíveis;
- atualização do `requirements.txt`, quando necessário.

---

## 34. Versionamento

O ForgeDocs utilizará Versionamento Semântico.

Formato:

```text
MAJOR.MINOR.PATCH
```

Exemplo:

```text
1.4.2
```

Durante a fase inicial:

```text
0.1.0-alpha
0.2.0-alpha
0.9.0-beta
1.0.0
```

Interpretação:

- `MAJOR`: alterações incompatíveis;
- `MINOR`: novas funcionalidades compatíveis;
- `PATCH`: correções compatíveis.

---

## 35. Definição de pronto

Uma tarefa será considerada concluída quando:

- o código estiver implementado;
- o comportamento esperado estiver validado;
- erros relevantes estiverem tratados;
- logs necessários estiverem adicionados;
- testes aplicáveis estiverem funcionando;
- documentação relacionada estiver atualizada;
- o código seguir os padrões deste documento;
- o commit estiver claro e corretamente classificado.

---

## 36. Princípios gerais

Durante o desenvolvimento, priorizar:

1. clareza antes de abstrações;
2. simplicidade antes de complexidade;
3. composição antes de duplicação;
4. validação antes de processamento;
5. mensagens claras antes de erros técnicos na interface;
6. código testável antes de soluções rígidas;
7. documentação proporcional à complexidade;
8. evolução incremental;
9. privacidade por padrão;
10. preservação do arquivo original.

---

## 37. Revisões do documento

Este documento deverá ser atualizado quando houver mudanças em:

- ferramentas;
- convenções;
- arquitetura;
- fluxo Git;
- estratégia de testes;
- versionamento;
- padrões de qualidade.

As alterações deverão ser registradas em commits de documentação.