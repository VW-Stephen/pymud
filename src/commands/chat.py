"""
Contains commands for communication
"""

from commands import BaseCommand


class Chat(BaseCommand):
    commands = ["chat", "ooc"]

    @staticmethod
    def handle(args, client, server):
        message = " ".join(args)
        server.send_all(f"{{bright_blue}}[CHAT] {client.hero.name} - {message}{{normal}}")


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
        if len(args) < 2:
            client.send("Who are you trying to whisper, and what are you saying?")

        recipient = args[0]
        text = " ".join(args[1:])
        if client.hero.name == recipient:
            client.send("Talking to yourself? Ok fine...")

        result = server.send_hero(recipient, f"{{bright_magenta}}[W] from {client.hero.name} - {text}{{normal}}")
        if not result:
            client.send("Nobody hears you")
            return

        client.send(f"{{magenta}}[W] to {recipient} - {text}{{normal}}")
