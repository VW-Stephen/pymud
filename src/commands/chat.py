"""
Contains commands for communication
"""

from commands import BaseCommand


class Chat(BaseCommand):
    commands = ["chat", "ooc"]

    @staticmethod
    def handle(args, client, server):
        message = f"[CHAT] {client.hero.name} - {args}"
        server.send_all("{bright_blue}" + message + "{normal}")


class Say(BaseCommand):
    commands = ["say"]

    @staticmethod
    def handle(args, client, server):
        # TODO
        client.send("SAY")


class Whisper(BaseCommand):
    commands = ["tell", "whisper"]

    @staticmethod
    def handle(args, client, server):
        tokens = args.split(" ")
        if len(tokens) < 2:
            client.send("Who are you trying to whisper, and what are you saying?")

        recipient = tokens[0]
        text = " ".join(tokens[1:])
        if client.hero.name == recipient:
            client.send("Talking to yourself? Ok fine...")

        message = f"[W] from {client.hero.name} - {text}"
        result = server.send_hero(recipient, "{bright_magenta}" + message + "{normal}")
        if not result:
            client.send("Nobody hears you")
            return

        message = f"[W] to {recipient} - {text}"
        client.send("{magenta}" + message + "{normal}")
