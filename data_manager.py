import json


def save_data_file(file_name, data_to_save):
    with open(file_name, "w") as f:
        json.dump(data_to_save, f, indent=4)
    print("Successfully saved data!")


def load_data_file(file_name):
    with open(file_name, "r") as f:
        loaded_file = json.load(f)
    return loaded_file
