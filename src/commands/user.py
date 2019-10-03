from commands import BaseCommand
from hero.hero import Hero


class Login(BaseCommand):
    """
    Command for logging in to the game
    """
    commands = ["login"]

    @staticmethod
    def handle(args, client, server):
        # TODO: Improve this because it's dumb
        data = args.split(" ")
        if not len(data) == 2:
            client.send("Usage: login {yellow}<username> <password>{normal}")
            return

        client.login(Hero(name=data[0], password=data[1]))
        client.send("Welcome {red}" + data[0] + "{normal}")


class Character(BaseCommand):
    """
    Command for showing character info
    """
    commands = ["character", "char", "c"]

    @staticmethod
    def handle(args, client, server):
        client.send(client.hero.name)


class Who(BaseCommand):
    """
    Command for showing all users logged into the game
    """
    commands = ["who", "players"]

    @staticmethod
    def handle(args, client, server):
        names = []
        for c in server.client_pool:
            if c and c.hero:
                names.append(c.hero.name)

        client.send("\n".join(names))


class Create(BaseCommand):
    """
    Command for creating a new hero BRO
    """
    commands = ["create"]

    @staticmethod
    def handle(args, client, server):
        tokens = args.split(" ")
        if len(tokens) != 2:
            client.send("")
