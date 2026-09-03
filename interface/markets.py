from data.items import items
import time


def comprar_com_torv(player, clear_screen):
    itens_loja = []
    for item_key, item_data in items.items():
        if item_data.get("equip_type") in {"weapon", "head", "chest", "arms", "legs", "feet"}:
            itens_loja.append((item_key, item_data))

    print("\n=== LOJA DE TORV ===")
    for indice, (item_key, item_data) in enumerate(itens_loja, start=1):
        print(f"{indice} - {item_data['name']} | {item_data.get('cost', 0)} ouro | {item_data.get('equip_type')}")
    print("0 - Voltar para a cidade\n")

    opcao_compra = input("Escolha o número do item para comprar: ")

    if opcao_compra == "0":
        player.local = "CIDADE"
        clear_screen()
        return True

    try:
        indice = int(opcao_compra) - 1
        if indice < 0 or indice >= len(itens_loja):
            print("Digite um número válido.\n")
            time.sleep(1.5)
            return False

        item_key, item_data = itens_loja[indice]
        preco = item_data.get("cost", 0)

        if player.gold < preco:
            print(f"Torv: Você não tem ouro suficiente para comprar {item_data['name']}.\n")
            time.sleep(2)
            clear_screen()
            return False

        player.gold -= preco
        player.add_item(item_key)
        print(f"Torv: Excelente escolha! Você comprou {item_data['name']} por {preco} ouro.\n")
        time.sleep(2)
        clear_screen()
    except ValueError:
        print("Digite um número válido.\n")
        time.sleep(1.5)
        clear_screen()

    return False
