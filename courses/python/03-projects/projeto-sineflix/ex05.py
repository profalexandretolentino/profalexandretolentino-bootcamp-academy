# Dicionário contendo categorias e filmes
catalogo = {
    "Ação": ["Matrix", "Vingadores"],
    "Ficção": ["Avatar", "Duna"],
    "Drama": ["Interestelar"]
}

# Percorre o dicionário
for categoria, filmes in catalogo.items():

    print(f"\n{categoria}:")

    # Percorre a lista de filmes da categoria
    for filme in filmes:
        print(f"- {filme}")