"""Catálogo central de ferramentas do ForgeDocs."""

from __future__ import annotations

from app.ui.data.tools.categories import TOOL_CATEGORIES
from app.ui.data.tools.converter import CONVERTER_TOOLS
from app.ui.data.tools.edit import EDIT_TOOLS
from app.ui.data.tools.optimize import OPTIMIZE_TOOLS
from app.ui.data.tools.organize import ORGANIZE_TOOLS
from app.ui.data.tools.security import SECURITY_TOOLS
from app.ui.data.tools.types import ToolDefinition

TOOLS: tuple[ToolDefinition, ...] = (
    *CONVERTER_TOOLS,
    *ORGANIZE_TOOLS,
    *EDIT_TOOLS,
    *OPTIMIZE_TOOLS,
    *SECURITY_TOOLS,
)

__all__ = (
    "TOOLS",
    "TOOL_CATEGORIES",
    "ToolDefinition",
)