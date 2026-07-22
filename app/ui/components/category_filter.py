"""Componente de filtro por categoria da HomePage."""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from app.ui import theme
from app.ui.typography import button_font


class CategoryFilter(ctk.CTkFrame):
    """Barra horizontal para filtragem de ferramentas por categoria."""

    def __init__(
        self,
        master: ctk.CTkFrame,
        categories: tuple[str, ...],
        on_category_change: Callable[[str], None] | None = None,
        initial_category: str = "Todas",
    ) -> None:
        super().__init__(
            master=master,
            fg_color="transparent",
            corner_radius=0,
        )

        if not categories:
            raise ValueError("CategoryFilter requer ao menos uma categoria.")

        if initial_category not in categories:
            raise ValueError(
                "A categoria inicial precisa existir na lista de categorias."
            )

        self._categories = categories
        self._on_category_change = on_category_change
        self._active_category = initial_category
        self._buttons: dict[str, ctk.CTkButton] = {}

        self._build_component()
        self._refresh_buttons()

    @property
    def active_category(self) -> str:
        """Retorna a categoria atualmente selecionada."""
        return self._active_category

    def select_category(self, category: str) -> None:
        """Seleciona uma categoria e executa o callback configurado."""
        if category not in self._categories:
            raise ValueError(f"Categoria desconhecida: {category}")

        if category == self._active_category:
            return

        self._active_category = category
        self._refresh_buttons()

        if self._on_category_change is not None:
            self._on_category_change(category)

    def _build_component(self) -> None:
        """Constrói os botões do filtro."""
        for column, category in enumerate(self._categories):
            button = ctk.CTkButton(
                master=self,
                text=category,
                width=108,
                height=32,
                corner_radius=theme.RADIUS_MEDIUM,
                border_width=1,
                font=button_font(),
                command=lambda selected=category: self.select_category(selected),
            )
            button.grid(
                row=0,
                column=column,
                padx=(0, 6),
            )

            self._buttons[category] = button

    def _refresh_buttons(self) -> None:
        """Atualiza o estilo visual dos botões."""
        for category, button in self._buttons.items():
            is_active = category == self._active_category

            if is_active:
                button.configure(
                    fg_color=theme.ACCENT_PRIMARY,
                    hover_color=theme.ACCENT_HOVER,
                    border_color=theme.ACCENT_PRIMARY,
                    text_color=theme.TEXT_PRIMARY,
                )
            else:
                button.configure(
                    fg_color=theme.SURFACE_DEFAULT,
                    hover_color=theme.SURFACE_HOVER,
                    border_color=theme.BORDER_DEFAULT,
                    text_color=theme.TEXT_SECONDARY,
                )