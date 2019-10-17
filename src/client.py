import socket
from threading import Thread

from colors import colorize
from commands.factory import handle_command
from log import log
from states import ClientState


class ClientThread(Thread):
    """
    Client connection thread that handles all their interaction with the world
    """
    def __init__(self, connection, address, server):
        super(ClientThread, self).__init__()

        # Network
        self.connection = connection
        self.address = address
        self.server = server

        # Game
        self.hero = None
        self.location = None
        self.state = ClientState.LOGGING_IN

    def run(self):
        """
        Main loop for the thread, handles messaging to/from the client
        """

        # Log in stuff
        self.send(self.server.world.banner)
        self.send("{yellow}connect <username> <password>{normal} for an existing hero")
        self.send("{yellow}create <username> <password>{normal} for a new hero")

        # Client game loop
        while True:
            # Socket mode is set to non-blocking here, so we have to catch timeout errors and handle them if/when
            try:
                data = self.receive()
            except socket.timeout:
                self.send("You seem distant, is there another woman? WHO IS THE BITCH?? (disconnected due to timeout)")
                self.exit()
                return

            if not data:
                continue

            log("Server - Received '{0}'".format(data))
            if data == "exit":
                self.exit()
                return

            handle_command(data, self, self.server)

    def login(self, hero):
        self.hero = hero
        self.state = ClientState.PLAYING

    def exit(self):
        if self.hero:
            self.hero.save()
        self.connection.close()
        exit(0)

    def receive(self):
        try:
            return str(self.connection.recv(1024), "ascii").strip()
        except BrokenPipeError:
            return None

    def send(self, message):
        try:
            message = colorize(str(message)) + "\n"
            self.connection.send(bytes(message, "ascii"))
        except BrokenPipeError:
            exit(0)
