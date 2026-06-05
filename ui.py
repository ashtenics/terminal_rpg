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

def display_shop_menu(shop_name, merchant_inv, player_gold):
    print("\n" + "═" * 60)
    print(f"🛒 {shop_name.upper():^54} 🛒")
    print("═" * 60)
    # Header Row
    print(f"  {'COMMAND':<15} {'ITEM NAME':<25} {'PRICE':<10}")
    print("─" * 60)
    
    # Item Rows
    for item_id, details in merchant_inv.items():
        cmd = f"[{item_id.upper()}]"
        name = details['display_name']
        cost = f"{details['cost']}g"
        print(f"  {cmd:<15} {name:<25} {cost:<10}")
        
    print("─" * 60)
    print(f"💰 Your Wallet: {player_gold} coins             [type 'back' to exit]")
    print("═" * 60)
