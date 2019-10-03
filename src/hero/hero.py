import json
import os
from dataclasses import dataclass

import const


@dataclass
class Hero:
    """
    User hero object
    """
    name: str
    password: str

    @staticmethod
    def exists(name):
        return os.path.isfile(os.path.join(const.DATA_HEROES_LOCATION, name))

    def save(self):
        file_path = os.path.join(const.DATA_HEROES_LOCATION, self.name)
        with open(file_path, "w") as outfile:
            outfile.write(json.dumps(self))
