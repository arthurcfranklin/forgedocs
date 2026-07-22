"""Definições tipográficas da interface do ForgeDocs."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Final

import customtkinter as ctk


FONT_FAMILY: Final[str] = "Host Grotesk"
FONT_FAMILY_MONOSPACE: Final[str] = "Cascadia Code"

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
FONTS_DIRECTORY: Final[Path] = PROJECT_ROOT / "assets" / "fonts"

FONT_FILES: Final[tuple[str, ...]] = (
    "hostgrotesk-regular.ttf",
    "hostgrotesk-medium.ttf",
    "hostgrotesk-semibold.ttf",
    "hostgrotesk-bold.ttf",
)


def load_application_fonts() -> None:
    """Carrega as fontes utilizadas pela interface do ForgeDocs."""
    missing_fonts: list[str] = []

    for filename in FONT_FILES:
        font_path = FONTS_DIRECTORY / filename

        if not font_path.is_file():
            missing_fonts.append(filename)
            continue

        ctk.FontManager.load_font(str(font_path))

    if missing_fonts:
        missing_list = ", ".join(missing_fonts)

        raise FileNotFoundError(
            f"Arquivos de fonte não encontrados: {missing_list}"
        )


@lru_cache(maxsize=1)
def display_font() -> ctk.CTkFont:
    """Fonte principal para títulos de maior destaque."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=36,
        weight="bold",
    )


@lru_cache(maxsize=1)
def page_title_font() -> ctk.CTkFont:
    """Fonte utilizada nos títulos das páginas."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=26,
        weight="bold",
    )


@lru_cache(maxsize=1)
def section_title_font() -> ctk.CTkFont:
    """Fonte utilizada nos títulos de seções e cards."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=18,
        weight="bold",
    )


@lru_cache(maxsize=1)
def body_font() -> ctk.CTkFont:
    """Fonte padrão para textos da interface."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=16,
        weight="normal",
    )


@lru_cache(maxsize=1)
def body_medium_font() -> ctk.CTkFont:
    """Fonte intermediária para textos com maior ênfase."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=15,
        weight="bold",
    )


@lru_cache(maxsize=1)
def caption_font() -> ctk.CTkFont:
    """Fonte para legendas, metadados e textos auxiliares."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=13,
        weight="normal",
    )


@lru_cache(maxsize=1)
def button_font() -> ctk.CTkFont:
    """Fonte utilizada nos botões."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=14,
        weight="bold",
    )


@lru_cache(maxsize=1)
def navigation_font() -> ctk.CTkFont:
    """Fonte utilizada nos itens de navegação."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=14,
        weight="normal",
    )


@lru_cache(maxsize=1)
def navigation_active_font() -> ctk.CTkFont:
    """Fonte utilizada no item de navegação ativo."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=14,
        weight="bold",
    )


@lru_cache(maxsize=1)
def brand_font() -> ctk.CTkFont:
    """Fonte utilizada na identidade textual do ForgeDocs."""
    return ctk.CTkFont(
        family=FONT_FAMILY,
        size=20,
        weight="bold",
    )


@lru_cache(maxsize=1)
def monospace_font() -> ctk.CTkFont:
    """Fonte monoespaçada para extensões e informações técnicas."""
    return ctk.CTkFont(
        family=FONT_FAMILY_MONOSPACE,
        size=12,
        weight="normal",
    )