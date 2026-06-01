def move(world, current_location, player_level):

    while True:

        print(f"[Current location: {current_location}], Player level: [{player_level}]\n")

        for direction, place in world[current_location]["exits"].items():
            target_room = world.get(place)
            if target_room:
                level_req = world[place]['required_level']
                print(f"Go {direction} to reach {place}. Level required: [{level_req}]")
            else:
                print(f"Go {direction} to reach {place}. (Warning: Room data missing!)")

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
