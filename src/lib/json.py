import json
from enum import Enum


class EnumEncoder(json.Encoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return str(obj)
