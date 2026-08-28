import time as t

def batle_menu():
    batle_menu_choices = input("1 - Atacar\n2 - Inventário\n3 - Fugir\n")
    if batle_menu_choices == "1":
        return
    elif batle_menu_choices == "2":
        return
    elif batle_menu_choices == "3":
        print("Player Fugiu!")
        t.sleep(2)
    else:
        "Digite algo válido"

def combat_display(player, enemy):
    contador_de_turno = 1
    print(f"UM {enemy.name} APARECEU!\n")
    t.sleep(1.5)
    while True:
        print(f"= = = = \033[1;33mTURNO {contador_de_turno}\033[m = = = =\n" f"    {enemy.hp}  X  {player.hp}\n")
        batle_menu()
        contador_de_turno += 1