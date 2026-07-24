"""Componente reutilizável de navegação da sidebar."""

from __future__ import annotations
from collections.abc import Callable
import customtkinter as ctk
from app.core.icon_manager import IconManager


class SidebarButton(ctk.CTkFrame):
    """Botão reutilizável para navegação na sidebar."""

    BACKGROUND_COLOR = "transparent"
    ACTIVE_BACKGROUND_COLOR = "#182238"
    HOVER_BACKGROUND_COLOR = "#151D2B"

    TEXT_COLOR = "#AAB7C8"
    ACTIVE_TEXT_COLOR = "#FFFFFF"
    ACCENT_COLOR = "#5B8CFF"

    ICON_SIZE = (18, 18)

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        text: str,
        command: Callable[[], None] | None = None,
        *,
        active: bool = False,
        icon_name: str | None = None,
    ) -> None:
        super().__init__(
            master=master,
            fg_color=self.BACKGROUND_COLOR,
            corner_radius=8,
            height=44,
        )

        self._command = command
        self._active = active
        self._icon = IconManager.load(icon_name, self.ICON_SIZE) if icon_name else None

        self.grid_columnconfigure(1, weight=1)
        self.grid_propagate(False)

        self._active_indicator = ctk.CTkFrame(
            master=self,
            width=3,
            height=24,
            corner_radius=2,
            fg_color=(self.ACCENT_COLOR if self._active else self.BACKGROUND_COLOR),
        )
        self._active_indicator.grid(
            row=0,
            column=0,
            padx=(0, 8),
            pady=10,
            sticky="ns",
        )

        self._button = ctk.CTkButton(
            master=self,
            text=text,
            image=self._icon,
            compound="left",
            command=self._handle_click,
            anchor="w",
            height=44,
            corner_radius=8,
            border_width=0,
            fg_color=(
                self.ACTIVE_BACKGROUND_COLOR if self._active else self.BACKGROUND_COLOR
            ),
            hover_color=self.HOVER_BACKGROUND_COLOR,
            text_color=(self.ACTIVE_TEXT_COLOR if self._active else self.TEXT_COLOR),
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold" if self._active else "normal",
            ),
        )
        self._button.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

    def set_active(self, active: bool) -> None:
        """Atualiza visualmente o estado ativo do botão."""

        self._active = active

        self._active_indicator.configure(
            fg_color=(self.ACCENT_COLOR if active else self.BACKGROUND_COLOR)
        )

        self._button.configure(
            fg_color=(
                self.ACTIVE_BACKGROUND_COLOR if active else self.BACKGROUND_COLOR
            ),
            text_color=(self.ACTIVE_TEXT_COLOR if active else self.TEXT_COLOR),
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold" if active else "normal",
            ),
        )

    def _handle_click(self) -> None:
        """Executa o callback associado ao item."""

        if self._command is not None:
            self._command()
