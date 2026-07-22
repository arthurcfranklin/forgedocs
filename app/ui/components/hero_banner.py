"""Banner principal da página inicial."""

import customtkinter as ctk

from app.ui import theme
from app.ui.typography import (
    body_font,
    body_medium_font,
    caption_font,
    display_font,
    section_title_font,
)


class HeroBanner(ctk.CTkFrame):
    """Banner principal com proposta de valor e indicadores de privacidade."""

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master=master,
            corner_radius=theme.RADIUS_XLARGE,
            fg_color=theme.BACKGROUND_SECONDARY,
            border_width=1,
            border_color=theme.BORDER_SUBTLE,
        )

        self._configure_layout()
        self._build_component()

    def _configure_layout(self) -> None:
        """Configura a distribuição interna do banner."""
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

    def _build_component(self) -> None:
        """Constrói os elementos visuais do banner."""
        self._build_content_section()
        self._build_visual_section()

    def _build_content_section(self) -> None:
        """Constrói o conteúdo textual do lado esquerdo."""
        content = ctk.CTkFrame(
            master=self,
            fg_color="transparent",
        )
        content.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(theme.SPACE_2XL, theme.SPACE_XL),
            pady=theme.SPACE_2XL,
        )
        content.grid_columnconfigure(0, weight=1)

        eyebrow = ctk.CTkLabel(
            master=content,
            text="FORGEDOCS • CONVERSOR DE ARQUIVOS",
            font=caption_font(),
            text_color=theme.ACCENT_PRIMARY,
            anchor="w",
        )
        eyebrow.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, theme.SPACE_MD),
        )

        title = ctk.CTkLabel(
            master=content,
            text="Documentos profissionais.\nPrivados por padrão.",
            font=display_font(),
            text_color=theme.TEXT_PRIMARY,
            justify="left",
            anchor="w",
        )
        title.grid(
            row=1,
            column=0,
            sticky="w",
        )

        subtitle = ctk.CTkLabel(
            master=content,
            text=(
                "Conversão, organização e processamento local em uma única aplicação.\n"
                "Rápido, privado e sem depender da nuvem."
            ),
            font=body_font(),
            text_color=theme.TEXT_SECONDARY,
            justify="left",
            anchor="w",
            wraplength=760,
        )
        subtitle.grid(
            row=2,
            column=0,
            sticky="w",
            pady=(theme.SPACE_XL, theme.SPACE_2XL),
        )

        badges = ctk.CTkFrame(
            master=content,
            fg_color="transparent",
        )
        badges.grid(
            row=3,
            column=0,
            sticky="w",
        )

        badge_items = (
            "100% Local",
            "100% Privado",
            "Sem Upload",
            "Ultra Rápido",
        )

        for column, text in enumerate(badge_items):
            self._create_badge(
                master=badges,
                text=text,
                column=column,
            )

    def _build_visual_section(self) -> None:
        """Constrói o manifesto visual do lado direito."""
        panel = ctk.CTkFrame(
            master=self,
            corner_radius=theme.RADIUS_LARGE,
            fg_color=theme.SURFACE_DEFAULT,
            border_width=1,
            border_color=theme.BORDER_DEFAULT,
        )
        panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(0, theme.SPACE_2XL),
            pady=theme.SPACE_2XL,
        )
        panel.grid_columnconfigure(0, weight=1)

        header = ctk.CTkLabel(
            master=panel,
            text="NOSSA FILOSOFIA",
            font=caption_font(),
            text_color=theme.TEXT_MUTED,
            anchor="w",
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_XL, theme.SPACE_LG),
        )

        principles = ctk.CTkFrame(
            master=panel,
            fg_color="transparent",
        )
        principles.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=theme.SPACE_XL,
            pady=(0, theme.SPACE_LG),
        )
        principles.grid_columnconfigure(1, weight=1)

        principle_items = (
            "Privacidade por padrão",
            "Processamento local",
            "Sem dependência de nuvem",
            "Totalmente offline",
        )

        for row, item in enumerate(principle_items):
            marker = ctk.CTkLabel(
                master=principles,
                text="●",
                width=18,
                font=caption_font(),
                text_color=theme.ACCENT_PRIMARY,
            )
            marker.grid(
                row=row,
                column=0,
                sticky="w",
                pady=3,
            )

            label = ctk.CTkLabel(
                master=principles,
                text=item,
                font=section_title_font(),
                text_color=theme.TEXT_PRIMARY,
                anchor="w",
            )
            label.grid(
                row=row,
                column=1,
                sticky="ew",
                padx=(theme.SPACE_SM, 0),
                pady=3,
            )

        divider = ctk.CTkFrame(
            master=panel,
            height=1,
            fg_color=theme.BORDER_DEFAULT,
        )
        divider.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=theme.SPACE_XL,
        )

        manifesto_frame = ctk.CTkFrame(
            master=panel,
            fg_color="transparent",
        )
        manifesto_frame.grid(
            row=3,
            column=0,
            sticky="w",
            padx=theme.SPACE_XL,
            pady=(theme.SPACE_LG, theme.SPACE_XL),
        )

        manifesto = ctk.CTkLabel(
            master=manifesto_frame,
            text="Seus dados, seu controle.",
            font=section_title_font(),
            text_color=theme.TEXT_PRIMARY,
        )
        manifesto.grid(
            row=0,
            column=0,
            sticky="w",
        )

        highlight = ctk.CTkLabel(
            master=manifesto_frame,
            text=" No seu computador.",
            font=section_title_font(),
            text_color=theme.ACCENT_PRIMARY,
        )
        highlight.grid(
            row=0,
            column=1,
            sticky="w",
        )

    def _create_badge(
        self,
        master: ctk.CTkFrame,
        text: str,
        column: int,
    ) -> None:
        """Cria um indicador de privacidade."""
        badge = ctk.CTkLabel(
            master=master,
            text=text,
            height=36,
            corner_radius=theme.RADIUS_SMALL,
            fg_color=theme.ACCENT_SOFT,
            text_color=theme.ACCENT_HOVER,
            font=caption_font(),
        )
        badge.grid(
            row=0,
            column=column,
            padx=(0, theme.SPACE_SM),
        )