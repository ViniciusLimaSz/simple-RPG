
class Potion:
    def use(self, player):
        pass

class SmallHealingPotion(Potion):
    def use(self, player):
        player.hp  += 10

class HealingPotion(Potion):
    def use(self,player):
        player.hp += 30

class GreatHealingPotion(Potion):
    def use(self, player):
        player.hp += 60

class ManaPotion(Potion):
    def use(self, player):
        player.mana += 25

class GreatManaPotion(Potion):
    def use(self, player):
        player.mana += 50

