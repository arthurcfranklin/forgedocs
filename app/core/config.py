"""Gerenciamento das configurações da aplicação."""

from __future__ import annotations

import json
from typing import Any

from app.core.paths import CONFIG_FILE, create_required_directories


DEFAULT_SETTINGS: dict[str, Any] = {
    "theme": "dark",
    "color_theme": "blue",
    "window_width": 1280,
    "window_height": 760,
}


def load_settings() -> dict[str, Any]:
    """Carrega as configurações da aplicação."""

    create_required_directories()

    if not CONFIG_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_settings(settings: dict[str, Any]) -> None:
    """Salva as configurações da aplicação."""

    create_required_directories()

    with CONFIG_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            settings,
            file,
            indent=4,
            ensure_ascii=False,
        )