
import time
from entities import Player

def Elia_Chat(player):
    #dialogo se for a primeira missão
    if player.first_misson == True:
                print("Elia: Olá Aventureiro, vejo que é novo por aqui, vamos criar o seu registro!\n")
                time.sleep(2)
                player.first_misson = False
                print("Elia: pronto, registro criado!\n")
                time.sleep(2)
                print("Elia: Lhe daremos uma missão de registro! Você deve matar um goblin!\n")
                time.sleep(2)
                player.guild_first_misson = True

    #dialogo se ja tiver feito a primeira missão
    else:
        if player.guild_first_misson == True:
                    print("Elia: Aguardamos o fim de sua Missão!")
                    time.sleep(3)
        elif player.guild_first_misson == False and not player.guild_first_misson_completed:
                    print("Parabêns, aqui está seu pagamento!")
                    print(f"{player.name} recebeu 10 ouros")
                    player.gold += 10
                    time.sleep(3)
                    player.gold += 10
                    player.guild_first_misson_completed = True

def Torv_chat(player):
    if player.first_Torv_chat == True:
    # Diálogo inicial do armeiro Torv. Ele saúda o jogador e explica a função da loja.
        print("Torv: Ah, um novo explorador! Eu sou Torv, o armeiro desta cidade.\n")
        time.sleep(2)
        print("Torv: Aqui você encontra armas e armaduras para sobreviver aos perigos da floresta.\n")
        time.sleep(2)
        print(f"Torv: Seu ouro atual é {player.gold}. Se quiser, eu vendo equipamentos sob medida.\n")
        time.sleep(2)
        print("Torv: Se a sua bolsa estiver vazia, volte quando tiver mais moedas.\n")
        time.sleep(2)
        print("Torv: E lembre-se: armas aumentam seu ataque, armaduras reduzem o dano recebido.\n")
        player.first_Torv_chat = False
    else:
        print(f"Torv: Olá {player.name}, venho fazer mais compras hoje suponho! De uma boa olhada no arsenal!")