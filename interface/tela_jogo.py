from logic.combat import combat_display
from entities.Enemy import goblin, skeleton
from interface.npc_dialogs import Elia_Chat
import os
import sys
import time
import random
from entities.Player import player
from logic.combat import combat_display

def efeito_digitar(palavra):
    for n in palavra:
        print(n, end="", flush=True)
        time.sleep(0.2)

def clear_scream():
    os.system('cls' if os.name == 'nt' else 'clear')

def city_choices(player):
    escolha_cidade = input(
        "1 - Guilda\n"
        "2 - Armeiro Torv\n"
        "3 - Floresta\n"
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
        escolha_armeiro = input(
            "1 - Falar com o Armeiro Torv\n"
            "2 - Comprar com Torv\n"
            "3 - Voltar\n"
        )
        if escolha_armeiro == "1":
            print("Diálogo em construção..\n")
            time.sleep(3)
            clear_scream()
        elif escolha_armeiro == "2":
            print("Em construção..\n")
            time.sleep(3)
            clear_scream()
        elif escolha_armeiro == "3":
            player.local = "CIDADE"
            clear_scream()
        else:
            print("Digite algo válido\n")

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
            if player.guild_first_misson == True:
                print("\nvagando...")
                time.sleep(3)
                enemy = random.choice(goblin(), skeleton())
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
    print("= = = = = = = = = = = = ")

def TELA_JOGO(player):
    while True:
        print("= = = = ELDORIA = = = =\n"
        f"VOCÊ ESTÁ EM {player.local}\n"
        f"VIDA: \033[0;32m{player.hp}\033[m  -  OURO: \033[0;33m{player.gold}\033[m\n")
        display_mission(player)
        print("\nVOCÊ PODE:\n")
        options_menu(player)

      
def MENU_JOGO():
    print("---- RPG SIMPLES ----\n".upper)
    comeco_jogo = input("ESCOLHA:\n 1 - NOVO JOGO\n 2 - FECHAR \n")
    if comeco_jogo == "1":
        jogador = player()
        clear_scream()
        TELA_JOGO(jogador)
    elif comeco_jogo == "2":
        sys.exit()
    else:
        print("Inválido")



