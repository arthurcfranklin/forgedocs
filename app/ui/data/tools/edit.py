"""Ferramentas da categoria Editar."""

from __future__ import annotations
from app.ui.data.tools.types import ToolDefinition

EDIT_TOOLS: tuple[ToolDefinition, ...] = (
        {
        "title": "Editar PDF",
        "description": (
            "Edite textos, imagens e páginas "
            "de documentos PDF."
        ),
        "category": "Editar",
        "action_name": "edit_pdf",
    },
)