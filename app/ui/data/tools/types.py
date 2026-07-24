"""Tipos utilizados pelo catálogo do ForgeDocs."""

from __future__ import annotations

from enum import StrEnum
from typing import NotRequired, TypedDict


class ToolStatus(StrEnum):
    """Estados possíveis de uma ferramenta."""

    AVAILABLE = "available"
    COMING_SOON = "coming_soon"


class ToolDefinition(TypedDict):
    """Estrutura de uma ferramenta do ForgeDocs."""

    title: str
    description: str
    category: str
    action_name: str
    status: NotRequired[ToolStatus]