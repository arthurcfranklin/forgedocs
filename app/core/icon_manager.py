"""Gerenciamento centralizado dos ícones da aplicação."""

from __future__ import annotations

from functools import cache

import customtkinter as ctk
from PIL import Image

from app.core.paths import GENERATED_ICONS_DIRECTORY


class IconManager:
    """Carrega e mantém em cache os ícones utilizados pela interface."""

    DEFAULT_SIZE: tuple[int, int] = (18, 18)

    @classmethod
    @cache
    def load(
        cls,
        name: str,
        size: tuple[int, int] | None = None,
    ) -> ctk.CTkImage:
        """Retorna um ícone carregado e armazenado em cache."""

        icon_size = size or cls.DEFAULT_SIZE
        icon_path = GENERATED_ICONS_DIRECTORY / f"{name}.png"

        if not icon_path.exists():
            raise FileNotFoundError(
                f"Ícone não encontrado: {icon_path}"
            )

        image = Image.open(icon_path)

        return ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=icon_size,
        )
    