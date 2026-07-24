import customtkinter as ctk


class SidebarFooter(ctk.CTkFrame):
    """Rodapé da sidebar."""

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(
            master=master,
            fg_color="transparent",
            corner_radius=0,
        )

        version_label = ctk.CTkLabel(
            master=self,
            text="ForgeDocs v0.1 Alpha",
            text_color="#6F7C8E",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=11,
            ),
        )
        version_label.pack(
            padx=20,
            pady=20,
        )