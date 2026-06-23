# ======================================
# SINEFLIX - FILMES (EX24 ATUALIZADO)
# ======================================

filmes = [
    {"titulo": "Matrix", "categoria": "Ficção", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Avatar", "categoria": "Ficção", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Duna", "categoria": "Ficção", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Interestelar", "categoria": "Ficção", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Inception", "categoria": "Ficção", "avaliacao": 0, "visualizacoes": 0},

    {"titulo": "Vingadores", "categoria": "Ação", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "John Wick", "categoria": "Ação", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Mad Max: Estrada da Fúria", "categoria": "Ação", "avaliacao": 0, "visualizacoes": 0},

    {"titulo": "O Poderoso Chefão", "categoria": "Drama", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Clube da Luta", "categoria": "Drama", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Forrest Gump", "categoria": "Drama", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "A Lista de Schindler", "categoria": "Drama", "avaliacao": 0, "visualizacoes": 0},

    {"titulo": "Pulp Fiction", "categoria": "Crime", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Os Suspeitos", "categoria": "Crime", "avaliacao": 0, "visualizacoes": 0},

    {"titulo": "Toy Story", "categoria": "Animação", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Shrek", "categoria": "Animação", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "Divertida Mente", "categoria": "Animação", "avaliacao": 0, "visualizacoes": 0},

    {"titulo": "Titanic", "categoria": "Romance", "avaliacao": 0, "visualizacoes": 0},
    {"titulo": "La La Land", "categoria": "Romance", "avaliacao": 0, "visualizacoes": 0}
]

# ======================================
# ADICIONAR FILME
# ======================================
def adicionar_filme():

    print("\n===== ADICIONAR FILME =====")

    titulo = input("Título do filme: ")
    categoria = input("Categoria do filme: ")

    # Verifica se já existe
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            print("\nFilme já cadastrado.")
            return

    novo_filme = {
        "titulo": titulo,
        "categoria": categoria,
        "visualizacoes": 0
    }

    filmes.append(novo_filme)

    print("\nFilme adicionado com sucesso!")

# ======================================
# LISTAR FILMES
# ======================================
def listar_filmes():

    print("\n===== CATÁLOGO =====")

    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
        return

    for filme in filmes:

        print("\n---------------------")
        print(f"Título: {filme['titulo']}")
        print(f"Categoria: {filme['categoria']}")
        print(f"Visualizações: {filme['visualizacoes']}")

# ======================================
# BUSCAR FILME
# ======================================
def buscar_filme():

    nome = input("Digite o nome do filme: ")

    encontrado = False

    for filme in filmes:

        if filme["titulo"].lower() == nome.lower():

            print("\n===== FILME ENCONTRADO =====")
            print(f"Título: {filme['titulo']}")
            print(f"Categoria: {filme['categoria']}")
            print(f"Visualizações: {filme['visualizacoes']}")

            encontrado = True
            break

    if not encontrado:
        print("\nFilme não encontrado.")

# ======================================
# MENU FILMES
# ======================================
def menu_filmes():

    while True:

        print("\n===== SINEFLIX - CATÁLOGO =====")
        print("1 - Exibir catálogo")
        print("2 - Buscar filme")
        print("3 - Adicionar filme")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_filmes()

        elif opcao == "2":
            buscar_filme()

        elif opcao == "3":
            adicionar_filme()

        elif opcao == "0":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")