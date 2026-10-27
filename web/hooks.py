"""Dodaje datoteke iz mape assets/ u izgrađenu web-stranicu.

Slike i drugi materijali ostaju na jednom mjestu u repozitoriju, a na stranici
su dostupni pod putanjom assets/, primjerice ![Opis](assets/slika.png) iz
seminar/index.md ili ![Opis](../assets/slika.png) iz seminar/postupci/.
"""

from pathlib import Path

from mkdocs.structure.files import File

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"


def on_files(files, config):
    for path in sorted(ASSETS_DIR.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            files.append(
                File(
                    path.relative_to(REPO_ROOT).as_posix(),
                    src_dir=str(REPO_ROOT),
                    dest_dir=config["site_dir"],
                    use_directory_urls=config["use_directory_urls"],
                )
            )
    return files
