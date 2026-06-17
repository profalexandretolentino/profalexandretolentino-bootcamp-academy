#from filmes import filmes

# # ======================================
# EXIBIR CATEGORIAS
# ======================================

def exibir_categorias():

    categorias = set()

    for filme in filmes:

        categorias.add(
            filme["categoria"]
        )

    print("\n===== CATEGORIAS =====")

    for categoria in categorias:

        print(categoria)

# ======================================
# FILMES POR CATEGORIA
# ======================================

def filmes_por_categoria():

    categoria = input(
        "Informe a categoria: "
    )

    print(
        f"\n===== {categoria.upper()} ====="
    )

    for filme in filmes:

        if (
            filme["categoria"].lower()
            ==
            categoria.lower()
        ):

            print(
                filme["titulo"]
            )

# ======================================
# RESUMO DE CATEGORIAS
# ======================================

def resumo_categorias():

    resumo = {}

    for filme in filmes:

        categoria = filme["categoria"]

        if categoria in resumo:

            resumo[categoria] += 1

        else:

            resumo[categoria] = 1

    print("\n===== RESUMO =====")

    for categoria, quantidade in resumo.items():

        print(
            f"{categoria}: "
            f"{quantidade} filme(s)"
        )

# ======================================
# DADOS PARA ANALYTICS
# ======================================

def obter_frequencia_categorias():

    frequencias = {}

    for filme in filmes:

        categoria = filme["categoria"]

        if categoria in frequencias:

            frequencias[categoria] += 1

        else:

            frequencias[categoria] = 1

    return frequencias

