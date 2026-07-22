from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from app.ui import theme
from app.ui.typography import (
    body_font,
    button_font,
    caption_font,
    section_title_font,
)


class FeatureCard(ctk.CTkFrame):
    """Card compacto para representar uma ferramenta do ForgeDocs."""

    def __init__(
        self,
        master,
        *,
        title: str,
        description: str,
        action_text: str = "Abrir",
        command: Callable[[], None] | None = None,
        accent_color: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            master,
            height=theme.CARD_MIN_HEIGHT,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
            corner_radius=theme.RADIUS_LARGE,
            **kwargs,
        )

        self.grid_propagate(False)

        self.title = title
        self.description = description
        self.action_text = action_text
        self.command = command
        self.accent_color = accent_color or theme.ACCENT_PRIMARY

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_propagate(False)

        self._build_accent()
        self._build_content()

    def _build_accent(self) -> None:
        """Cria a barra superior de destaque."""
        accent = ctk.CTkFrame(
            self,
            height=3,
            fg_color=self.accent_color,
            corner_radius=2,
        )
        accent.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=theme.SPACE_MD,
            pady=(theme.SPACE_MD, 0),
        )
        accent.grid_propagate(False)

    def _build_content(self) -> None:
        """Monta o conteúdo do card."""
        content = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        content.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=theme.SPACE_LG,
            pady=(theme.SPACE_LG, theme.SPACE_LG),
        )
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=1)

        title_label = ctk.CTkLabel(
            content,
            text=self.title,
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
            anchor="w",
            justify="left",
            wraplength=300,
        )
        title_label.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, theme.SPACE_MD),
        )

        description_label = ctk.CTkLabel(
            content,
            text=self.description,
            font=body_font(),
            text_color=theme.TEXT_SECONDARY,
            anchor="nw",
            justify="left",
            wraplength=220,
        )
        description_label.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(0, theme.SPACE_LG),
        )

        action_button = ctk.CTkButton(
            content,
            text=self.action_text,
            command=self._handle_action,
            font=button_font(),
            width=96,
            height=32,
            corner_radius=theme.RADIUS_SMALL,
            fg_color=theme.SURFACE_HOVER,
            hover_color=theme.SURFACE_ACTIVE,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
            text_color=theme.TEXT_PRIMARY,
        )
        action_button.grid(
            row=2,
            column=0,
            sticky="w",
        )

    def _handle_action(self) -> None:
        """Executa a ação vinculada ao card."""
        if self.command is not None:
            self.command()