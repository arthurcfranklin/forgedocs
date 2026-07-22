"""Configuração do sistema de logs do ForgeDocs."""

from __future__ import annotations

import logging

from app.core.paths import LOG_FILE, create_required_directories


def configure_logging() -> None:
    """Configura o sistema de logs da aplicação."""

    create_required_directories()

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)-8s | "
            "%(name)s | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    """Retorna um logger configurado."""

    return logging.getLogger(name)