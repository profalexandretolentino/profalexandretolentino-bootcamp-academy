# ======================================
# ALTERAR CATEGORIA
# ======================================

def alterar_categoria():

    print(
        "\n===== ALTERAR CATEGORIA ====="
    )

    titulo = input(
        "Informe o filme: "
    )

    encontrado = False

    for filme in filmes:

        if (
            filme["titulo"].lower()
            ==
            titulo.lower()
        ):

            print(
                f"\nCategoria atual: "
                f"{filme['categoria']}"
            )

            nova_categoria = input(
                "Nova categoria: "
            )

            filme["categoria"] = nova_categoria

            print(
                "\nCategoria atualizada!"
            )

            encontrado = True

            break

    if not encontrado:

        print(
            "\nFilme não encontrado."
        )