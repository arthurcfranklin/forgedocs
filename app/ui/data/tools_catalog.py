"""Catálogo de ferramentas disponíveis no ForgeDocs."""

from __future__ import annotations
from typing import TypedDict


class ToolDefinition(TypedDict):
    """Estrutura de dados de uma ferramenta do ForgeDocs."""

    title: str
    description: str
    category: str
    action_name: str


TOOLS: tuple[ToolDefinition, ...] = (
    {
        "title": "Word → PDF",
        "description": (
            "Converta documentos Word para PDF "
            "preservando a formatação."
        ),
        "category": "Conversão",
        "action_name": "word_to_pdf",
    },
    {
        "title": "PDF → Word",
        "description": (
            "Converta arquivos PDF em documentos "
            "Word editáveis."
        ),
        "category": "Conversão",
        "action_name": "pdf_to_word",
    },
    {
        "title": "JPEG → PDF",
        "description": (
            "Converta imagens JPEG em documentos PDF."
        ),
        "category": "Imagens",
        "action_name": "jpeg_to_pdf",
    },
    {
        "title": "PDF → JPEG",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens JPEG."
        ),
        "category": "Imagens",
        "action_name": "pdf_to_jpeg",
    },
    {
        "title": "PowerPoint → PDF",
        "description": (
            "Converta apresentações PowerPoint para PDF "
            "preservando o layout."
        ),
        "category": "Conversão",
        "action_name": "powerpoint_to_pdf",
    },
    {
        "title": "PDF → PowerPoint",
        "description": (
            "Converta arquivos PDF em apresentações "
            "PowerPoint editáveis."
        ),
        "category": "Conversão",
        "action_name": "pdf_to_powerpoint",
    },
    {
        "title": "Excel → PDF",
        "description": (
            "Converta planilhas Excel para PDF "
            "preservando a estrutura."
        ),
        "category": "Conversão",
        "action_name": "excel_to_pdf",
    },
    {
        "title": "PDF → Excel",
        "description": (
            "Extraia tabelas de arquivos PDF "
            "para planilhas Excel."
        ),
        "category": "Conversão",
        "action_name": "pdf_to_excel",
    },
    {
        "title": "Mesclar PDF",
        "description": (
            "Combine vários arquivos PDF "
            "em um único documento."
        ),
        "category": "Ferramentas PDF",
        "action_name": "merge_pdf",
    },
    {
        "title": "Dividir PDF",
        "description": (
            "Separe páginas de um PDF "
            "em novos arquivos."
        ),
        "category": "Ferramentas PDF",
        "action_name": "split_pdf",
    },
    {
        "title": "Comprimir PDF",
        "description": (
            "Reduza o tamanho de arquivos PDF "
            "mantendo a qualidade."
        ),
        "category": "Ferramentas PDF",
        "action_name": "compress_pdf",
    },
    {
        "title": "Editar PDF",
        "description": (
            "Edite textos, imagens e páginas "
            "de documentos PDF."
        ),
        "category": "Ferramentas PDF",
        "action_name": "edit_pdf",
    },
    {
        "title": "Proteger PDF",
        "description": (
            "Adicione senha e restrições "
            "de acesso ao PDF."
        ),
        "category": "Segurança",
        "action_name": "protect_pdf",
    },
    {
        "title": "Desbloquear PDF",
        "description": (
            "Remova a proteção por senha "
            "de PDFs autorizados."
        ),
        "category": "Segurança",
        "action_name": "unlock_pdf",
    },
    {
        "title": "Organizar PDF",
        "description": (
            "Reordene, gire ou remova "
            "páginas de um PDF."
        ),
        "category": "Ferramentas PDF",
        "action_name": "organize_pdf",
    },
    {
        "title": "Corromper PDF",
        "description": (
            "Gere uma cópia danificada "
            "para testes."
        ),
        "category": "Ferramentas PDF",
        "action_name": "corrupt_pdf",
    },
)