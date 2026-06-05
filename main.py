import room
import ui
import data_manager
from merchant import handle_purchase
from entities import Player


def main():
    print("Enter your characters name:")
    player_name = input("> ").strip()

    world_map = data_manager.load_data_file("world_map.json")
    player = Player(player_name, 100, 10, 10, 100, 0, 0, "Town Square", 0)

    while True:

        room.display_info(world_map, player.location, player.level)

        player_input = input("What will you do? (Type a direction or 'info')\n> ").strip().lower()

        if player_input == "info":
            player.display_stats()

        elif player_input == "exit":
            break

        elif player_input in world_map[player.location]["exits"]:
            player.location = room.move(world_map, player.location, player.level, player_input)

        elif player_input in world_map[player.location].get("actions", {}):
            print(f"Executing action: {player_input}")
        
        else:
            ui.print_alert(f"Invalid command, direction, or action: '{player_input}'.")

    
    print("Loop successfully exited!")

main()
