class Enemy:
    def __init__(self, hp, max_hp, mana, max_mana, strength, intelligence, agility, level, xp_reward):
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.max_mana = max_mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.level = level
        self.xp_reward = xp_reward

class Goblin(Enemy):
    def __init__(self):
        super().__init__(hp =10, max_hp=10, mana=0, max_mana=0, strength=5, intelligence=3, agility= 5, level=1, xp_reward= 15)
