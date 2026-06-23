# ======================================
# AVALIAR FILME
# ======================================

def avaliar_filme():

    print(
        "\n===== AVALIAR FILME ====="
    )

    titulo = input(
        "Informe o filme: "
    )

    for filme in filmes:

        if (
            filme["titulo"].lower()
            ==
            titulo.lower()
        ):

            print("\nEscolha:")

            print("1 - ⭐")
            print("2 - ⭐⭐")
            print("3 - ⭐⭐⭐")
            print("4 - ⭐⭐⭐⭐")
            print("5 - ⭐⭐⭐⭐⭐")

            opcao = input(
                "Avaliação: "
            )

            estrelas = {

                "1": "⭐",
                "2": "⭐⭐",
                "3": "⭐⭐⭐",
                "4": "⭐⭐⭐⭐",
                "5": "⭐⭐⭐⭐⭐"
            }

            if opcao in estrelas:

                filme["avaliacao"] = estrelas[opcao]

                print(
                    "\nAvaliação registrada!"
                )

            else:

                print(
                    "\nOpção inválida."
                )

            return

    print("\nFilme não encontrado.")

    #=================== Atualizar Listar Filmes
    
    def listar_filmes():

    print("\n===== CATÁLOGO =====")

    for filme in filmes:

        print("\n----------------")

        print(
            f"Título: "
            f"{filme['titulo']}"
        )

        print(
            f"Categoria: "
            f"{filme['categoria']}"
        )
        print(
            f"Avaliação: "
            f"{filme['avaliacao']}"
        )

        # Atualizar meno - print("5 - Avaliar Filme")

        #elif opcao == "5":
        #avaliar_filme()