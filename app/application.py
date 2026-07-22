"""Inicialização da aplicação ForgeDocs."""

from __future__ import annotations

from app.core.config import load_settings
from app.core.logging_config import configure_logging, get_logger

logger = get_logger(__name__)


class ForgeDocsApplication:
    """Classe principal da aplicação."""

    def __init__(self) -> None:
        configure_logging()

        self.settings = load_settings()

        logger.info("ForgeDocs iniciado com sucesso.")

    def run(self) -> None:
        """Executa a aplicação."""

        logger.info("Interface gráfica ainda não implementada.")