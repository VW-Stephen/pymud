import json
from enum import Enum


class EnumEncoder(json.Encoder):
    @staticmethod
    def default(obj: object):
        if isinstance(obj, Enum):
            return str(obj)
