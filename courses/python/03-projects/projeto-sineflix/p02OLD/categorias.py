# ======================================
# CATEGORIAS
# ======================================
def exibir_categorias():

    catalogo = {
        "Ação": ["Matrix", "Vingadores"],
        "Ficção": ["Avatar", "Duna"],
        "Drama": ["Interestelar"]
    }

    for categoria, lista_filmes in catalogo.items():

        print(f"\n{categoria}")

        for filme in lista_filmes:
            print(f"- {filme}")
