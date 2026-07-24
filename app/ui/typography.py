"""Definições tipográficas da interface do ForgeDocs."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Final

import customtkinter as ctk


FONT_FAMILY_LIGHT: Final[str] = "Host Grotesk Light"
FONT_FAMILY_REGULAR: Final[str] = "Host Grotesk"
FONT_FAMILY_MEDIUM: Final[str] = "Host Grotesk Medium"
FONT_FAMILY_SEMIBOLD: Final[str] = "Host Grotesk SemiBold"
FONT_FAMILY_BOLD: Final[str] = "Host Grotesk"
FONT_FAMILY_EXTRABOLD: Final[str] = "Host Grotesk ExtraBold"

FONT_FAMILY_MONOSPACE: Final[str] = "Cascadia Code"

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]

FONTS_DIRECTORY: Final[Path] = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "HostGrotesk"
)

FONT_FILES: Final[tuple[str, ...]] = (
    "hostgrotesk-light.ttf",
    "hostgrotesk-light-italic.ttf",
    "hostgrotesk-regular.ttf",
    "hostgrotesk-italic.ttf",
    "hostgrotesk-medium.ttf",
    "hostgrotesk-medium-italic.ttf",
    "hostgrotesk-semibold.ttf",
    "hostgrotesk-semibold-italic.ttf",
    "hostgrotesk-bold.ttf",
    "hostgrotesk-bold-italic.ttf",
    "hostgrotesk-extrabold.ttf",
    "hostgrotesk-extrabold-italic.ttf",
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
def hero_title_font() -> ctk.CTkFont:
    """Fonte utilizada no título principal do Hero."""
    return ctk.CTkFont(
        family=FONT_FAMILY_EXTRABOLD,
        size=44,
        weight="normal",
    )


@lru_cache(maxsize=1)
def display_font() -> ctk.CTkFont:
    """Fonte utilizada em títulos de grande destaque."""
    return ctk.CTkFont(
        family=FONT_FAMILY_BOLD,
        size=36,
        weight="bold",
    )


@lru_cache(maxsize=1)
def page_title_font() -> ctk.CTkFont:
    """Fonte utilizada nos títulos principais das páginas."""
    return ctk.CTkFont(
        family=FONT_FAMILY_BOLD,
        size=26,
        weight="bold",
    )


@lru_cache(maxsize=1)
def section_title_font() -> ctk.CTkFont:
    """Fonte utilizada nos títulos de seções e cards."""
    return ctk.CTkFont(
        family=FONT_FAMILY_SEMIBOLD,
        size=18,
        weight="normal",
    )


@lru_cache(maxsize=1)
def body_font() -> ctk.CTkFont:
    """Fonte padrão utilizada nos textos da interface."""
    return ctk.CTkFont(
        family=FONT_FAMILY_REGULAR,
        size=16,
        weight="normal",
    )


@lru_cache(maxsize=1)
def body_medium_font() -> ctk.CTkFont:
    """Fonte utilizada em textos com ênfase intermediária."""
    return ctk.CTkFont(
        family=FONT_FAMILY_MEDIUM,
        size=15,
        weight="normal",
    )


@lru_cache(maxsize=1)
def caption_font() -> ctk.CTkFont:
    """Fonte utilizada em legendas, metadados e textos auxiliares."""
    return ctk.CTkFont(
        family=FONT_FAMILY_MEDIUM,
        size=13,
        weight="normal",
    )


@lru_cache(maxsize=1)
def button_font() -> ctk.CTkFont:
    """Fonte utilizada nos botões."""
    return ctk.CTkFont(
        family=FONT_FAMILY_SEMIBOLD,
        size=14,
        weight="normal",
    )


@lru_cache(maxsize=1)
def navigation_font() -> ctk.CTkFont:
    """Fonte utilizada nos itens de navegação."""
    return ctk.CTkFont(
        family=FONT_FAMILY_MEDIUM,
        size=14,
        weight="normal",
    )


@lru_cache(maxsize=1)
def navigation_active_font() -> ctk.CTkFont:
    """Fonte utilizada no item de navegação ativo."""
    return ctk.CTkFont(
        family=FONT_FAMILY_SEMIBOLD,
        size=14,
        weight="normal",
    )


@lru_cache(maxsize=1)
def brand_font() -> ctk.CTkFont:
    """Fonte utilizada na identidade textual do ForgeDocs."""
    return ctk.CTkFont(
        family=FONT_FAMILY_BOLD,
        size=20,
        weight="bold",
    )


@lru_cache(maxsize=1)
def monospace_font() -> ctk.CTkFont:
    """Fonte monoespaçada utilizada em informações técnicas."""
    return ctk.CTkFont(
        family=FONT_FAMILY_MONOSPACE,
        size=12,
        weight="normal",
    )