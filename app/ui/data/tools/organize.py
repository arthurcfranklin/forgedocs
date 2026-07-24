"""Ferramentas da categoria Organizar."""

from __future__ import annotations
from app.ui.data.tools.types import ToolDefinition

ORGANIZE_TOOLS: tuple[ToolDefinition, ...] = (
    {
        "title": "Juntar PDF",
        "description": (
            "Combine vários arquivos PDF "
            "em um único documento."
        ),
        "category": "Organizar",
        "action_name": "merge_pdf",
    },
    {
        "title": "Dividir PDF",
        "description": (
            "Separe páginas de um PDF "
            "em novos arquivos."
        ),
        "category": "Organizar",
        "action_name": "split_pdf",
    },
    {
        "title": "Organizar PDF",
        "description": (
            "Reordene, gire ou remova "
            "páginas de um PDF."
        ),
        "category": "Organizar",
        "action_name": "organize_pdf",
    },
)