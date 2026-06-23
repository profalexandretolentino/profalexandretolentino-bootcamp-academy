from filmes import filmes

# ======================================
# EXIBIR CATEGORIAS
# ======================================

def exibir_categorias():

    categorias = set()

    for filme in filmes:
        categorias.add(filme["categoria"])

    print("\n===== CATEGORIAS =====")

    for categoria in categorias:
        print(categoria)


# ======================================
# FILMES POR CATEGORIA
# ======================================

def filmes_por_categoria():

    categoria = input("Informe a categoria: ")

    print(f"\n===== {categoria.upper()} =====")

    encontrou = False

    for filme in filmes:

        if filme["categoria"].lower() == categoria.lower():

            print(f"- {filme['titulo']}")
            encontrou = True

    if not encontrou:
        print("Nenhum filme encontrado.")


# ======================================
# RESUMO + RANKING (NOVO DIFERENCIAL)
# ======================================

def resumo_categorias():

    resumo = {}

    for filme in filmes:

        cat = filme["categoria"]

        if cat in resumo:
            resumo[cat] += 1
        else:
            resumo[cat] = 1

    print("\n===== RESUMO =====")

    # ranking (MAIS IMPORTANTE NOVO)
    ranking = sorted(
        resumo.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for categoria, qtd in ranking:
        print(f"{categoria}: {qtd} filmes")

    print("\n===== RANKING DE POPULARIDADE =====")

    for i, (cat, qtd) in enumerate(ranking, start=1):
        print(f"{i}º {cat} ({qtd})")


# ======================================
# ANALYTICS DATA EXPORT
# ======================================

def obter_frequencia_categorias():

    frequencias = {}

    for filme in filmes:

        cat = filme["categoria"]

        frequencias[cat] = frequencias.get(cat, 0) + 1

    return frequencias

# ======================================
# MENU CATEGORIAS
# ======================================
def menu_categorias():

    while True:

        print("\n===== SINEFLIX - CATEGORIAS =====")
        print("1 - Exibir categorias")
        print("2 - Filmes por categorias")
        print("3 - Resumo das categorias")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_categorias()

        elif opcao == "2":
            filmes_por_categoria()

        elif opcao == "3":
            resumo_categorias()

        elif opcao == "0":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")