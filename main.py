import os
import json
from data_manager import load_game, save_game
from merchant import handle_purchase, shop_room
from rooms import move


def main():
    player = load_game()

    while True:

