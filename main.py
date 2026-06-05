import room
import ui
import data_manager
from entities import Player


def main():
    ui.display_title_menu()

    while True:
        choice = input("> ").strip()

        if choice == "1":
            ui.display_name_selection()
            player_name = input("> ").strip()
            player = Player(player_name, 100, 10, 10, 100, 0, 10, "Town Square", 0, [])
            break

        elif choice == "2":
            pd = data_manager.load_data_file("data/player_save_data.json")
            player = Player(
                pd["name"],
                pd["health"],
                pd["damage"],
                pd["defence"],
                pd["max_health"],
                pd["level"],
                pd["gold"],
                pd["location"],
                pd["xp"],
                pd["inventory"]
            )
            break

        elif choice == "3":
            print("\nGoodbye, adventurer!")
            return

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

    world_map = data_manager.load_data_file("data/world_map.json")
    shops = data_manager.load_data_file("data/shops.json")

    while True:

        room.display_info(world_map, player.location, player.level, shops)

        player_input = input("What will you do? (Type a direction or 'inventory')\n> ").strip().lower()

        if player_input == "inventory":
            player.display_stats()

        elif player_input == "exit":
            save_data = player.get_player_save_data()
            data_manager.save_data_file("data/player_save_data.json", save_data)
            return

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
                        chosen_item = item_list[shop_choice]
                        
                        if player.can_afford(chosen_item["cost"]):
                            player.pay(chosen_item["cost"])
                            player.receive_item(chosen_item["display_name"]) 
                            print(f"\nBought {chosen_item['display_name']}!")

                        else:
                            ui.print_alert("Not enough gold!")

                    elif shop_choice == "back":
                        break


        else:
            ui.print_alert(f"Invalid command, direction, or action: '{player_input}'.")

main()
