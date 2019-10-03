"""
Factory methods for handling commands from users.
"""

from commands import chat, info, user
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

        user.Character,
        user.Who
    ],
    ClientState.LOGGING_IN: [
        user.Login
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
    args = " ".join(tokens[1:])

    # Iterate over the commands for the given state
    for c in ENABLED_COMMANDS[client.state]:
        if command in c.commands:
            c.handle(args, client, server)
            return

    client.send("Unknown command, see {yellow}commands{normal} for help")
