import json
import os

import const


class World(object):
    """
    Singleton for the game world
    """
    class SingleWorld(object):
        """
        Actual world object to which we defer all calls World calls
        """
        def __init__(self):
            self._read_data("banner", os.path.join(const.DATA_LOCATION, "banner.txt"), False)

        def _read_data(self, member, file_location, parse=True):
            with open(file_location, "r") as infile:
                data = infile.read()
                if parse:
                    data = json.loads(data)
                self.__setattr__(member, data)

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
