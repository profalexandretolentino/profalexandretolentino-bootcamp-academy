from filmes import filmes


# ======================================
# RANKING DE CATEGORIAS
# ======================================

def ranking_categorias():

    frequencias = {}

    # Percorre todos os filmes
    for filme in filmes:

        categoria = filme["categoria"]

        # Conta quantas vezes cada categoria aparece
        if categoria in frequencias:

            frequencias[categoria] += 1

        else:

            frequencias[categoria] = 1

    # Ordena do maior para o menor
    ranking = sorted(
        frequencias.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n===== RANKING DE CATEGORIAS =====")

    posicao = 1

    for categoria, quantidade in ranking:

        print(
            f"{posicao}º - "
            f"{categoria} "
            f"({quantidade} conteúdos)"
        )

        posicao += 1