# ForgeDocs

Suíte desktop moderna para Windows voltada ao processamento e gerenciamento de documentos, com foco em privacidade, produtividade e execução 100% local.

> **Status:** Em desenvolvimento (v0.1.0-alpha)

---

## 📖 Sobre

O **ForgeDocs** é um projeto desenvolvido em Python com o objetivo de oferecer uma suíte completa para manipulação de documentos, reunindo diversas ferramentas em uma única aplicação desktop.

Todo o processamento é realizado localmente, sem dependência de serviços em nuvem ou APIs externas, garantindo maior privacidade, desempenho e controle sobre os arquivos do usuário.

O projeto também faz parte do meu portfólio profissional, sendo desenvolvido com foco em arquitetura de software, boas práticas, escalabilidade e experiência do usuário.

---

## ✨ Funcionalidades Planejadas

### 📄 Conversão de documentos

- Word → PDF
- Excel → PDF
- PowerPoint → PDF
- Imagens → PDF
- Markdown → PDF

### 📑 Organização de PDFs

- Mesclar PDFs
- Dividir PDFs
- Reordenar páginas
- Rotacionar páginas
- Remover páginas

### ⚡ Otimização

- Compressão de PDFs
- Otimização de imagens
- Redução de tamanho de arquivos

### 🔍 OCR

- Reconhecimento óptico de caracteres
- Pesquisa em documentos digitalizados

### 🔒 Segurança

- Proteção por senha
- Remoção de senha (quando autorizada)
- Marca d'água
- Assinatura digital

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular para facilitar manutenção, escalabilidade e evolução das funcionalidades.

```
ForgeDocs
│
├── app
│   ├── core
│   ├── services
│   │   ├── conversion
│   │   ├── optimization
│   │   ├── organization
│   │   └── security
│   └── ui
│       ├── components
│       └── pages
│
├── assets
│
├── docs
│
├── tests
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Tecnologias

### Linguagem

- Python 3.13

### Interface

- CustomTkinter

### Manipulação de documentos

- PyMuPDF
- python-docx
- openpyxl
- python-pptx

### Imagens

- Pillow

### Empacotamento

- PyInstaller

---

## 🗺️ Roadmap

### Sprint 0 — Fundação ✅

- [x] Estrutura do projeto
- [x] Git
- [x] GitHub
- [x] Ambiente virtual
- [x] README inicial
- [x] Licença MIT

### Sprint 1 — Interface

- [ ] Janela principal
- [ ] Sidebar
- [ ] Navegação
- [ ] Tema Dark
- [ ] Componentes reutilizáveis

### Sprint 2 — Conversão

- [ ] Word → PDF
- [ ] Excel → PDF
- [ ] PowerPoint → PDF

### Sprint 3 — PDFs

- [ ] Mesclar
- [ ] Dividir
- [ ] Organizar páginas

### Sprint 4 — Recursos avançados

- [ ] OCR
- [ ] Compressão
- [ ] Segurança

---

## 🎯 Objetivos

- Arquitetura modular
- Código limpo e documentado
- Interface moderna
- Processamento local
- Alto desempenho
- Fácil manutenção

---

## 📄 Licença

Distribuído sob a licença **MIT**.

Consulte o arquivo **LICENSE** para mais informações.