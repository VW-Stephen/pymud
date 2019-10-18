import random

import const
from commands import BaseCommand
from world.flags import RoomFlag


class Recall(BaseCommand):
    commands = ["recall", "recal"]

    @staticmethod
    def handle(args, client, server):
        # If the room is NO_RECALL then ignore the request
        room = server.world.get_room(client.hero)
        if RoomFlag.NO_RECALL in room.flags:
            client.send("You cannot recall from this location")
            return

        server.world.move_hero(client.hero, const.LOCATION_RECALL)
        room = server.world.get_room(client.hero)
        client.send(room.look())


class MoveMixin(object):
    responses = [
        "There's nothing that way, quit wasting my time",
        "Don't think you can move that way, champ...",
        "Not really an option from where you're standing, now is it?",
        "Nah there's nothing over there",
        "You can't go that way, so let's pretend you didn't even try"
    ]

    @staticmethod
    def do_move(direction, client, server):
        room = server.world.get_room(client.hero)
        if not room.exits.get(direction, None):
            client.send(random.choice(MoveMixin.responses))
            return

        server.world.move_hero(client.hero, room.exits[direction])
        room = server.world.get_room(client.hero)
        if room:
            client.run_command("look")


class North(BaseCommand):
    commands = ["north", "n"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("north", client, server)


class South(BaseCommand):
    commands = ["south", "s"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("south", client, server)


class East(BaseCommand):
    commands = ["east", "e"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("east", client, server)


class West(BaseCommand):
    commands = ["west", "w"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("west", client, server)


class Up(BaseCommand):
    commands = ["up", "u"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("up", client, server)


class Down(BaseCommand):
    commands = ["down", "d"]

    @staticmethod
    def handle(args, client, server):
        MoveMixin.do_move("down", client, server)
