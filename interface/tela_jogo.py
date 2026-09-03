from logic.combat import combat_display
from entities.Enemy import goblin, skeleton
from interface.npc_dialogs import Elia_Chat, Torv_chat
from data.items import items
import os
import sys
import time
import random
from entities.Player import player
from logic.combat import combat_display
from interface.markets import comprar_com_torv

def efeito_digitar(palavra):
    for n in palavra:
        print(n, end="", flush=True)
        time.sleep(0.2)

def clear_scream():
    os.system('cls' if os.name == 'nt' else 'clear')

def inventory_and_equipment(player):
    # Um conjunto facilita verificar se o tipo do item pode ser equipado.
    tipos_equipamento = {"weapon", "shield", "head", "chest", "arms", "legs", "feet"}
    nomes_slots = {
        "weapon": "Arma",
        "shield": "Escudo",
        "head": "Cabeça",
        "chest": "Peito",
        "arms": "Braços",
        "legs": "Pernas",
        "feet": "Pés",
    }

    print("=== INVENTÁRIO ===")
    if player.inventory:
        for indice, (item_key, quantidade) in enumerate(player.inventory.items(), start=1):
            
            item_data = items.get(item_key, {})
            
            nome_item = item_data.get("name", item_key)
            print(f"{indice} - {nome_item} / {quantidade}")
    else:
        print("Inventário vazio")

    
    print("\n=== EQUIPAMENTOS ===")
    for slot, item_key in player.equipment.items():
        nome_item = items.get(item_key, {}).get("name", item_key) if item_key else "vazio"
        print(f"{nomes_slots.get(slot, slot)} / {nome_item}")

    
    itens_equipaveis = [
        item_key
        for item_key in player.inventory
        if items.get(item_key, {}).get("equip_type") in tipos_equipamento
    ]

    
    if not itens_equipaveis:
        input("\nPressione Enter para voltar...")
        return

    
    print("\nItens equipáveis:")
    for indice, item_key in enumerate(itens_equipaveis, start=1):
        print(f"{indice} - {items[item_key]['name']}")
    print("0 - Voltar")

    escolha = input("Escolha um item para equipar: ")
    if escolha == "0":
        return

    try:
        
        item_selecionado = itens_equipaveis[int(escolha) - 1]
    except (ValueError, IndexError):
        
        print("Digite uma opção válida.")
        time.sleep(1.5)
        return

    
    if player.equip_item(item_selecionado):
        print(f"{items[item_selecionado]['name']} equipado.")
    else:
        print(f"Você não possui {items[item_selecionado]['name']} no inventário.")

    print("\n=== INVENTÁRIO ATUALIZADO ===")
    if player.inventory:
        for item_key, quantidade in player.inventory.items():
            nome_item = items.get(item_key, {}).get("name", item_key)
            print(f"{nome_item} / {quantidade}")
    else:
        print("Inventário vazio")
    time.sleep(1.5)

def city_choices(player):
    escolha_cidade = input(
        "1 - Guilda\n"
        "2 - Armeiro Torv\n"
        "3 - Floresta\n"
        "0 - Inventário\n"
    )
    if escolha_cidade == "1":
        clear_scream()
        player.local = "GUILDA"

    elif escolha_cidade == "2":
        clear_scream()
        player.local = "ARMEIRO"

    elif escolha_cidade == "3":
        clear_scream()
        player.local = "FLORESTA"

    elif escolha_cidade == "0":
        clear_scream()
        inventory_and_equipment(player)
        clear_scream()


    else:
        print("Digite algo válido")

def guild_choices(player):
        escolha_guild = input(
            "1 - Falar com a Balconista Elia\n"
            "2 - Voltar\n"
        )
        if escolha_guild == "1":
            clear_scream()
            Elia_Chat(player)
            clear_scream()
        elif escolha_guild == "2":
            player.local = "CIDADE"
            clear_scream()
        else:
            print("Digite algo válido\n")

def gunsmith_choices(player):
    while True:
        escolha_armeiro = input(
            "1 - Falar com o Armeiro Torv\n"
            "2 - Comprar com Torv\n"
            "3 - Voltar\n"
        )

        if escolha_armeiro == "1":
            clear_scream()
            Torv_chat(player)
            time.sleep(2)
            clear_scream()
            break

        elif escolha_armeiro == "2":
            if comprar_com_torv(player, clear_scream):
                break

        elif escolha_armeiro == "3":
            player.local = "CIDADE"
            clear_scream()
            break
        else:
            print("Digite algo válido\n")
            time.sleep(1.2)
            clear_scream()

def forest_choices(player):
        escolha_forest = input(
            "1 - Explorar Floresta\n"
            "2 - Caçar\n"
            "3 - Voltar a cidade\n"
        )
        if escolha_forest == "1":
            print("Em construção..\n")
            time.sleep(3)
            clear_scream()
        elif escolha_forest == "2":
            if player.guild_first_misson == True:
                enemy = goblin()
                combat_display(player, enemy)
                return
            else:
                print("\nVagando...")
                time.sleep(3)
                enemy = random.choice([goblin(), skeleton()])
                combat_display(player, enemy)

        elif escolha_forest == "3":
            clear_scream()
            player.local = "CIDADE"
        else:
            print("Digite algo válido\n")

def options_menu(player):
        if player.local == "CIDADE":
            city_choices(player)
        elif player.local == "GUILDA":
            guild_choices(player)
        elif player.local == "ARMEIRO":
            gunsmith_choices(player)
        elif player.local == "FLORESTA":
            forest_choices(player)

def display_mission(player):
    print("= = Missões Ativas: = =\n")
    if player.first_misson == True:
        print("- Missão: Se registre na Guilda! \n")
    if player.guild_first_misson == True:
        print("- Vá para a floresta e mate um Golbin!\n")
    elif player.guild_first_misson == False and not player.guild_first_misson_completed:
        print("- Volte para a Guilda e fale com a Balconista Elia!\n")
    print("= = = = = = = = = = = = ")

def TELA_JOGO(player):
    while True:
        print("= = = = ELDORIA = = = =\n"
        f"{player.name} está em \033[0;33m{player.local}\033[m\n"
        f"VIDA: \033[0;32m{player.hp}\033[m  -  OURO: \033[0;33m{player.gold}\033[m\n")
        display_mission(player)
        print("\nVOCÊ PODE:\n")
        options_menu(player)

      
def MENU_JOGO():
    print("= = = = RPG - ELDORIA = = = =")
    comeco_jogo = input("ESCOLHA:\n 1 - NOVO JOGO\n 2 - FECHAR \n")
    if comeco_jogo == "1":
        jogador = player()
        clear_scream()
        input_name = str(input("Digite seu nome jogador: "))
        jogador.name = f"\033[0;35m{input_name}\033[m"
        TELA_JOGO(jogador)
    elif comeco_jogo == "2":
        sys.exit()
    else:
        print("Inválido")



