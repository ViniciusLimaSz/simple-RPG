class enemy:
    def __init__(self, name, hp, max_hp, mana, max_mana, strength, intelligence, agility, resistence, level, xp_reward):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.max_mana = max_mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.resistence = resistence
        self.level = level
        self.xp_reward = xp_reward

    def take_damage(self, damage):
        self.hp -= damage

class goblin(enemy):
    def __init__(self):
        super().__init__(name="\033[0;32mGoblin\033[m",hp =30, max_hp=30, mana=0, max_mana=0, strength=2, intelligence=1, agility= 5, resistence = 0, level=1, xp_reward= 15)

class young_dragon(enemy):
    def __init__(self):
        super().__init__(name ="Dragão Jovem",hp =1000, max_hp=1000, mana=0, max_mana=0, strength=5, intelligence=3, agility= 5, resistence= 0.5, level=10, xp_reward= 250)

class ancient_red_dragon(enemy):
	def __init__(self):
		super().__init__(name="\033[0;31mDragão Vermelho Ancião\033[m", hp=10000, max_hp=10000,mana =10000, max_mana=10000, strength=100, intelligence=100, agility= 10, resistence=50, level=20, xp_reward= 10000)

class skeleton(enemy):
    def __init__(self):
        super().__init__(name="\033[0;34mSkeleton\033[m",hp =30, max_hp=30, mana=0, max_mana=0, strength=2, intelligence=1, agility= 5, resistence = 0, level=1, xp_reward= 15)
		
