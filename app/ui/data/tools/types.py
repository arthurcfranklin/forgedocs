"""Tipos utilizados pelo catálogo do ForgeDocs."""

from __future__ import annotations

from typing import TypedDict


class ToolDefinition(TypedDict):
    """Estrutura de uma ferramenta do ForgeDocs."""

    title: str
    description: str
    category: str
    action_name: str