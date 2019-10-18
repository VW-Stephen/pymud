"""
Factory methods for handling commands from users.
"""

from commands import chat, info, movement, silly, user
from states import ClientState

"""
List of commands that are enabled, grouped by client state. To turn a command on, it must be in the list
"""
ENABLED_COMMANDS = {
    ClientState.PLAYING: [
        chat.Chat,
        chat.Say,
        chat.Whisper,

        info.Colors,
        info.Look,

        movement.Down,
        movement.East,
        movement.North,
        movement.Recall,
        movement.South,
        movement.Up,
        movement.West,

        silly.Fart,
        silly.Laugh,
        silly.Poke,

        user.Character,
        user.Save,
        user.Who
    ],
    ClientState.LOGGING_IN: [
        user.Login,
        user.Create
    ],
    ClientState.CREATING_HERO: [
        info.Look,

        user.Pray
    ]
}


def handle_command(message, client, server):
    """
    Handles the message from the given client

    Args:
        message: Full message received from the client
        client: Client thread that sent the message
        server: Global MUD server
    """
    tokens = message.split(" ")
    if not tokens:
        return

    command = tokens[0].lower()

    # Intercept custom commands here, stuff that's metadata on commands
    if command == "help":
        if len(tokens) == 1:
            info.Help.handle([], client, server)
            return

        for c in ENABLED_COMMANDS[client.state]:
            if tokens[1] in c.commands:
                c.help(tokens[1:], client)
                return

    # Iterate over the commands for the given state
    for c in ENABLED_COMMANDS[client.state]:
        if command in c.commands:
            args = tokens[1:] if len(tokens) > 1 else []
            c.handle(args, client, server)
            return

    client.send("Unknown command, see {yellow}commands{normal} for help")
