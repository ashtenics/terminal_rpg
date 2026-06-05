def handle_purchase(player_gold, merchant_inv, desired_item):

    desired_item = desired_item.strip().lower()

    if desired_item in merchant_inv:
        return True


def shop_info(player_gold, merchant_inv):
    for item, details in merchant_inv.items():
        print(f"Check out this {details['display_name']}!, it costs {details['cost']} coins. ")

    print(
        f"\nWhat would you like to buy? "
        f"[available coins: {player_gold}]"
        )
