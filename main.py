from data import weapons

from entities.Enemy import goblin, young_dragon,ancient_red_dragon
from entities.Player import player

pl = player()

pl.add_item("iron_sword")
pl.equip_item("iron_sword")

print(pl.equipment)