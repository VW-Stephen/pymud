import json


class World(object):
    """
    Singleton for the game world
    """
    class SingleWorld(object):
        """
        Actual world object to which we defer all calls World calls
        """
        state = ""

        def __init__(self):
            self._read_data(
                "hero_classes", "C:\\Users\\Stephen\\Documents\\GitHub\\pymud\\src\\world\\data\\classes.json"
            )
            self._read_data(
                "banner", "C:\\Users\\Stephen\\Documents\\GitHub\\pymud\\src\\world\\data\\banner.txt", False
            )

        def _read_data(self, member, file_location, parse=True):
            with open(file_location, "r") as infile:
                data = infile.read()
                if parse:
                    data = json.loads(data)
                self.__setattr__(member, data)

    instance = None

    def __init__(self):
        if not World.instance:
            World.instance = World.SingleWorld()

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
