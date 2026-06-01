class LivingEntity():
    def __init__(self, name, damage, health, defence):
        self.name = name
        self.damage = damage
        self.health = health
        self.defence = defence
        self.spawn_chance = spawn_chance


class Player(LivingEntity):
    def __init__(self, name, health, damage, defence, gold=0):
        super().__init__(name, health, damage, defence)
        self.gold = gold
        self.inventory = []
        self.level = level


class Enemy(LivingEntity):
    def __init__(self, name, damage, health, defence, spawn_chance):
        super().__init__(name, damage, health, defence)
        self.spawn_chance = spawn_chance
