"""Inicialização e execução principal do ForgeDocs."""

from __future__ import annotations

from app.core.config import load_settings
from app.core.logging_config import configure_logging, get_logger
from app.ui.main_window import MainWindow
from app.ui.typography import load_application_fonts


class ForgeDocsApplication:
    """Coordena a inicialização e execução do ForgeDocs."""

    def __init__(self) -> None:
        configure_logging()

        self.logger = get_logger(__name__)
        self.settings = load_settings()
        self.window: MainWindow | None = None

        self.logger.info("ForgeDocs iniciado com sucesso.")

    def run(self) -> None:
        """Inicializa e mantém ativa a interface gráfica."""
        self.logger.info("Inicializando interface gráfica.")

        load_application_fonts()

        self.window = MainWindow()
        self.window.mainloop()