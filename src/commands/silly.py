import random

from commands import BaseCommand


class _SillyCommand(BaseCommand):
    no_args: str
    no_target: str

    @staticmethod
    def _send(client, message):
        if isinstance(message, list):
            client.send(random.choice(message))
        else:
            client.send(message)

    @classmethod
    def handle(cls, args, client, server):
        # No target
        if len(args) == 0:
            cls._send(cls.no_args)
            return

        # Room based targets
        room = server.world.get_room(client.hero)
        target = room.find_target(args[0])
        if not target:
            cls._send(cls.no_target)
            return

        # Check each command in the command list to see if the target has a corresponding command that matches it.
        # If it does we accept the first one (please don't match more than one when creating mobs!) and return the
        # result
        for command in cls.commands:
            if command in target.commands:
                client.send(target.commands[command])
                return

        # No target? Fail
        client.send(cls.no_target)


class Clap(_SillyCommand):
    commands = ["clap"]
    no_args = [
        "You start clapping at nothing",
        "You have so much clap they should call it applause. BURN!",
    ]
    no_target = "You can't find anything to clap for"


class Fart(_SillyCommand):
    commands = ["fart"]
    no_args = [
        "You quietly crop dust the area",
        "Silent but deadly, your fart almost suffocates you",
        "Your butt-trumpet plays a lovely tune",
        "You fart in your own general direction",
        "You trusted that fart, gambled, and lost. Time to change your undies",
        "You fart on yourself, probably for the heat"
    ]
    no_target = "What are you trying to fart on? Why do I even have to ask?"


class Laugh(_SillyCommand):
    commands = ["laugh"]
    no_args = [
        "You laugh like a maniac",
        "You chuckle about a joke you heard earlier",
        ""
    ]
    no_target = "What are you laughing at, chump?"


class Poke(_SillyCommand):
    commands = ["poke"]
    no_args = "You poke yourself, HOT"
    no_target = "You can't poke that (that's what she said!)"
