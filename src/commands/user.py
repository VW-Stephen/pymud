from random import randint

import const
from commands import BaseCommand
from hero.hero import Hero
from hero.types import HeroType
from states import ClientState


class Character(BaseCommand):
    """
    Command for showing character info
    """
    commands = ["character", "char", "c"]

    @staticmethod
    def handle(args, client, server):
        client.send(f"""
{client.hero.name} - lvl {client.hero.level} {client.hero.hero_class}
  {{red}}STR{{normal}}: {client.hero.strength}
  {{red}}DEX{{normal}}: {client.hero.dexterity} 
  {{red}}INT{{normal}}: {client.hero.intelligence}
  {{red}}CON{{normal}}: {client.hero.constitution}
  {{red}}WIS{{normal}}: {client.hero.wisdom}
  {{red}}CHA{{normal}}: {client.hero.charisma}
""")


class Create(BaseCommand):
    """
    Command for creating a new hero BRO
    """
    commands = ["create"]

    @staticmethod
    def handle(args, client, server):
        if len(args) != 2:
            client.send("You should probably specify a username and password if you're creating a hero")
            return

        name = args[0]
        password = args[1]
        if Hero.exists(name):
            client.send("Someone with that name already exists, maybe you meant to {yellow}login{normal}?")
            return

        client.hero = Hero(name=name, password=password)
        client.send(f"{{red}}NOOB ALERT, NOOB ALERT{{normal}} {name} has entered the building")
        client.state = ClientState.CREATING_HERO


class Login(BaseCommand):
    """
    Command for logging in to the game
    """
    commands = ["login", "connect"]

    @staticmethod
    def handle(args, client, server):
        # TODO: Improve this because it's dumb
        if not len(args) == 2:
            client.send("Usage: login {yellow}<username> <password>{normal}")
            return

        name = args[0]
        password = args[1]

        hero = Hero.load(name)
        if hero.password == password:
            client.login(hero)
            client.send(f"Welcome back, {{red}}{name}{{normal}}")
            client.state = ClientState.PLAYING

            room = server.world.get_room(hero)
            client.send(room.look())
            return

        # Bad password dummy
        client.send("That password doesn't match what we have, you {red}dirty hackist{normal}!")

    @staticmethod
    def help(args, client):
        client.send("")


class Pray(BaseCommand):
    """
    Command for setting up a new hero after creation
    """
    commands = ["pray"]

    @staticmethod
    def handle(args, client, server):
        """
        Defers the given pray command to the correct handler
        """
        if not len(args):
            client.send("Pray for what, exactly?")
            return

        commands = {
            "ascension": Pray._handle_ascension,
            "ascend": Pray._handle_ascension,

            "attr": Pray._handle_attributes,
            "attributes": Pray._handle_attributes,

            "class": Pray._handle_class,

            "gear": Pray._handle_gear,
            "equipment": Pray._handle_gear
        }

        for c in commands.keys():
            if args[0] == c:
                commands[c](args[1:], client, server)
                return

        # Didn't match any of that stuff? Fail I guess
        client.send("Not sure what you want, maybe try {yellow}help pray{normal}?")

    @staticmethod
    def _handle_class(args, client, server):
        """
        Handles praying for a class

        Usage:
            pray class <classname>
        """
        class_options = ", ".join([f"{{yellow}}{t.name}{{normal}}" for t in HeroType])

        if not args:
            client.send(f"Which class are you praying for again? Maybe something like... {class_options}")
            return

        hero_class = args[0].lower()
        for ht in HeroType:
            if ht.name.lower() == hero_class:
                client.hero.hero_class = ht
                client.send(f"""Welcome, brave {ht.name}!
You can {{yellow}}pray class <name>{{normal}} to change class
Or {{yellow}}pray attributes{{normal}} to continue""")
                return

        # Not found SAD DAYS
        client.send(f"Maybe select a class that exists, dummy. Like... {class_options}")

    @staticmethod
    def _handle_attributes(args, client, server):
        """
        Handles praying for attributes
        """
        def roll():
            return randint(1, 6) + randint(1, 6) + 6

        client.hero.strength = roll()
        client.hero.dexterity = roll()
        client.hero.intelligence = roll()
        client.hero.wisdom = roll()
        client.hero.constitution = roll()
        client.hero.charisma = roll()

        client.send(f"""You have been granted the following attributes:
  {{red}}STR{{normal}}: {client.hero.strength}
  {{red}}DEX{{normal}}: {client.hero.dexterity}
  {{red}}INT{{normal}}: {client.hero.intelligence}
  {{red}}WIS{{normal}}: {client.hero.wisdom}
  {{red}}CON{{normal}}: {client.hero.constitution}
  {{red}}CHA{{normal}}: {client.hero.charisma}
  
If you're happy with those stats maybe it's time to {{yellow}}pray gear{{normal}} so you're not naked?""")

    @staticmethod
    def _handle_gear(args, client, server):
        """
        Handles the prayer for equipment, which is pretty neat
        """
        # TODO
        client.send("Yeah I'll do this later, maybe")

    @staticmethod
    def _handle_ascension(args, client, server):
        """
        Handles the ascension phase of praying, which finalizes the hero setup process
        """
        client.hero.save()
        client.send("Time to party BRO. Also time to change this message")  # TODO: Reword
        client.state = ClientState.PLAYING


class Save(BaseCommand):
    """
    Command for forcing a save on the server side
    """
    commands = ["save"]

    @staticmethod
    def handle(args, client, server):
        client.hero.save()
        client.send("{green}Saved{normal}")


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
