from data.items import items
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
        item_info = player.inventory[item]

        print(
            position,
            f'{item_info["name"]}: {item_info["quantidade"]}',
            flush=True
        )

        time.sleep(0.2)

    chaves = list(player.inventory.keys())

    seleção_item = int(input("Selecione um item: "))

    item_selecionado = chaves[seleção_item - 1]

    print(player.inventory[item_selecionado]["name"])
