import time

def efeito_digitar(palavra):
    for n in palavra:
        print(n, end="", flush=True)
        time.sleep(0.2)

lista = {
    "iron_sword": {
        "quantidade" : 1,
        "name" : "Espada de ferro"
    },
    "iron_helmet": {
        "quantidade" : 1,
        "name" : "Elmo de ferro"
    },
    "iron_shield": {
        "quantidade" : 1,
        "name" : "Escudo de ferro"
    },
    "iron_boots": {
        "quantidade" : 1,
        "name" : "Botas de ferro"
    },
}
print("Inventário:")
for p, i in enumerate(lista, start=1):
    print(p, f"- {lista[i]["name"]}: {lista[i]["quantidade"]}", flush=True)
    time.sleep(0.2)

chave = list(lista.keys())
seleção_item = int(input(""))
item_celecionado = chave[seleção_item - 1]
print(f"{lista[item_celecionado]["name"]}")

def seleção_inventario_batle(player):
    for position, item in enumerate(player.inventory, start=1):
        print(position, f"{player.inventory[item]["name"]}: {player.inventory[item]["quantidade"]}", flush=True)
        time.sleep(0.2)
    chave = list(player.inventory.keys())
    seleção_item = int(input(""))
    item_celecionado = chave[seleção_item - 1]
    print(f"{player.inventory[item_celecionado]["name"]}")
