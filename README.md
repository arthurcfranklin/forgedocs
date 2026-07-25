# 📄 ForgeDocs

![Status](https://img.shields.io/badge/Status-Alpha-orange)
![Version](https://img.shields.io/badge/Version-v0.2.0--alpha-blue)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Suíte desktop moderna para Windows voltada ao processamento e gerenciamento de documentos, desenvolvida com foco em privacidade, produtividade e processamento 100% local.

---

## ✨ Principais Características

- 🔒 **Privacidade por padrão** — processamento realizado totalmente offline.
- ⚡ **Arquitetura escalável** — componentes independentes e reutilizáveis.
- 🎨 **Design consistente** — interface moderna baseada em Design System dedicado.
- 📄 **Suíte integrada** — preparada para centralizar ferramentas de documentos.
- 📚 **Desenvolvimento estruturado** — documentação técnica e roadmap versionados.

---

# 📸 Preview da Interface

![ForgeDocs](assets/images/forgedocs-main.png)

> Interface principal do ForgeDocs (v0.2.0-alpha), apresentando a arquitetura visual da aplicação, catálogo de ferramentas e os componentes que servirão de base para as próximas funcionalidades.

---

# 📊 Status

🟢 Em desenvolvimento ativo.

**Versão atual:** `v0.2.0-alpha`

O ForgeDocs já possui sua infraestrutura principal concluída, incluindo arquitetura modular, Design System, interface desktop, sistema de ícones, documentação técnica e organização completa do projeto. As próximas versões serão focadas na implementação das funcionalidades de processamento e gerenciamento de documentos.

---

# 📖 Sobre o Projeto

O ForgeDocs é uma suíte desktop para Windows desenvolvida em Python com o objetivo de centralizar ferramentas para conversão, organização, otimização e proteção de documentos em uma única aplicação.

O projeto segue a filosofia **Local First**, realizando todo o processamento diretamente na máquina do usuário. Dessa forma, elimina a dependência de serviços em nuvem, preserva a privacidade dos dados e oferece maior desempenho durante as operações.

Além do desenvolvimento da aplicação, o projeto é estruturado com foco em arquitetura de software, documentação técnica, padronização visual, escalabilidade e boas práticas de engenharia de software.

---

# 🎯 Objetivos

- Centralizar ferramentas de processamento de documentos
- Eliminar a dependência de serviços online
- Garantir processamento totalmente local
- Construir uma arquitetura modular e escalável
- Desenvolver uma interface moderna e consistente
- Aplicar boas práticas de engenharia de software

---

# ✨ Funcionalidades

## 📄 Conversão de documentos

- Word → PDF
- PDF → Word
- Excel → PDF
- PDF → Excel
- PowerPoint → PDF
- PDF → PowerPoint
- Imagens → PDF
- PDF → Imagens
- Markdown → PDF
- HTML → PDF

## 📑 Organização de PDFs

- Mesclar PDFs
- Dividir PDFs
- Reordenar páginas
- Rotacionar páginas
- Extrair páginas
- Remover páginas

## ✏️ Edição

- Marca d'água
- Numeração de páginas
- Cabeçalhos e rodapés
- Metadados
- Edição básica de PDFs

## ⚡ Otimização

- Compressão de PDFs
- OCR
- Conversão para PDF/A
- Reparo de arquivos

## 🔒 Segurança

- Proteção por senha
- Remoção de senha
- Redação de conteúdo
- Comparação de documentos
- Assinatura digital

---

# 🏗 Arquitetura

```text
ForgeDocs
│
├── app
│   ├── core
│   ├── services
│   └── ui
│       ├── components
│       └── views
│
├── assets
├── docs
├── tests
│
├── main.py
└── requirements.txt
```

A arquitetura foi projetada para favorecer modularidade, reutilização de componentes, manutenção simplificada e expansão contínua da aplicação.

---

# 🛠 Tecnologias Utilizadas

## Linguagem

- Python 3.13

## Interface

- CustomTkinter
- Pillow

## Processamento de documentos

- PyMuPDF
- pypdf
- python-docx
- openpyxl
- python-pptx

## Versionamento

- Git
- GitHub

---

# 📚 Documentação

Toda a documentação técnica do projeto encontra-se disponível em:

```text
docs/
```

## Documentos Disponíveis

### Arquitetura

- Architecture Documentation
- Design System
- UI Guidelines

### Engenharia

- Coding Standards
- Engineering Guidelines

### Planejamento

- Product Roadmap

---

# 🚀 Releases

| Versão | Descrição |
|---------|-----------|
| v0.1.0-alpha | Project Foundation |
| v0.2.0-alpha | Application Shell & Design System |

---

# 🗺 Roadmap

## ✅ Concluído

- Arquitetura modular
- Interface desktop
- Design System
- Sistema de ícones
- Estrutura de configuração
- Sistema de logging
- Documentação técnica
- Estrutura de releases

## 🚧 Próxima versão — v0.3.0-alpha

### Document Conversion Engine

- Word → PDF
- PDF → Word
- Excel → PDF
- PowerPoint → PDF
- Imagens → PDF
- PDF → Imagens

## 🔮 Futuras versões

### Organização de PDFs

- Mesclagem
- Divisão
- Reordenação
- Extração de páginas

### Ferramentas avançadas

- OCR
- Compressão
- Segurança
- Plugins

---

# 📄 Licença

Distribuído sob a licença **MIT**.

Consulte o arquivo **LICENSE** para mais informações.
