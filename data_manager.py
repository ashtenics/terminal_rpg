import os
import json


def load_game():
    if os.path.exists("player_state.json") and os.path.getsize("player_state.json") > 0:
        with open("player_state.json") as f:
            print("Successfuly loaded up your save data!")

            data = json.load(f)

            return data

    else:
        name = input("Enter your character name: ")

        return {
            "name": name,
            "health": 100,
            "mana": 50,
            "level": 0,
            "gold": 10,
            "inventory": {},
            "location": "Town Square",
            "position": [0, 0],
        }


def save_game(player_data):
    with open("player_state.json", "w") as f:
        json.dump(player_data, f, indent=4)
    print("Successfuly saved your current progress!")



def load_world_map(world_map_file):
    with open(world_map_file, "r") as f:
        world_map = json.load(f)
    return world_map
