from enum import Enum


class HeroType(str, Enum):
    Warrior = "Warrior"
    Mage = "Mage"


class GearSlot(str, Enum):
    Head = "Head"
    Body = "Body"
