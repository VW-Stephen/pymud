"""
Contains commands for querying game related information
"""
from commands import BaseCommand
from colors import COLOR_MAP


class Colors(BaseCommand):
    commands = ["colors", "color"]

    @staticmethod
    def handle(args, client, server):
        client.send(", ".join([f"{{key}}{key}{{normal}}" for key in COLOR_MAP.keys()]))


class Help(BaseCommand):
    commands = ["help"]

    @staticmethod
    def handle(args, client, server):
        client.send(
            "Shows helpful information about commands. Use {yellow}help <command>{normal} to read a bunch of stuff like"
            " a damn NERD, because that's just what you are. Give me your lunch money, NERD!"
        )


class Look(BaseCommand):
    commands = ["look", "l"]

    @staticmethod
    def handle(args, client, server):
        if len(args) == 0:
            Look._look_room(client, server)

    @staticmethod
    def _look_room(client, server):
        # Include the room messages
        room = server.world.get_room(client.hero)
        message = f"{room.look()}"

        # Show any other users in the room
        occupants = server.world.get_room_heroes(room.room_id)
        occupants.remove(client.hero.name)

        if occupants:
            message += "\n"
            for occupant in occupants:
                message += f"{{bright_blue}}{occupant}{{normal}}\n"
        client.send(message)
