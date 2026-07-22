from __future__ import annotations
import customtkinter as ctk
from app.ui import theme
from app.ui.pages.home_page import HomePage

class MainWindow(ctk.CTk):

    DEFAULT_WIDTH = 1500
    DEFAULT_HEIGHT = 920
    MIN_WIDTH = 1280
    MIN_HEIGHT = 720

    def __init__(self) -> None:
        super().__init__()

        self._configure_appearance()
        self._configure_window()
        self._configure_layout()
        self._build_placeholder_content()

    def _configure_appearance(self) -> None:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def _configure_window(self) -> None:
        self.title("ForgeDocs")
        self.geometry(f"{self.DEFAULT_WIDTH}x{self.DEFAULT_HEIGHT}")
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.configure(fg_color=theme.BACKGROUND_PRIMARY)

        self._center_window()

    def _configure_layout(self) -> None:
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def _build_placeholder_content(self) -> None:
        self.sidebar_frame = ctk.CTkFrame(
            master=self,
            width=theme.SIDEBAR_WIDTH,
            corner_radius=0,
            fg_color=theme.SIDEBAR_BACKGROUND,
        )
        self.sidebar_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.sidebar_frame.grid_propagate(False)
        self.content_frame = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            fg_color=theme.BACKGROUND_PRIMARY,
        )
        self.content_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        self.home_page = HomePage(self.content_frame)
        self.home_page.pack(
    fill="both",
    expand=True,
)

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

    def _center_window(self) -> None:
        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_x = max((screen_width - self.DEFAULT_WIDTH) // 2, 0)
        position_y = max((screen_height - self.DEFAULT_HEIGHT) // 2, 0)

        self.geometry(
            f"{self.DEFAULT_WIDTH}x{self.DEFAULT_HEIGHT}"
            f"+{position_x}+{position_y}"
        )