
def combat(player, enemy):
    contador_de_turno = 1
    print(f"Um \033[1;32m{enemy.name}\033[m apareceu!\n")
    batalhar_ou_Fugir = int(input(
        "1 - Batalhar\n"
        "2 - Fugir\n"
        "\n"
        ""))
    if batalhar_ou_Fugir == 1:
        while True:
            print(f"==== \033[1;33mTURNO {contador_de_turno}\033[m ====\n"
            f"{enemy.hp}      {player.hp}")
            atacar_ou_inventario = int(input("\n"
            "1 - ATACAR\n"
            "2 - INVENTÁRIO\n"
            "\n"
            ""))
            contador_de_turno += 1

            if atacar_ou_inventario == 1:
                
                if player.hp <= 0 or enemy.hp <= 0:
                    break

    else:
        print("Fugiu")

def calculate_damage(self):
    return