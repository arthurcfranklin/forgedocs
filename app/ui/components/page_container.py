"""Contêiner responsável por hospedar as páginas da aplicação."""

from __future__ import annotations

import customtkinter as ctk

from app.ui import theme


class PageContainer(ctk.CTkFrame):
    """Área principal destinada à exibição das páginas do ForgeDocs."""

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(
            master=master,
            corner_radius=0,
            fg_color=theme.BACKGROUND_PRIMARY,
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._current_page: ctk.CTkBaseClass | None = None

    def show_page(self, page: ctk.CTkBaseClass) -> None:
        """Exibe uma página no contêiner."""
        if page is self._current_page:
            return

        if self._current_page is not None:
            self._current_page.grid_remove()

        self._current_page = page
        self._current_page.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

    @property
    def current_page(self) -> ctk.CTkBaseClass | None:
        """Retorna a página atualmente exibida."""
        return self._current_page