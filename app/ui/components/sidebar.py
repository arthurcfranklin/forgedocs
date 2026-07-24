from collections.abc import Callable

import customtkinter as ctk

from app.ui import theme
from app.ui.components.sidebar_button import SidebarButton
from app.ui.components.sidebar_footer import SidebarFooter
from app.ui.components.sidebar_header import SidebarHeader


class Sidebar(ctk.CTkFrame):
    """Componente principal de navegação lateral do ForgeDocs."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        *,
        on_navigate: Callable[[str], None] | None = None,
    ) -> None:
        super().__init__(
            master=master,
            width=theme.SIDEBAR_WIDTH,
            fg_color=theme.SIDEBAR_BACKGROUND,
            corner_radius=0,
        )

        self._on_navigate = on_navigate
        self._buttons: dict[str, SidebarButton] = {}
        self._active_item = "home"

        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._create_header()
        self._create_primary_navigation()
        self._create_secondary_navigation()
        self._create_footer()

    def _create_header(self) -> None:
        """Cria o cabeçalho institucional da sidebar."""

        header = SidebarHeader(
            master=self,
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
        )

    def _create_primary_navigation(self) -> None:
        """Cria os itens principais de navegação."""

        navigation_frame = ctk.CTkFrame(
            master=self,
            fg_color="transparent",
            corner_radius=0,
        )
        navigation_frame.grid(
            row=1,
            column=0,
            padx=theme.SPACE_LG,
            pady=(0, theme.SPACE_LG),
            sticky="ew",
        )
        navigation_frame.grid_columnconfigure(0, weight=1)

        items = [
            ("home", "Início", "house"),
            ("convert", "Converter", "arrow-left-right"),
            ("organize", "Organizar", "list-sort-descending"),
            ("edit", "Editar", "square-pen"),
            ("optimize", "Otimizar", "zap"),
            ("security", "Segurança", "lock-keyhole"),
        ]

        self._create_navigation_buttons(
            master=navigation_frame,
            items=items,
            initial_row=0,
        )

    def _create_secondary_navigation(self) -> None:
        """Cria o divisor e os itens auxiliares da navegação inferior."""

        secondary_navigation_frame = ctk.CTkFrame(
            master=self,
            fg_color="transparent",
            corner_radius=0,
        )
        secondary_navigation_frame.grid(
            row=3,
            column=0,
            padx=theme.SPACE_LG,
            pady=(0, theme.SPACE_SM),
            sticky="ew",
        )
        secondary_navigation_frame.grid_columnconfigure(0, weight=1)

        divider = ctk.CTkFrame(
            master=secondary_navigation_frame,
            height=2,
            corner_radius=0,
            fg_color=theme.DIVIDER_COLOR,
        )
        divider.grid(
            row=0,
            column=0,
            padx=theme.SPACE_SM,
            pady=(0, theme.SPACE_LG),
            sticky="ew",
        )
        divider.grid_propagate(False)

        items = [
            ("open_files", "Abrir arquivos", "folder-open"),
            ("settings", "Configurações", "settings"),
            ("about", "Sobre", "info"),
        ]

        self._create_navigation_buttons(
            master=secondary_navigation_frame,
            items=items,
            initial_row=1,
        )

    def _create_navigation_buttons(
        self,
        master: ctk.CTkFrame,
        items: list[tuple[str, str, str]],
        *,
        initial_row: int,
    ) -> None:
        """Cria e registra um conjunto de botões de navegação."""

        for row_offset, (item_id, label, icon_name) in enumerate(items):
            button = SidebarButton(
                master=master,
                text=label,
                icon_name=icon_name,
                active=item_id == self._active_item,
                command=lambda selected=item_id: self._select_item(
                    selected
                ),
            )
            button.grid(
                row=initial_row + row_offset,
                column=0,
                pady=theme.SPACE_XS,
                sticky="ew",
            )

            self._buttons[item_id] = button

    def _create_footer(self) -> None:
        """Cria o rodapé da sidebar."""

        footer = SidebarFooter(
            master=self,
        )
        footer.grid(
            row=4,
            column=0,
            sticky="ew",
        )

    def _select_item(self, item_id: str) -> None:
        """Atualiza o item ativo e dispara o callback de navegação."""

        if item_id == self._active_item:
            return

        if item_id not in self._buttons:
            return

        current_button = self._buttons.get(self._active_item)

        if current_button is not None:
            current_button.set_active(False)

        self._buttons[item_id].set_active(True)
        self._active_item = item_id

        if self._on_navigate is not None:
            self._on_navigate(item_id)