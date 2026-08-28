from data.items import items
from data.attacks import attacks

class player:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.mana = 100
        self.max_mana = 100
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        self.level = 1
        self.max_level = 10
        self.xp = 0
        self.xp_to_next_level = 100
        self.inventory = {}
        self.equipment = {
            "weapon": None,
            "shield": None,
            "head": None,
            "chest": None,
            "arms": None,
            "legs": None,
            "feet": None,
        }
        self.list_attacks = []
        self.gold = 100
        self.local = "CIDADE"
        self.first_misson = True
        self.guild_first_misson = None
        
    def add_item(self, item):
        self.inventory[item] = self.inventory.get(item, 0) + 1
    
    def remove_item(self, item, quantidade_remover):
        if quantidade_remover > self.inventory.get(item, 0):
            print("Digite um valor válido igual ou menor ao que possui!")
        if quantidade_remover <= self.inventory.get(item, 0):
            self.inventory[item] -= quantidade_remover
            if self.inventory.get(item, 0) <= 0:
                del self.inventory[item]

    def equip_item(self, item):
        slot = items[item]["equip_type"]
        if self.equipment.get(slot) is not None:
            item_antigo = self.equipment[slot]
            self.inventory[item_antigo] = self.inventory.get(item_antigo, 0) + 1
            if items[item_antigo]["equip_type"] == "weapon":
                for attack in items[item_antigo]["attacks"]:
                    self.list_attacks.remove(attack)
        if self.inventory.get(item, 0) > 0:
            self.equipment[slot] = item
            self.remove_item(item, 1)
            if items[item]["equip_type"] == "weapon":
                for attack in items[item]["attacks"]:
                    self.lis_attacks.append(attack)


    def unequip_item(self, slot):
        item = self.equipment.get(slot)
        if self.equipment.get(slot) is not None:
            self.inventory[self.equipment[slot]] = self.inventory.get(self.equipment[slot], 0) + 1
            self.equipment[slot] = None
            if items[item]["equip_type"] == "weapon":
                for attack in items[item]["attacks"]:
                    self.attacks.remove(attack)


    def xp_gain(self, valor):
        self.xp += valor
        self.level_up()

    def level_up(self):
            while self.xp >= self.xp_to_next_level and self.level < self.max_level:
                self.level += 1
                self.xp_to_next_level *= 2

    def take_damage(self, damage):
        resistencia_total = 0
        for slot in ["head", "chest", "arms", "legs", "feet"]:
            item = self.equipment.get(slot)
            if item is not None:
                resistencia_total += items[item]["resistance"]
        dano_final = damage * (1 - resistencia_total)
        self.hp -= dano_final


    def calculate_damage(self, slot, ataque):
        item = self.equipment.get(slot)
        damage = (self.strength + items[item]["base_damage"]) * attacks[ataque]["multiplier"]
        return damage
