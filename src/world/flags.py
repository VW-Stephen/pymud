from enum import Enum


class MobFlag(str, Enum):
    NO_ATTACK = "NO_ATTACK"  # Players can't attack the mob
    WANDERER = "WANDERER"  # Mob will wander the zone


class RoomFlag(str, Enum):
    """
    Flags that can be applied to rooms
    """
    NO_RECALL = "NO_RECALL"
