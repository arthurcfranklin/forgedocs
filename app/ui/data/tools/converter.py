"""Ferramentas da categoria Converter."""

from __future__ import annotations
from app.ui.data.tools.types import ToolDefinition

CONVERTER_TOOLS: tuple[ToolDefinition, ...] = (
        {
        "title": "Word → PDF",
        "description": (
            "Converta documentos Word para PDF "
            "preservando a formatação."
        ),
        "category": "Converter",
        "action_name": "word_to_pdf",
    },
    {
        "title": "PDF → Word",
        "description": (
            "Converta arquivos PDF em documentos "
            "Word editáveis."
        ),
        "category": "Converter",
        "action_name": "pdf_to_word",
    },
    {
        "title": "JPEG → PDF",
        "description": (
            "Converta imagens JPEG em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "jpeg_to_pdf",
    },
    {
        "title": "PDF → JPEG",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens JPEG."
        ),
        "category": "Converter",
        "action_name": "pdf_to_jpeg",
    },
    {
        "title": "PowerPoint → PDF",
        "description": (
            "Converta apresentações PowerPoint para PDF "
            "preservando o layout."
        ),
        "category": "Converter",
        "action_name": "powerpoint_to_pdf",
    },
    {
        "title": "PDF → PowerPoint",
        "description": (
            "Converta arquivos PDF em apresentações "
            "PowerPoint editáveis."
        ),
        "category": "Converter",
        "action_name": "pdf_to_powerpoint",
    },
    {
        "title": "Excel → PDF",
        "description": (
            "Converta planilhas Excel para PDF "
            "preservando a estrutura."
        ),
        "category": "Converter",
        "action_name": "excel_to_pdf",
    },
    {
        "title": "PDF → Excel",
        "description": (
            "Extraia tabelas de arquivos PDF "
            "para planilhas Excel."
        ),
        "category": "Converter",
        "action_name": "pdf_to_excel",
    },
        {
        "title": "CSV → PDF",
        "description": (
            "Converta arquivos CSV em documentos PDF "
            "organizados e legíveis."
        ),
        "category": "Converter",
        "action_name": "csv_to_pdf",
    },
    {
        "title": "HTML → PDF",
        "description": (
            "Converta páginas e arquivos HTML "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "html_to_pdf",
    },
    {
        "title": "EPUB → PDF",
        "description": (
            "Converta livros digitais EPUB "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "epub_to_pdf",
    },
    {
        "title": "PDF → EPUB",
        "description": (
            "Converta documentos PDF "
            "em livros digitais EPUB."
        ),
        "category": "Converter",
        "action_name": "pdf_to_epub",
    },
    {
        "title": "PNG → PDF",
        "description": (
            "Converta imagens PNG "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "png_to_pdf",
    },
    {
        "title": "PDF → PNG",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens PNG."
        ),
        "category": "Converter",
        "action_name": "pdf_to_png",
    },
    {
        "title": "WEBP → PDF",
        "description": (
            "Converta imagens WEBP "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "webp_to_pdf",
    },
    {
        "title": "PDF → WEBP",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens WEBP."
        ),
        "category": "Converter",
        "action_name": "pdf_to_webp",
    },
    {
        "title": "TIFF → PDF",
        "description": (
            "Converta imagens TIFF "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "tiff_to_pdf",
    },
    {
        "title": "PDF → TIFF",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens TIFF."
        ),
        "category": "Converter",
        "action_name": "pdf_to_tiff",
    },
    {
        "title": "BMP → PDF",
        "description": (
            "Converta imagens BMP "
            "em documentos PDF."
        ),
        "category": "Converter",
        "action_name": "bmp_to_pdf",
    },
    {
        "title": "PDF → BMP",
        "description": (
            "Extraia páginas de arquivos PDF "
            "como imagens BMP."
        ),
        "category": "Converter",
        "action_name": "pdf_to_bmp",
    },
    {
        "title": "PDF → PDF/A",
        "description": (
            "Converta documentos PDF para o padrão "
            "PDF/A de preservação digital."
        ),
        "category": "Converter",
        "action_name": "pdf_to_pdfa",
    },
)