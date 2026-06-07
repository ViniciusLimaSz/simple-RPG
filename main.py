
# LOCAIS
mapa = {
    "cidade": {
        "descricao": "Uma cidade antiga.",
        "saidas": {
            "norte": "floresta",
            "sul": "deserto"
            }
        }
    }

#Itens
armas = {
    "espadas": {
        "espada_aco": {
            "dano": 20,
            "nome": "Espada de Aço Puro",
            "tipo_dano": ["cortante", "perfurante"]
        },
        "espada_ferro": {
            "dano": 10,
            "nome": "Espada de Ferro",
            "tipo_dano": ["cortante", "perfurante"]
        }
    },
    "armaduras": {
        "armadura_ferro": {
            "defesa_base": 10,
            "nome": "Armadura de Ferro",
            "resistencias": {
                "cortante": 0.7,
                "perfurante": 0.5,
            }
        }
    }
}

entidades = {
    "jogador": {
        "nome": "Herói",
        "nivel": 1,
        "hp": 100,
        "hp_max": 100,
        "stamina": 50,
        "stamina_max": 50,
        "ataque": 10,
        "defesa": 5,
        "velocidade": 5,
        "experiencia": 0,
        "xp_proximo_nivel": 100
    }
}


