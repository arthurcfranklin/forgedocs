"""Página inicial do ForgeDocs."""

from collections.abc import Callable

import customtkinter as ctk

from app.ui import theme
from app.ui.components.category_filter import CategoryFilter
from app.ui.components.feature_card import FeatureCard
from app.ui.components.hero_banner import HeroBanner
from app.ui.data.tools import (
    TOOLS,
    TOOL_CATEGORIES,
    ToolDefinition,
    ToolStatus,
)
from app.ui.typography import (
    body_font,
    body_medium_font,
    section_title_font,
)

class HomePage(ctk.CTkFrame):
    """Página inicial do ForgeDocs."""

    GRID_COLUMNS = 4

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master=master,
            corner_radius=0,
            fg_color=theme.BACKGROUND_PRIMARY,
        )

        self._active_category = "Todas"
        self._tools_frame: ctk.CTkFrame | None = None

        self._configure_layout()
        self._build_page()

    def _configure_layout(self) -> None:
        """Configura o comportamento estrutural da página."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_page(self) -> None:
        """Constrói todas as seções da página inicial."""
        self.content = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=0,
            fg_color=theme.BACKGROUND_PRIMARY,
            scrollbar_button_color=theme.SURFACE_ELEVATED,
            scrollbar_button_hover_color=theme.SURFACE_HOVER,
        )
        self.content.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.content.grid_columnconfigure(0, weight=1)

        self._build_hero_banner()
        self._build_tools_section()
        self._build_supported_formats_section()
        self._build_recent_activity_section()

    def _build_hero_banner(self) -> None:
        """Adiciona o banner principal."""
        self.hero_banner = HeroBanner(master=self.content)
        self.hero_banner.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(theme.SPACE_2XL, theme.SPACE_XL),
        )

    def _build_tools_section(self) -> None:
        """Constrói a seção de ferramentas."""
        self.tools_section = ctk.CTkFrame(
            master=self.content,
            fg_color="transparent",
            corner_radius=0,
        )
        self.tools_section.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(0, theme.SPACE_XL),
        )
        self.tools_section.grid_columnconfigure(0, weight=1)

        self._build_tools_header()
        self._build_category_filter()
        self._build_tools_grid()

    def _build_tools_header(self) -> None:
        """Constrói o título da seção de ferramentas."""
        title = ctk.CTkLabel(
            master=self.tools_section,
            text="Ferramentas",
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
            anchor="w",
        )
        title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, theme.SPACE_LG),
        )

    def _build_category_filter(self) -> None:
        """Constrói o filtro de categorias."""
        self.category_filter = CategoryFilter(
            master=self.tools_section,
            categories=TOOL_CATEGORIES,
            on_category_change=self._handle_category_change,
            initial_category=self._active_category,
        )
        self.category_filter.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(4, 0),
            pady=(0, theme.SPACE_LG),
        )

    def _build_tools_grid(self) -> None:
        """Cria ou reconstrói a grade de ferramentas."""
        if self._tools_frame is not None:
            self._tools_frame.destroy()

        self._tools_frame = ctk.CTkFrame(
            master=self.tools_section,
            fg_color="transparent",
            corner_radius=0,
        )
        self._tools_frame.grid(
            row=2,
            column=0,
            sticky="ew",
        )

        for column in range(self.GRID_COLUMNS):
            self._tools_frame.grid_columnconfigure(
                column,
                weight=1,
                uniform="tools",
            )

        visible_tools = self._get_visible_tools()

        for index, tool in enumerate(visible_tools):
            self._build_tool_card(
                tool=tool,
                index=index,
            )

    def _build_tool_card(
        self,
        tool: ToolDefinition,
        index: int,
    ) -> None:
        """Cria um card individual de ferramenta."""
        if self._tools_frame is None:
            return

        row = index // self.GRID_COLUMNS
        column = index % self.GRID_COLUMNS

        card = FeatureCard(
            master=self._tools_frame,
            title=tool["title"],
            description=tool["description"],
            action_text="Abrir",
            status=tool.get("status", ToolStatus.AVAILABLE),
            command=self._create_tool_command(
                action_name=tool["action_name"],
            ),
        )

        left_padding = 0 if column == 0 else theme.SPACE_SM
        right_padding = (
            0
            if column == self.GRID_COLUMNS - 1
            else theme.SPACE_SM
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=(left_padding, right_padding),
            pady=(0, theme.SPACE_LG),
        )

    def _get_visible_tools(self) -> tuple[ToolDefinition, ...]:
        """Retorna as ferramentas da categoria selecionada."""
        if self._active_category == "Todas":
            return TOOLS

        return tuple(
            tool
            for tool in TOOLS
            if tool["category"] == self._active_category
        )

    def _create_tool_command(
        self,
        action_name: str,
    ) -> Callable[[], None]:
        """Cria o callback de abertura de uma ferramenta."""
        return lambda: self._handle_tool_open(action_name)

    def _handle_category_change(self, category: str) -> None:
        """Atualiza os cards conforme a categoria selecionada."""
        self._active_category = category
        self._build_tools_grid()

    def _handle_tool_open(self, action_name: str) -> None:
        """Recebe temporariamente a ferramenta selecionada."""
        print(f"Abrir ferramenta: {action_name}")

    def _build_supported_formats_section(self) -> None:
        """Constrói a seção de formatos suportados."""
        section = ctk.CTkFrame(
            master=self.content,
            corner_radius=theme.RADIUS_LARGE,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
        )
        section.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(0, theme.SPACE_XL),
        )
        section.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            master=section,
            text="Formatos suportados",
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
            anchor="w",
        )
        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_XL, theme.SPACE_SM),
        )

        description = ctk.CTkLabel(
            master=section,
            text="A compatibilidade será ampliada progressivamente.",
            font=body_font(),
            text_color=theme.TEXT_SECONDARY,
            anchor="w",
        )
        description.grid(
            row=1,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
        )

        formats_frame = ctk.CTkFrame(
            master=section,
            fg_color="transparent",
            corner_radius=0,
        )
        formats_frame.grid(
            row=2,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_LG, theme.SPACE_XL),
        )

        formats = (
            "PDF",
            "DOC",
            "DOCX",
            "XLS",
            "XLSX",
            "PPT",
            "PPTX",
            "JPEG",
            "JPG",
            "PNG",
        )

        for index, file_format in enumerate(formats):
            label = ctk.CTkLabel(
                master=formats_frame,
                text=file_format,
                width=64,
                height=34,
                corner_radius=theme.RADIUS_SMALL,
                fg_color=theme.BACKGROUND_TERTIARY,
                text_color=theme.TEXT_SECONDARY,
                font=body_medium_font(),
            )
            label.grid(
                row=0,
                column=index,
                padx=(0, theme.SPACE_SM),
            )

    def _build_recent_activity_section(self) -> None:
        """Constrói a seção de atividade recente."""
        section = ctk.CTkFrame(
            master=self.content,
            corner_radius=theme.RADIUS_LARGE,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
        )
        section.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(0, theme.SPACE_2XL),
        )
        section.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            master=section,
            text="Atividade recente",
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
            anchor="w",
        )
        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_XL, theme.SPACE_SM),
        )

        empty_title = ctk.CTkLabel(
            master=section,
            text="Nenhuma operação realizada",
            font=body_medium_font(),
            text_color=theme.TEXT_SECONDARY,
        )
        empty_title.grid(
            row=1,
            column=0,
            pady=(theme.SPACE_XL, theme.SPACE_SM),
        )

        empty_description = ctk.CTkLabel(
            master=section,
            text=(
                "As operações concluídas aparecerão aqui "
                "para consulta rápida."
            ),
            font=body_font(),
            text_color=theme.TEXT_MUTED,
        )
        empty_description.grid(
            row=2,
            column=0,
            pady=(0, theme.SPACE_2XL),
        )