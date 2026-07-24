"""Ferramentas da categoria Otimizar."""

from __future__ import annotations
from app.ui.data.tools.types import ToolDefinition

OPTIMIZE_TOOLS: tuple[ToolDefinition, ...] = (
        {
        "title": "Comprimir PDF",
        "description": (
            "Reduza o tamanho de arquivos PDF "
            "mantendo a qualidade."
        ),
        "category": "Otimizar",
        "action_name": "compress_pdf",
    },
)