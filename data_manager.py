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


def save_data_file(file_name, data_to_save):
    with open(file_name, "w") as f:
        json.dump(data_to_save, f, indent=4)
    print("Successfully saved data!")


def load_data_file(file_name):
    with open(file_name, "r") as f:
        loaded_file = json.load(f)
    return loaded_file
