import json
from pathlib import Path

from dataclasses import dataclass

@dataclass
class Config:
    """
    General configuration parser class.
    """
    directory: Path
    filenames: list[str]

    def __read_file(self, filename: str):
        """
        Reads a single configuration file and yields a dictionary.
        """
        with Path(self.directory, filename).open("r") as f:
           yield json.load(f)
    
    def load(self) -> dict[str, str]:
        """
        Reads all files and yields dictionaries.
        """
        for file in self.filenames:
            yield from self.__read_file(file)

    