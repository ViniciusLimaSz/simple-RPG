
class Potion:
    def __init__(self, restore_hp=0, restore_mana=0):
        self.restore_hp = restore_hp
        self.restore_mana = restore_mana

    def use(self, player):
        if self.restore_hp > 0:
            player.hp = min(player.max_hp, player.hp + self.restore_hp)
        if self.restore_mana > 0:
            player.mana = min(player.max_mana, player.mana + self.restore_mana)
        return True


class SmallHealingPotion(Potion):
    def __init__(self):
        super().__init__(restore_hp=10)


class HealingPotion(Potion):
    def __init__(self):
        super().__init__(restore_hp=30)


class GreatHealingPotion(Potion):
    def __init__(self):
        super().__init__(restore_hp=60)


class ManaPotion(Potion):
    def __init__(self):
        super().__init__(restore_mana=25)


class GreatManaPotion(Potion):
    def __init__(self):
        super().__init__(restore_mana=50)


potions = {
    "small_healing_potion": {
        "equip_type": "potion",
        "category": "healing",
        "name": "Poção Pequena de Cura",
        "cost": 10,
        "restore_hp": 10,
        "restore_mana": 0,
        "class": SmallHealingPotion,
    },
    "healing_potion": {
        "equip_type": "potion",
        "category": "healing",
        "name": "Poção de Cura",
        "cost": 25,
        "restore_hp": 30,
        "restore_mana": 0,
        "class": HealingPotion,
    },
    "great_healing_potion": {
        "equip_type": "potion",
        "category": "healing",
        "name": "Grande Poção de Cura",
        "cost": 45,
        "restore_hp": 60,
        "restore_mana": 0,
        "class": GreatHealingPotion,
    },
    "mana_potion": {
        "equip_type": "potion",
        "category": "mana",
        "name": "Poção de Mana",
        "cost": 20,
        "restore_hp": 0,
        "restore_mana": 25,
        "class": ManaPotion,
    },
    "great_mana_potion": {
        "equip_type": "potion",
        "category": "mana",
        "name": "Grande Poção de Mana",
        "cost": 40,
        "restore_hp": 0,
        "restore_mana": 50,
        "class": GreatManaPotion,
    },
}

