"""
Contains everything needed to bring up a MUD server and handle client threads
"""
import socket

import const
from client import ClientThread
from log import log
from world.world import World


class MUDServer(object):
    client_pool = []
    socket_server = None
    world = None

    def __init__(self):
        log("Building world...")
        self.world = World()

        log("Initializing server...")
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind((const.SERVER_HOST, const.SERVER_PORT))
        self.socket_server.listen(const.SERVER_NUM_CONNECTIONS)

        log("Server's listening!")

    def serve(self):
        while True:
            connection, address = self.socket_server.accept()
            log(f"Server - {address} connected")

            thread = ClientThread(connection, address, self)
            self.client_pool.append(thread)
            thread.start()

    def send_all(self, message):
        for c in self.client_pool:
            try:
                c.send(message)
            except ConnectionAbortedError:
                self.client_pool.remove(c)
                log(f"Attempted to send_all to an expired client {c}")

    def send_hero(self, hero_name, message):
        for c in self.client_pool:
            if c.hero and c.hero.name == hero_name:
                c.send(message)
                return True
        return False


mud_server = MUDServer()
mud_server.serve()
