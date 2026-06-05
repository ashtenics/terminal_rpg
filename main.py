import room
import ui
import data_manager
import merchant
from entities import Player


def main():
    print("Enter your characters name:")
    player_name = input("> ").strip()

    world_map = data_manager.load_data_file("world_map.json")
    shops = data_manager.load_data_file("shops.json")
    player = Player(player_name, 100, 10, 10, 100, 0, 100, "Town Square", 0)

    while True:

        room.display_info(world_map, player.location, player.level)

        player_input = input("What will you do? (Type a direction or 'inventory')\n> ").strip().lower()

        if player_input == "inventory":
            player.display_stats()

        elif player_input == "exit":
            break

        elif player_input in world_map[player.location]["exits"]:
            player.location = room.move(world_map, player.location, player.level, player_input)

        elif player_input in world_map[player.location].get("actions", {}):
            
            if player_input == "shop":
                current_shop = world_map[player.location]['actions']['shop']
                item_list = shops[current_shop]["inventory"]
                ui.display_shop_menu(player.location, item_list, player.gold)

                while True:
                    shop_choice = input("What would you like to buy? (Type an item name or 'inventory')\n> ").strip().lower()

                    if shop_choice == "inventory":
                        player.display_stats()

                    elif shop_choice in item_list:
                        if player.can_afford(item_list[shop_choice]["cost"]):
                            player.pay(item_list[shop_choice]["cost"])
                            player.receive_item(shop_choice)
                        else:
                            ui.print_alert("Not enought gold!")

                    elif shop_choice == "back":
                        break

                    else:
                        ui.print_alert("Item not found! Try again.")
                        continue


        else:
            ui.print_alert(f"Invalid command, direction, or action: '{player_input}'.")
    
    print("Loop successfully exited!")

main()
