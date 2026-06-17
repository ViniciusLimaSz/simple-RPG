
class Player:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.mana = 50
        self.max_mana = 50
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        
        self.level = 1
        self.max_level = 10
        self.xp = 0
        self.xp_to_next_level = 100
        self.inventory = {}
        self.equipment = {
            "weapons": None,
            "shield": None,
            "head": None,
            "chest": None,
            "arms": None,
            "legs": None,
            "feet": None,
        }
    
    def add_item(self, item):
        self.inventory[item] = self.inventory.get(item, 0) + 1

    def remove_item(self, item):
        if self.inventory.get(item) is not None:
            self.inventory[item] -= 1
        if self.inventory.get(item) == 0:
            del self.inventory[item]

    def equip_item(self, slot, item):
        if self.inventory.get(item, 0) > 0 and self.equipment.get(slot) is None:
            self.equipment[slot] = item
            self.remove_item()
        elif self.inventory[item] > 0 and self.equipment.get(slot) is not None:
            self.inventory[self.equipment[slot]] = self.inventory.get(self.equipment[slot], 0) + 1
            self.equipment[slot] = item
            self.remove_item()
        return

    def unequip_item(self, slot):
        if self.equipment.get(slot) is not None:
            self.inventory[self.equipment[slot]] = self.inventory.get(self.equipment[slot], 0) + 1
            self.equipment[slot] = None

    def xp_gain(self, valor):
        self.xp += valor
        self.level_up()

    def level_up(self):
            while self.xp >= self.xp_to_next_level and self.level < self.max_level:
                self.level += 1
                self.xp_to_next_level *= 2


