import time as t
import os
from data.attacks import attacks
from data.potions import potions

def clear_scream():
    os.system('cls' if os.name == 'nt' else 'clear')

def potion_selection(player):
    available_potions = [
        item_key
        for item_key, quantity in player.inventory.items()
        if item_key in potions and quantity > 0
    ]

    if not available_potions:
        print("Você não possui poções.")
        return False

    while True:
        print("Escolha uma poção:")
        for position, potion_key in enumerate(available_potions, start=1):
            potion_name = potions[potion_key]["name"]
            quantity = player.inventory[potion_key]
            print(f"{position} - {potion_name} ({quantity})")
        print("0 - Voltar")

        try:
            choice = int(input("Selecione uma poção: "))
        except ValueError:
            print("Digite o número de uma opção válida!")
            continue

        if choice == 0:
            return False

        if choice < 1 or choice > len(available_potions):
            print("Digite o número de uma poção válida!")
            continue

        potion_key = available_potions[choice - 1]
        potions[potion_key]["class"]().use(player)
        player.remove_item(potion_key, 1)
        print(f"Você usou {potions[potion_key]['name']}.")
        return True

def attack_selection(player):
    if not player.list_attacks:
        print("Player não possui ataques disponíveis.")
        return None

    while True:
        for position, attack_key in enumerate(player.list_attacks, start=1):
            print(f"{position} - {attacks[attack_key]['name']}")

        try:
            choice = int(input("Selecione um ataque: "))
            attack_key = player.list_attacks[choice - 1]
        except (ValueError, IndexError):
            print("Digite o número de um ataque válido!")
            continue

        return attack_key

def combat_display(player, enemy):
    clear_scream()
    contador_de_turno = 1
    print(f"UM {enemy.name} APARECEU!\n")
    t.sleep(1.5)
    while player.hp > 0 and enemy.hp > 0:
            print(f"= = = = \033[1;33mTURNO {contador_de_turno}\033[m = = = =\n" f"{enemy.name} - {enemy.hp}  X  {player.hp} - Player\n")
            batle_menu_choices = input("1 - Atacar\n2 - Inventário (Poções)\n3 - Fugir\n")
            if batle_menu_choices == "1":
                print("Escolha seu ataque:\n")
                selected_attack = attack_selection(player)
                if selected_attack is None:
                    continue

                if player.agility >= enemy.agility:
                    first_attacker = player
                    second_attacker = enemy
                else:
                    first_attacker = enemy
                    second_attacker = player

                for attacker in [first_attacker, second_attacker]:
                    if attacker is player:
                        target = enemy
                    else:
                        target = player

                    if attacker.hp <= 0 or target.hp <= 0:
                        continue

                    if attacker is player:
                        damage = player.calculate_damage(selected_attack)
                        target.take_damage(damage)
                        print(f"Player usou {attacks[selected_attack]['name']} e causou {damage} de dano!")
                    else:
                        damage = enemy.strength
                        target.take_damage(damage)
                        print(f"{enemy.name} atacou e causou {damage} de dano!")
                    t.sleep(1)



            elif batle_menu_choices == "2":
                potion_selection(player)


            elif batle_menu_choices == "3":
                print("Player Fugiu!")
                t.sleep(1.5)
                clear_scream()
                break
            contador_de_turno += 1

    if player.hp <= 0:
        print("Player Derrotado!")
        t.sleep(1.5)
        clear_scream()
    elif enemy.hp <= 0:
        print(f"{enemy.name} derrotado! Player Venceu!")
        t.sleep(1.5)
        player.xp_gain(enemy.xp_reward)
        if player.guild_first_misson == True:
            player.guild_first_misson = False
        clear_scream()

        
