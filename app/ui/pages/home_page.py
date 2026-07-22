from __future__ import annotations

import customtkinter as ctk

from app.ui import theme
from app.ui.components.category_filter import CategoryFilter
from app.ui.components.hero_banner import HeroBanner
from app.ui.typography import (
    body_font,
    body_medium_font,
    caption_font,
    display_font,
    section_title_font,
)


class HomePage(ctk.CTkFrame):
    """Página inicial do ForgeDocs."""

    CATEGORIES = (
        "Todas",
        "Conversão",
        "Ferramentas PDF",
        "Imagens",
        "OCR",
        "Segurança",
    )

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master=master,
            corner_radius=0,
            fg_color=theme.BACKGROUND_PRIMARY,
        )

        self._configure_layout()
        self._build_page()

    def _configure_layout(self) -> None:
        """Configura o comportamento responsivo da página."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_page(self) -> None:
        """Constrói todos os elementos visuais da página."""
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
        self._build_category_filter()
        self._build_tools_section()
        self._build_supported_formats_section()
        self._build_recent_activity_section()

    def _build_category_filter(self) -> None:
        """Constrói a barra de categorias das ferramentas."""
        section = ctk.CTkFrame(
            master=self.content,
            fg_color="transparent",
        )
        section.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(0, theme.SPACE_XL),
        )
        section.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            master=section,
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

        self.category_filter = CategoryFilter(
            master=section,
            categories=self.CATEGORIES,
            on_category_change=self._handle_category_change,
        )
        self.category_filter.grid(
            row=1,
            column=0,
            sticky="w",
        )

    def _build_tools_section(self) -> None:
        """Constrói a seção provisória de ferramentas."""
        section = ctk.CTkFrame(
            master=self.content,
            fg_color="transparent",
        )
        section.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(0, theme.SPACE_XL),
        )
        section.grid_columnconfigure((0, 1), weight=1, uniform="tools")

        self._create_tool_placeholder(
            master=section,
            row=0,
            column=0,
            title="Converter arquivos",
            description="Converta documentos e imagens entre formatos compatíveis.",
            status="Disponível em breve",
        )

        self._create_tool_placeholder(
            master=section,
            row=0,
            column=1,
            title="Organizar PDFs",
            description="Mescle, divida e reorganize páginas com processamento local.",
            status="Em desenvolvimento",
        )

        self._create_tool_placeholder(
            master=section,
            row=1,
            column=0,
            title="Comprimir documentos",
            description="Reduza o tamanho dos arquivos preservando sua qualidade.",
            status="Planejado",
        )

        self._create_tool_placeholder(
            master=section,
            row=1,
            column=1,
            title="Processar imagens",
            description="Prepare imagens para documentos e fluxos profissionais.",
            status="Planejado",
        )

    def _build_supported_formats_section(self) -> None:
        """Constrói a área de formatos previstos."""
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
        )
        formats_frame.grid(
            row=2,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_LG, theme.SPACE_XL),
        )

        formats = ("PDF", "DOCX", "XLSX", "PPTX", "PNG", "JPG")

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
        """Constrói o estado vazio da atividade recente."""
        section = ctk.CTkFrame(
            master=self.content,
            corner_radius=theme.RADIUS_LARGE,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
        )
        section.grid(
            row=4,
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
            text="As operações concluídas aparecerão aqui para consulta rápida.",
            font=body_font(),
            text_color=theme.TEXT_MUTED,
        )
        empty_description.grid(
            row=2,
            column=0,
            pady=(0, theme.SPACE_2XL),
        )

    def _handle_category_change(self, category: str) -> None:
        """Recebe temporariamente a categoria selecionada."""
        print(f"Categoria selecionada: {category}")

    def _create_tool_placeholder(
        self,
        master: ctk.CTkFrame,
        row: int,
        column: int,
        title: str,
        description: str,
        status: str,
    ) -> None:
        """Cria um card provisório para uma ferramenta."""
        card = ctk.CTkFrame(
            master=master,
            height=theme.CARD_MIN_HEIGHT,
            corner_radius=theme.RADIUS_LARGE,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
        )
        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=(
                0 if column == 0 else theme.SPACE_SM,
                theme.SPACE_SM if column == 0 else 0,
            ),
            pady=(0, theme.SPACE_LG),
        )
        card.grid_propagate(False)
        card.grid_columnconfigure(0, weight=1)

        status_label = ctk.CTkLabel(
            master=card,
            text=status,
            font=caption_font(),
            text_color=theme.ACCENT_HOVER,
            fg_color=theme.ACCENT_SOFT,
            corner_radius=theme.RADIUS_SMALL,
            height=28,
        )
        status_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_XL, theme.SPACE_LG),
        )

        title_label = ctk.CTkLabel(
            master=card,
            text=title,
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
            anchor="w",
        )
        title_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
        )

        description_label = ctk.CTkLabel(
            master=card,
            text=description,
            font=body_font(),
            text_color=theme.TEXT_SECONDARY,
            justify="left",
            anchor="w",
            wraplength=390,
        )
        description_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_SM, theme.SPACE_XL),
        )

    def _build_hero_banner(self) -> None:
        """Insere o banner principal na página."""
        self.hero_banner = HeroBanner(
            master=self.content,
        )
        self.hero_banner.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=theme.SPACE_2XL,
            pady=(theme.SPACE_2XL, theme.SPACE_XL),
    )