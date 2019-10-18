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
        if len(args) == 0:
            client.send("Say what?")
            return

        recipients = server.world.get_other_heroes_in_room(client.hero)
        if len(recipients) == 0:
            client.send("Nobody hears you")
            return

        message = f"{client.hero.name} says: {' '.join(args)}"
        for r in recipients:
            server.send_hero(r, message)
        client.send(f"{{bright_black}}You say: {' '.join(args)}{{normal}}")


class Whisper(BaseCommand):
    commands = ["tell", "whisper"]

    @staticmethod
    def handle(args, client, server):
        if len(args) < 2:
            client.send("Who are you trying to whisper, and what are you saying?")
            return

        recipient = args[0]
        text = " ".join(args[1:])
        if client.hero.name == recipient:
            client.send("Talking to yourself? Ok fine...")

        result = server.send_hero(recipient, f"{{bright_magenta}}[W] from {client.hero.name} - {text}{{normal}}")
        if not result:
            client.send("Nobody hears you")
            return

        client.send(f"{{magenta}}[W] to {recipient} - {text}{{normal}}")


class Emote(BaseCommand):
    commands = ["emote"]

    @staticmethod
    def handle(args, client, server):
        if len(args) == 0:
            client.send("Emote what, exactly?")
            return
