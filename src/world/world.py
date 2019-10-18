import json
import os

import const
from hero.hero import Hero
from lib.log import log
from world.models import Room


class World:
    """
    Singleton for the game world
    """
    class SingleWorld:
        """
        Actual world object to which we defer all calls World calls
        """
        banner: str
        rooms: dict = {}
        hero_locations: dict = {}
        commands: list = []

        def __init__(self):
            self.banner = self._read_data(os.path.join(const.DATA_LOCATION, "banner.txt"), False)

            log("Reading zone information")
            self._read_zones()
            log(f"Loaded {len(self.rooms)} rooms")

        @staticmethod
        def _read_data(file_location: str, parse: bool = True):
            """
            Reads the given data file, returns the data
            """
            with open(file_location, "r") as infile:
                data = infile.read()
                return json.loads(data) if parse else data

        def _read_zones(self):
            """
            Reads each of the zone files, loading rooms into the world
            """
            for file in os.listdir(const.DATA_ZONES_LOCATION):
                full_path = os.path.join(const.DATA_ZONES_LOCATION, file)
                if not os.path.isfile(full_path) or not file.endswith(".json"):
                    continue

                # Cast data as a list to shut up IDE warnings, probably a good call to have it here anyway BUT just
                # don't be a dummy creating the data files and you're fine
                data = list(self._read_data(full_path))
                self.rooms.update({room["room_id"]: Room(**room) for room in data})

        def move_hero(self, hero: Hero, room_id: Room):
            # TODO: Handle invalid rooms I guess?
            if room_id in self.rooms:
                self.hero_locations[hero.name] = room_id

        def get_room(self, hero: Hero):
            room_id = self.hero_locations.get(hero.name, None)

            # If they haven't been assigned a location yet we recall them
            if not room_id:
                room_id = const.LOCATION_RECALL
                self.move_hero(hero, room_id)
            return self.rooms.get(room_id, None)

        def get_other_heroes_in_room(self, hero: Hero):
            room = self.get_room(hero)
            others = self.get_room_heroes(room.room_id)
            if hero.name in others:
                others.remove(hero.name)
            return others

        def get_room_heroes(self, room_id: str):
            return [key for key, value in self.hero_locations.items() if value == room_id]

        def tick(self):
            # TODO: Updates to the world per server tick. Includes combat, enemies moving, etc
            pass

    instance = None

    def __init__(self):
        # Initialize the singleton
        if not World.instance:
            World.instance = World.SingleWorld()

    def __getattr__(self, item):
        # Proxy attributes through to the singleton
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        # Proxy attributes through to the singleton
        return setattr(self.instance, key, value)
