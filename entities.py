class LivingEntity():
    def __init__(self, name, health, damage, defence, max_health):
        self.name = name
        self.damage = damage
        self.health = health
        self.defence = defence
        self.max_health = max_health


class Player(LivingEntity):

    def __init__(self, name, health, damage, defence, max_health, level, gold, location, xp, inventory):
        super().__init__(name, health, damage, defence, max_health)
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.xp = xp
        self.location = location


    def __str__(self):
        return {self.name}


    def take_damage(self, incoming_damage):
        final_damage = max(0, incoming_damage - self.defence)
        self.health -= final_damage
        print(f"Player {self.name} took {final_damage} damage.")
    
    def can_afford(self, amount):
        if self.gold >= amount:
            return True
        else:
            return False

    def pay(self, amount):
        self.gold -= amount

    def receive_item(self, item):
        self.inventory.append(item)

    def gain_xp(self, amount):
        self.xp += amount
        print(f"Gained {amount} XP!")
        if self.xp > 100:
            self.level_up()

    def level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.xp = 0
            self.max_health += 20
            self.health = self.max_health
            self.damage += 2
            self.defence += 5
            print(f"LEVEL UP! You are now level {self.level}, Max Health increased to {self.max_health}!")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"Healed for {amount}. Current Health: {self.health}")

    def display_stats(self):
        inv_items = ", ".join(self.inventory) if self.inventory else "Empty"
        
        print("\n┌──────────────────────────────────────────────────┐")
        print(f"│  PLAYER STATUS: {self.name.upper():<31} │")
        print("├──────────────────────────────────────────────────┤")
        print(f"│  Level: {self.level:<5} | XP: {self.xp:<5} | Location: {self.location:<13} │")
        print(f"│  Health: {self.health}/{self.max_health:<4} | Gold: {self.gold:<23} │")
        print(f"│  Inventory: {inv_items:<36} │")
        print("└──────────────────────────────────────────────────┘\n")

    def is_alive(self):
        return self.health > 0

    def get_player_save_data(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
            "defence": self.defence,
            "max_health": self.max_health,
            "level": self.level,
            "gold": self.gold,
            "location": self.location,
            "xp": self.xp,
            "inventory": self.inventory,
        }

    
class Enemy(LivingEntity):
    def __init__(self, name, health, damage, defence, max_health, spawn_chance):
        super().__init__(name, health, damage, defence, max_health)
        self.spawn_chance = spawn_chance

    def take_damage(self, amount):
        final_damage = max(0, amount - self.defence)
        self.health -= final_damage
        print(f"{self.name} took {final_damage} damage.")
