from dataclasses import dataclass, field


@dataclass
class Mob:
    """
    The base class for all mobs, including friendly ones
    """
    name: str = ""
    commands: list = field(default_factory=list)
    flags: list = field(default_factory=list)


@dataclass
class Room:
    room_id: str
    title: str
    description: str

    exits: dict = field(default_factory=dict)
    mobs: list = field(default_factory=list)
    flags: list = field(default_factory=list)

    def __post_init__(self):
        """
        Custom post-init work to nest dataclasses
        """
        mobs = [Mob(**m) for m in self.mobs]
        self.mobs = mobs

    def find_target(self, name: str):
        """
        Returns a Mob from the given name. Will attempt to match each word in the mob name, so when name is "dude" it'll
        match a Mob with name "Some Dude Bro". If no Mob exists that appears to match, returns None
        """
        if not name:
            return None

        for mob in self.mobs:
            tokens = mob.name.lower().split(" ")
            for token in tokens:
                if token.startswith(name.lower()):
                    return mob
        return None

    def look(self):
        return f"""{{green}}{self.title}{{normal}}
{self.description}
{{yellow}}[{', '.join(self.exits.keys())}]{{normal}}"""
