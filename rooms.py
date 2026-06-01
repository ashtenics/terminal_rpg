import json


def move(world, current_location, player_level):

    while True:

        print(f"[Current location: {current_location}], Player level: [{player_level}]\n")

        for direction, place in world[current_location]["exits"].items():
            level_req = world[place]['required_level']
            print(f"Go {direction} to reach {place}. Level required: [{level_req}]")

        print("\nSelect a direction to head to:")

        user_input = input("> ").strip()

        if user_input in world[current_location]["exits"]:
            desired_location = world[current_location]["exits"][user_input]

            if player_level >= world[desired_location]["required_level"]:

                current_location = desired_location
                return current_location

            else:
                print("\nPlayer level too low. Try again.\n")

        else:
            print("\nDirection not found. Try again.\n")


if __name__ == "__main__":
    with open("world_map.json", "r") as f:
        world_map = json.load(f)

    with open("player_state.json", "r") as f:
        player_data = json.load(f)

    player_data["location"] = move(world_map, player_data["location"], player_data["level"])
    
    with open("player_state.json", "w") as f:
        json.dump(player_data, f, indent=4)
