# ForgeDocs

Suíte local para processamento de documentos no Windows, desenvolvida em Python.

[English](README.md)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows-0078D4?style=flat)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-2EA44F?style=flat)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-1F6FEB?style=flat)
![Privacidade](https://img.shields.io/badge/Privacidade-Local%20First-238636?style=flat)

## Visão Geral

O ForgeDocs é uma suíte desktop desenvolvida para centralizar tarefas comuns de processamento de documentos em uma única aplicação para Windows.

O projeto é voltado à conversão, organização, edição, otimização e proteção de documentos, mantendo o processamento local no dispositivo do usuário. Os arquivos permanecem sob controle do usuário durante todo o fluxo de trabalho, sem depender de serviços externos em nuvem para processamento.

O ForgeDocs utiliza uma arquitetura modular projetada para permitir evolução contínua, facilitar a manutenção e possibilitar a inclusão de novas ferramentas ao longo do desenvolvimento.

## Funcionalidades

O ForgeDocs está sendo desenvolvido em torno de cinco áreas principais:

- **Converter** — Transformar documentos entre formatos compatíveis.
- **Organizar** — Unir, dividir, reordenar e extrair conteúdo de documentos.
- **Editar** — Aplicar ajustes, anotações e outras modificações suportadas.
- **Otimizar** — Comprimir, reparar e preparar arquivos para uso mais eficiente.
- **Proteger** — Adicionar controles de segurança e privacidade aos documentos compatíveis.

Todas as ferramentas seguem um fluxo de trabalho consistente:

**Selecionar → Configurar → Processar → Revisar → Exportar**

O processamento é realizado localmente, sem necessidade de envio dos arquivos para serviços externos.

## Captura de Tela

<p align="center">
  <img src="assets/images/app/forgedocs-main.png" alt="Interface principal do ForgeDocs" width="900">
</p>

## Tecnologias

| Área | Tecnologias |
| --- | --- |
| Base | Python 3.13 |
| Interface | CustomTkinter, Pillow |
| PDF e Documentos | PyMuPDF, pypdf, python-docx |
| Planilhas e Apresentações | openpyxl, python-pptx |
| Outros Formatos | Markdown |
| Distribuição | PyInstaller, PyWin32 |
| Plataforma | Windows |

A stack é baseada em bibliotecas consolidadas do ecossistema Python, com cada componente responsável por uma parte específica do fluxo de processamento de documentos.

## Arquitetura

O ForgeDocs é organizado em responsabilidades bem definidas para reduzir o acoplamento e facilitar a manutenção e evolução independente dos componentes.

As principais áreas arquiteturais são:

- **Interface** — Interface desktop, navegação e feedback ao usuário.
- **Aplicação** — Orquestração dos fluxos e coordenação dos serviços.
- **Núcleo** — Configurações compartilhadas, caminhos, logs e exceções.
- **Serviços** — Conversão, organização, edição e otimização de documentos.
- **Utilitários** — Validação de arquivos, operações auxiliares e integrações locais.
- **Motores de Documentos** — Processamento específico para PDF, Word, Excel, PowerPoint, imagens e Markdown.

Essa separação permite adicionar novas ferramentas e integrações sem exigir alterações significativas na estrutura existente da aplicação.

## Estrutura do Projeto

O repositório é organizado nas seguintes áreas principais:

```text
ForgeDocs/
├── app/
│   ├── core/
│   ├── services/
│   └── ui/
├── assets/
├── docs/
├── tests/
├── config/
├── main.py
├── requirements.txt
└── README.md
```

- `app/` contém o código-fonte da aplicação e seus principais módulos.
- `assets/` armazena os recursos estáticos utilizados pelo projeto.
- `docs/` contém a documentação técnica e do projeto.
- `tests/` contém testes automatizados e validações dos serviços.
- `config/` contém as configurações do projeto.
- `main.py` fornece o ponto de entrada da aplicação.
- `requirements.txt` define as dependências Python.

## Primeiros Passos

### Requisitos

- Windows
- Python 3.13
- Dependências definidas em `requirements.txt`

### Instalação

Clone o repositório:

```bash
git clone https://github.com/arthurcfranklin/forgedocs.git
cd forgedocs
```

Crie e ative um ambiente virtual e, em seguida, instale as dependências do projeto.

> A configuração exata do ambiente de desenvolvimento e os comandos de execução devem seguir a configuração atual do projeto.

### Execução

O ForgeDocs encontra-se atualmente em desenvolvimento ativo.

As instruções de desenvolvimento e execução serão documentadas nesta seção conforme o fluxo da aplicação for estabilizado.

## Documentação

A documentação técnica é mantida no diretório `docs/` e evolui juntamente com a aplicação.

As áreas documentadas atualmente incluem:

- **Arquitetura** — Organização do sistema, componentes e responsabilidades.
- **Padrões de Desenvolvimento** — Convenções de código e práticas de desenvolvimento.
- **Diretrizes de Interface** — Padrões visuais e de interação da aplicação desktop.
- **Roadmap** — Planejamento técnico e próximos marcos de desenvolvimento.
- **Branding** — Identidade e diretrizes visuais do projeto.

## Roadmap

- [x] Foundation
- [x] Core Services
- [ ] Desktop GUI
- [ ] Document Tools
- [ ] Optimization
- [ ] Security & v1.0

O desenvolvimento segue uma abordagem incremental, priorizando a consolidação de uma base estável antes da expansão do conjunto de funcionalidades.

## Princípios do Projeto

- **Local-first** — O processamento dos documentos permanece no dispositivo do usuário.
- **Arquitetura modular** — Os componentes possuem responsabilidades claras e independentes.
- **Experiência consistente** — As ferramentas seguem padrões compartilhados de interface e fluxo de trabalho.
- **Manutenibilidade** — O projeto prioriza uma estrutura clara e tecnologias consolidadas.
- **Desenvolvimento incremental** — Novas funcionalidades são incorporadas conforme a plataforma amadurece.
- **Código aberto** — O desenvolvimento permanece transparente e documentado.

## Licença

O ForgeDocs é distribuído sob a [Licença MIT](LICENSE).

---

Desenvolvido por **Arthur Franklin**.
