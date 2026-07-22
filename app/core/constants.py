"""Constantes globais utilizadas pelo ForgeDocs."""

from typing import Final

APP_NAME: Final[str] = "ForgeDocs"
APP_VERSION: Final[str] = "0.1.0-alpha"

DEFAULT_THEME: Final[str] = "dark"
DEFAULT_COLOR_THEME: Final[str] = "blue"

DEFAULT_WINDOW_WIDTH: Final[int] = 1280
DEFAULT_WINDOW_HEIGHT: Final[int] = 760

MIN_WINDOW_WIDTH: Final[int] = 1024
MIN_WINDOW_HEIGHT: Final[int] = 640

CONFIG_DIRECTORY_NAME: Final[str] = "config"
LOG_DIRECTORY_NAME: Final[str] = "logs"
TEMP_DIRECTORY_NAME: Final[str] = "temp"
OUTPUT_DIRECTORY_NAME: Final[str] = "output"

CONFIG_FILE_NAME: Final[str] = "settings.json"
LOG_FILE_NAME: Final[str] = "forgedocs.log"

SUPPORTED_DOCUMENT_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".txt",
        ".md",
    }
)

SUPPORTED_IMAGE_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".bmp",
        ".jpeg",
        ".jpg",
        ".png",
        ".tiff",
        ".webp",
    }
)

SUPPORTED_FILE_EXTENSIONS: Final[frozenset[str]] = (
    SUPPORTED_DOCUMENT_EXTENSIONS | SUPPORTED_IMAGE_EXTENSIONS
)