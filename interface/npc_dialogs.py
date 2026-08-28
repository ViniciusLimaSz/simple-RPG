
import time
from entities import Player

def Elia_Chat(player):
    #dialogo se for a primeira missão
    if player.first_misson == True:
                print("Elia: Olá Aventureiro, vejo que é novo por aqui, vamos criar o seu registro!\n")
                time.sleep(1.5)
                player.first_misson = False
                print("Elia: pronto, registro criado!\n")
                time.sleep(1.5)
                print("Elia: Lhe daremos uma missão de registro! Você deve matar um goblin!\n")
                time.sleep(1.5)
                player.guild_first_misson = True

    #dialogo se ja tiver feito a primeira missão
    else:
        if player.guild_first_misson == True:
                    print("Elia: Aguardamos o fim de sua Missão!")
                    time.sleep(3)
        elif player.guild_first_misson == False:
                    print("Parabêns, aqui está seu pagamento!")
                    time.sleep(3)
                    player.gold += 10
