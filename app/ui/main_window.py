from __future__ import annotations

import customtkinter as ctk

from app.ui import theme
from app.ui.components.page_container import PageContainer
from app.ui.components.sidebar import Sidebar
from app.ui.pages.home_page import HomePage


class MainWindow(ctk.CTk):
    """Janela principal da aplicação ForgeDocs."""

    DEFAULT_WIDTH = 1500
    DEFAULT_HEIGHT = 920
    MIN_WIDTH = 1280
    MIN_HEIGHT = 720

    def __init__(self) -> None:
        super().__init__()

        self._configure_appearance()
        self._configure_window()
        self._configure_layout()
        self._build_application_shell()

    def _configure_appearance(self) -> None:
        """Configura a aparência global da interface."""

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def _configure_window(self) -> None:
        """Configura as propriedades da janela principal."""

        self.title("ForgeDocs")
        self.geometry(f"{self.DEFAULT_WIDTH}x{self.DEFAULT_HEIGHT}")
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.configure(fg_color=theme.BACKGROUND_PRIMARY)

        self._center_window()

    def _configure_layout(self) -> None:
        """Configura o grid principal da janela."""

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def _build_application_shell(self) -> None:
        """Constrói a estrutura principal da interface."""

        self._build_sidebar()
        self._build_page_container()
        self._build_status_bar()

    def _build_sidebar(self) -> None:
        """Constrói a sidebar principal da aplicação."""

        self.sidebar = Sidebar(
            master=self,
            on_navigate=self._handle_navigation,
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

    def _build_page_container(self) -> None:
        """Constrói a área responsável pela exibição das páginas."""

        self.page_container = PageContainer(self)
        self.page_container.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        self.home_page = HomePage(self.page_container)
        self.page_container.show_page(self.home_page)

    def _build_status_bar(self) -> None:
        """Constrói a barra de status inferior."""

        self.status_bar_frame = ctk.CTkFrame(
            master=self,
            height=theme.STATUS_BAR_HEIGHT,
            corner_radius=0,
            fg_color=theme.STATUS_BAR_BACKGROUND,
            border_width=1,
            border_color=theme.STATUS_BAR_BORDER,
        )
        self.status_bar_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
        )
        self.status_bar_frame.grid_propagate(False)

    def _handle_navigation(self, item_id: str) -> None:
        """Processa temporariamente as solicitações de navegação."""

        if item_id == "home":
            self.page_container.show_page(self.home_page)

    def _center_window(self) -> None:
        """Centraliza a janela principal na tela."""

        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_x = max(
            (screen_width - self.DEFAULT_WIDTH) // 2,
            0,
        )
        position_y = max(
            (screen_height - self.DEFAULT_HEIGHT) // 2,
            0,
        )

        self.geometry(
            f"{self.DEFAULT_WIDTH}x{self.DEFAULT_HEIGHT}"
            f"+{position_x}+{position_y}"
        )