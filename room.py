import ui


def move(world, current_location, player_level, chosen_direction):

    desired_location_name = world[current_location]["exits"][chosen_direction]

    target_room_data = world[desired_location_name]

    if player_level >= target_room_data['required_level']:
        ui.print_travel_message(desired_location_name)
        return desired_location_name

    else:
        ui.print_alert("Player level too low to enter that area")
        return current_location


def display_info(world, current_location, player_level, shops_data):
    print(f"\n  📍 Current Location: {current_location}")
    print("  🚪 Available Exits:")
    
    for direction, place in world[current_location]["exits"].items():
        level_req = world[place]['required_level']
        if player_level < level_req:
            lock_status = f"🔒 (Requires Lvl {level_req})"
        else:
            lock_status = "✅"  
        print(f"     • [{direction.upper()}] -> {place} {lock_status}")

    room_actions = world[current_location].get("actions", {})
    if room_actions:
        print("  ✨ Local Actions:")
        for command, action_target in room_actions.items():
            # If the action is a shop, look up its real name in shops.json
            if command == "shop" and action_target in shops_data:
                clean_description = shops_data[action_target]["shop_name"]
            else:
                clean_description = action_target
                
            print(f"     • [{command.upper()}] -> {clean_description}")

    print()
