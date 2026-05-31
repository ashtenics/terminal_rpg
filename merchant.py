merchant_inventory = {
    "Health Potion": {"price": 10, "stock": 0},
    "Iron Sword": {"price": 50, "stock": 1},
    "Bread": {"price": 2, "stock": 20},
}

player_inventory = {}

coin_prompt = "How many coins do you have? "
coin_input = input(coin_prompt)
coins = int(coin_input)


def handle_purchase(coins_available, merchant_inv, player_inv):

    for item, details in merchant_inv.items():
        print(
            f"Check out this {item}!, it costs {details['price']} coins. "
            f"Only {details['stock']} unit(s) left"
        )

    print(
        f"\nWhat would you like to buy? "
        f"[available coins: {coins_available}]"
        )

    player_input = input("> ")

    if player_input in merchant_inv:
        item_data = merchant_inv[player_input]

        if item_data['stock'] > 0:

            if coins_available >= item_data['price']:
                print("Purchase successful!")
                coins_available -= item_data['price']
                item_data['stock'] -= 1

                if player_input in player_inv:
                    player_inv[player_input] += 1

                else:
                    player_inv[player_input] = 1

            else:
                print(
                    "Looks like you don't have "
                    "enough coins to buy this item."
                )

        else:
            print("I'm afraid that this item is out of stock.")

    else:
        print("This item doesn't exist.")

    return coins_available


coins = handle_purchase(coins, merchant_inventory, player_inventory)

print(f"Remaining funds: {coins}")
print(merchant_inventory)
print(player_inventory)
