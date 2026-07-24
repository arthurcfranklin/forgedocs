"""Geração dos ícones PNG utilizados pela interface."""

from io import BytesIO
from pathlib import Path

import resvg_py
from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SVG_DIRECTORY = PROJECT_ROOT / "assets" / "icons" / "svg"
OUTPUT_DIRECTORY = PROJECT_ROOT / "assets" / "icons" / "generated"

ICON_SIZE = 48
ICON_COLOR = "#AAB7C8"


def colorize_png(
    png_bytes: bytes,
    color: str,
) -> Image.Image:
    """Aplica uma cor uniforme ao PNG preservando sua transparência."""

    image = Image.open(BytesIO(png_bytes)).convert("RGBA")
    alpha_channel = image.getchannel("A")

    colored_image = Image.new(
        mode="RGBA",
        size=image.size,
        color=color,
    )
    colored_image.putalpha(alpha_channel)

    return colored_image


def build_icons() -> None:
    """Converte e colore os ícones SVG do ForgeDocs."""

    if not SVG_DIRECTORY.exists():
        raise FileNotFoundError(
            f"Diretório de SVGs não encontrado: {SVG_DIRECTORY}"
        )

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    svg_files = sorted(SVG_DIRECTORY.glob("*.svg"))

    if not svg_files:
        print("Nenhum arquivo SVG encontrado.")
        return

    for svg_path in svg_files:
        output_path = OUTPUT_DIRECTORY / f"{svg_path.stem}.png"
        svg_content = svg_path.read_text(encoding="utf-8")

        png_bytes = resvg_py.svg_to_bytes(
            svg_string=svg_content,
            width=ICON_SIZE,
            height=ICON_SIZE,
        )

        colored_icon = colorize_png(
            png_bytes=png_bytes,
            color=ICON_COLOR,
        )
        colored_icon.save(
            output_path,
            format="PNG",
        )

        print(
            f"Gerado: {output_path.relative_to(PROJECT_ROOT)}"
        )

    print(
        f"\n{len(svg_files)} ícone(s) gerado(s) com sucesso."
    )


if __name__ == "__main__":
    build_icons()