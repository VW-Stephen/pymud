from dataclasses import dataclass, field


@dataclass
class Room:
    room_id: str
    title: str
    description: str
    exits: dict = field(default_factory=dict)
    mods: list = field(default_factory=list)

    heroes: list = field(default_factory=list)
    mobs: list = field(default_factory=list)
    flags: list = field(default_factory=list)

    def look(self):
        return f"""{{green}}{self.title}{{normal}}
{self.description}
{{yellow}}[{', '.join(self.exits.keys())}]{{normal}}"""


@dataclass
class Mob:
    """
    The base class for all mobs, including friendly ones
    """
    name: str
    commands: field(default_factory=list)
    flags: field(default_factory=list)
