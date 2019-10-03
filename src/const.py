"""
Contains configuration for the game
"""
import os

# Server settings
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1337
SERVER_NUM_CONNECTIONS = 50

# Data settings
DATA_LOCATION = "C:\\Users\\Stephen\\Documents\\GitHub\\pymud\\src\\data"
DATA_HEROES_LOCATION = os.path.join(DATA_LOCATION, "heroes")
