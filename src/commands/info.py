"""
Contains commands for querying game related information
"""
from commands import BaseCommand
from colors import COLOR_MAP


class Colors(BaseCommand):
    commands = ["colors", "color"]

    @staticmethod
    def handle(args, client, server):
        result = "\n".join(["{" + key + "}" + key for key in COLOR_MAP.keys()])
        result += "{normal}"
        client.send(result)
