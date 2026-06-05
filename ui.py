def print_header(title):
    text = f" {title.upper()} "
    print("\n" + "=" * 50)
    print(f"{text:=^50}")
    print("=" * 50 + "\n")


def print_alert(message):
    print("\n" + "!" * 50)
    print(f" ALERT: {message} ")
    print("!" * 50 + "\n")


def get_user_choice(prompt_text="What will you do?"):
    print("━" * 40)
    choice = input(f" {prompt_text}\n ❯ ").strip().lower()
    print("━" * 40)
    return choice


def print_travel_message(destination):
    print(f"\n ➔ Entering: [ {destination.upper()} ]")
    print(" ──────────────────────────────────────────────────")


def print_shop_greeting(shop_name, greeting):
    print("\n┌" + "─" * 58 + "┐")
    print(f"│ {shop_name.upper():^56} │")
    print("└" + "─" * 58 + "┘")
    print(f"  📖 {greeting}")
    print("─" * 60 + "\n")


def display_shop_menu(location_name, item_list, player_gold):
    print("\n🛒 " + "═" * 56 + " 🛒")
    print(f"  {location_name.upper()} SHOPPING DISTANCE")
    print(f"  Your Wallet: {player_gold} Gold")
    print("═" * 62)
    
    for item_id, item_data in item_list.items():
        name = item_data["display_name"]
        cost = item_data["cost"]
        print(f"  [{item_id}] {name:<30} Cost: {cost:<5} Gold")
        
    print("─" * 62)
    print("  Type the item NUMBER to buy, or 'back' to leave.")
    print("─" * 62)


def display_combat_hud(player_name, p_hp, p_max_hp, enemy_name, e_hp, e_max_hp):
    # Calculate health bar lengths (10 blocks max)
    p_bar_count = int((p_hp / p_max_hp) * 10) if p_hp > 0 else 0
    p_bar = "█" * p_bar_count + "░" * (10 - p_bar_count)
    
    e_bar_count = int((e_hp / e_max_hp) * 10) if e_hp > 0 else 0
    e_bar = "█" * e_bar_count + "░" * (10 - e_bar_count)
    
    # Format Strings
    p_status = f"{player_name.upper()} [{p_hp}/{p_max_hp}]"
    e_status = f"[{e_hp}/{e_max_hp}] {enemy_name.upper()}"
    
    print("\n⚔️ " + "═" * 56 + " ⚔️")
    # Print the name headers aligned to the sides
    print(f"  {p_status:<25} VS {e_status:>27}")
    # Print the physical health bars
    print(f"  HP: [{p_bar}]" + " " * 22 + f"HP: [{e_bar}]")
    print("═" * 62)


def display_combat_menu():
    print("┌" + "─" * 60 + "┐")
    print(f"│  {'[1] ATTACK':<28}{'[2] USE ITEM':<30} │")
    print(f"│  {'[3] FLEE':<28}{'':<30} │")
    print("└" + "─" * 60 + "┘")


def print_combat_log(message):
    print(f"  💥 {message}")


def display_title_menu():
    print("\n" + "═" * 62)
    print(f"{'⚡ THE FORGOTTEN DUNGEONS ⚡':^62}")
    print("═" * 62 + "\n")
    
    print(f"{'╔' + '═' * 30 + '╗':^62}")
    print(f"{'║  [1] START NEW GAME          ║':^62}")
    print(f"{'║  [2] LOAD SAVED GAME         ║':^62}")
    print(f"{'║  [3] EXIT GAME               ║':^62}")
    print(f"{'╚' + '═' * 30 + '╝':^62}\n")
    
    print("─" * 62)
    print(f"{'Select an option (1-3)':^62}")
    print("─" * 62)


def display_name_selection():
    print("\n" + "═" * 62)
    print(f"{'⚔️  CHARACTER CREATION  ⚔️':^62}")
    print("═" * 62 + "\n")
    
    print(f"{'Before you step into the dark...':^62}")
    print(f"{'What is your adventurers name? ':^62}\n")
    print("─" * 62)
