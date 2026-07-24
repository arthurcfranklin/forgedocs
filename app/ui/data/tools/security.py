"""Ferramentas da categoria Segurança."""

from __future__ import annotations
from app.ui.data.tools.types import ToolDefinition

SECURITY_TOOLS: tuple[ToolDefinition, ...] = (
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
        "title": "Corromper PDF",
        "description": (
            "Gere uma cópia danificada "
            "para testes."
        ),
        "category": "Segurança",
        "action_name": "corrupt_pdf",
    },
)