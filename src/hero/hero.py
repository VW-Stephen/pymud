import json
import os
from dataclasses import dataclass, field, asdict

import const
from hero.types import HeroType


@dataclass
class Hero:
    """
    User hero object
    """
    name: str = ""
    password: str = ""

    hero_class: HeroType = None
    level: int = 1

    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    flags: list = field(default_factory=list)

    @staticmethod
    def exists(name):
        return os.path.isfile(os.path.join(const.DATA_HEROES_LOCATION, name))

    def save(self):
        file_path = os.path.join(const.DATA_HEROES_LOCATION, self.name)
        with open(file_path, "w") as outfile:
            outfile.write(json.dumps(asdict(self)))

    @staticmethod
    def load(name):
        file_path = os.path.join(const.DATA_HEROES_LOCATION, name)
        with open(file_path, "r") as infile:
            data = json.loads(infile.read())
        return Hero(**data)
