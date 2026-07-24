import customtkinter as ctk


class SidebarHeader(ctk.CTkFrame):
    """Cabeçalho institucional da sidebar."""

    BACKGROUND_COLOR = "transparent"
    TITLE_COLOR = "#FFFFFF"
    SUBTITLE_COLOR = "#9AA6B2"
    DIVIDER_COLOR = "#202A38"

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        *,
        title: str = "ForgeDocs",
        subtitle: str = "Professional Toolkit",
    ) -> None:
        super().__init__(
            master=master,
            fg_color=self.BACKGROUND_COLOR,
            corner_radius=0,
        )

        self.grid_columnconfigure(0, weight=1)

        self._title_label = ctk.CTkLabel(
            master=self,
            text=title,
            text_color=self.TITLE_COLOR,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold",
            ),
            anchor="center",
        )
        self._title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(28, 0),
            sticky="ew",
        )

        self._subtitle_label = ctk.CTkLabel(
            master=self,
            text=subtitle,
            text_color=self.SUBTITLE_COLOR,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=15,
                weight="normal",
            ),
            anchor="center",
        )
        self._subtitle_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(2, 24),
            sticky="ew",
        )

        self._divider = ctk.CTkFrame(
            master=self,
            height=1,
            corner_radius=0,
            fg_color=self.DIVIDER_COLOR,
        )
        self._divider.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="ew",
        )
