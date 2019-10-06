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
            " a damn NERD"
        )
