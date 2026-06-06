import room
import ui
import data_manager
from entities import Player, Enemy
import random


def main():
    # menu screen, chraracter creation
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
    
    # loading data into file

    world_map = data_manager.load_data_file("data/world_map.json")
    shops = data_manager.load_data_file("data/shops.json")

    # safe zones

    safe_zones = ["Town Square", "Bazaar"]

    # main game loop

    while True:

        room.display_info(world_map, player.location, player.level, shops)

        player_input = input("What will you do? (Type a direction or 'inventory')\n> ").strip().lower()

        if player_input == "inventory":
            player.display_stats()

        elif player_input == "exit":
            save_data = player.get_player_save_data()
            data_manager.save_data_file("data/player_save_data.json", save_data)
            return

        # movement between locations

        elif player_input in world_map[player.location]["exits"]:
            player.location = room.move(world_map, player.location, player.level, player_input)

            # combat initiation

            enemy = Enemy("Slime", 50, 10, 5, 50, 0.4)

            roll = random.random()

            if player.location not in safe_zones:
                if roll <= enemy.spawn_chance:
                    print(f"\nA wild {enemy.name} jumps out of the shadows!")

                    while player.health and enemy.health > 0:
                        ui.display_combat_hud(player.name, player.health, player.max_health, enemy.name, enemy.health, enemy.max_health)
                        ui.display_combat_menu()
                        combat_input = input("> ").strip()
                        
                        if combat_input == "1":
                            enemy.take_damage(player.damage)
                            print(f"\nDealt {max(0, player.damage - enemy.defence)} to {enemy.name} enemy.")
                            player.take_damage(enemy.damage)
                            print(f"\nBut {enemy.name} fought back dealing {max(0, enemy.damage - player.defence)}")
                            player.gain_xp(10)
                            player.level_up()
                        
                        elif combat_input == "2":
                            print("\nFeature currently unavailable.")

                        elif combat_input == "3":
                            print(f"Player {player.name} flead the battle.")
                            break

                        else:
                            ui.print_alert("Command not found, please try again.")
                else:
                    print("\nThe room is quiet for now...")
            else:
                print("\nThis is a safe room.")

        # actions, shop

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
