"""Gerenciamento centralizado de caminhos do ForgeDocs."""

from __future__ import annotations

import sys
from pathlib import Path

from app.core.constants import (
    CONFIG_DIRECTORY_NAME,
    CONFIG_FILE_NAME,
    LOG_DIRECTORY_NAME,
    LOG_FILE_NAME,
    OUTPUT_DIRECTORY_NAME,
    TEMP_DIRECTORY_NAME,
)


def _get_project_root() -> Path:
    """Retorna o diretório raiz do projeto ou do executável."""

    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parents[2]


PROJECT_ROOT = _get_project_root()

APP_DIRECTORY = PROJECT_ROOT / "app"

ASSETS_DIRECTORY = PROJECT_ROOT / "assets"
ICONS_DIRECTORY = ASSETS_DIRECTORY / "icons"
IMAGES_DIRECTORY = ASSETS_DIRECTORY / "images"

CONFIG_DIRECTORY = PROJECT_ROOT / CONFIG_DIRECTORY_NAME
LOG_DIRECTORY = PROJECT_ROOT / LOG_DIRECTORY_NAME
TEMP_DIRECTORY = PROJECT_ROOT / TEMP_DIRECTORY_NAME
OUTPUT_DIRECTORY = PROJECT_ROOT / OUTPUT_DIRECTORY_NAME

CONFIG_FILE = CONFIG_DIRECTORY / CONFIG_FILE_NAME
LOG_FILE = LOG_DIRECTORY / LOG_FILE_NAME


def create_required_directories() -> None:
    """Cria automaticamente os diretórios utilizados pela aplicação."""

    for directory in (
        CONFIG_DIRECTORY,
        LOG_DIRECTORY,
        TEMP_DIRECTORY,
        OUTPUT_DIRECTORY,
    ):
        directory.mkdir(parents=True, exist_ok=True)