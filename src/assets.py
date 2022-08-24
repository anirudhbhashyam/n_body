from pathlib import Path

from dataclasses import dataclass, field
import pygame

@dataclass
class Assets:
    res_dir: Path
    images: dict[str, pygame.image] = field(default_factory = dict)

    def __post_init__(self) -> None:
        self._load()

    def _load(self) -> None:
        for filepath in Path.iterdir(self.res_dir.resolve()):
            name = filepath.name.split(".")[0]
            img = pygame.image.load(filepath).convert()
            self.images[name] = img