# filmes py
# filmes = []
# # ======================================
# ADICIONAR FILME
# ======================================

def adicionar_filme():

    titulo = input(
        "Título do filme: "
    )

    categoria = input(
        "Categoria do filme: "
    )

    filme = {
        "titulo": titulo,
        "categoria": categoria
    }

    filmes.append(filme)

    print("\nFilme cadastrado com sucesso!")


# ======================================
# LISTAR FILMES
# ======================================

def listar_filmes():

    print("\n===== CATÁLOGO =====")

    if len(filmes) == 0:

        print("Nenhum filme cadastrado.")
        return

    for filme in filmes:

        print(
            f"\nTítulo: "
            f"{filme['titulo']}"
        )

        print(
            f"Categoria: "
            f"{filme['categoria']}"
        )

# ======================================
# BUSCAR FILME
# ======================================

def buscar_filme():

    nome = input(
        "Digite o filme: "
    )

    encontrado = False

    for filme in filmes:

        if (
            filme["titulo"].lower()
            ==
            nome.lower()
        ):

            print("\nFilme encontrado!")

            print(
                f"Título: "
                f"{filme['titulo']}"
            )

            print(
                f"Categoria: "
                f"{filme['categoria']}"
            )

            encontrado = True

    if not encontrado:

        print("\nFilme não encontrado.")