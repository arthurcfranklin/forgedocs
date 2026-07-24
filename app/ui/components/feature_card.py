from collections.abc import Callable
from typing import TypedDict

import customtkinter as ctk

from app.ui import theme
from app.ui.data.tools.types import ToolStatus
from app.ui.typography import (
    body_font,
    button_font,
    caption_font,
    section_title_font,
)

class ToolStatusConfig(TypedDict):
    """Configuração visual e funcional de um estado de ferramenta."""

    badge_text: str | None
    enabled: bool



TOOL_STATUS_CONFIG: dict[ToolStatus, ToolStatusConfig] = {
    ToolStatus.AVAILABLE: {
        "badge_text": None,
        "enabled": True,
    },
    ToolStatus.COMING_SOON: {
        "badge_text": "Em breve",
        "enabled": False,
    },
}



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
        status: ToolStatus = ToolStatus.AVAILABLE,
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

        self.title = title
        self.description = description
        self.action_text = action_text
        self.command = command
        self.accent_color = accent_color or theme.ACCENT_PRIMARY
        self.status = status

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_propagate(False)

        self._build_accent()
        self._build_content()

    @property
    def status_config(self) -> ToolStatusConfig:
        """Retorna a configuração associada ao estado atual."""
        return TOOL_STATUS_CONFIG[self.status]

    @property
    def is_available(self) -> bool:
        """Indica se a ferramenta pode ser utilizada."""
        return self.status_config["enabled"]

    @property
    def status_text(self) -> str | None:
        """Retorna o texto visual associado ao estado."""
        return self.status_config["badge_text"]

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

        header = ctk.CTkFrame(
            content,
            fg_color="transparent",
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, theme.SPACE_MD),
        )
        header.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            header,
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
            sticky="w",
        )

        if self.status_text is not None:
            status_badge = ctk.CTkLabel(
                header,
                text=self.status_text,
                font=caption_font(),
                text_color=theme.TEXT_SECONDARY,
                fg_color=theme.SURFACE_HOVER,
                corner_radius=theme.RADIUS_SMALL,
                padx=8,
                pady=2,
            )
            status_badge.grid(
                row=0,
                column=1,
                sticky="e",
                padx=(theme.SPACE_MD, 0),
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
            state="normal" if self.is_available else "disabled",
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
        """Executa a ação vinculada ao card quando disponível."""
        if not self.is_available:
            return

        if self.command is not None:
            self.command()