# ======================================
# SINEFLIX - CATÁLOGO DE FILMES
# ======================================

from utilitarios import exibir_estrelas

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

    # Evita duplicidade
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            print("\nFilme já cadastrado.")
            return

    novo_filme = {
        "titulo": titulo,
        "categoria": categoria,
        "avaliacao": 0,
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
        print(f"Avaliação: {exibir_estrelas(filme['avaliacao'])}")
        print(f"Visualizações: {filme['visualizacoes']}")


# ======================================
# BUSCAR FILME
# ======================================
def buscar_filme():

    nome = input("Digite o nome do filme: ")

    for filme in filmes:

        if filme["titulo"].lower() == nome.lower():

            print("\n===== FILME ENCONTRADO =====")
            print(f"Título: {filme['titulo']}")
            print(f"Categoria: {filme['categoria']}")
            print(f"Avaliação: {exibir_estrelas(filme['avaliacao'])}")
            print(f"Visualizações: {filme['visualizacoes']}")
            return

    print("\nFilme não encontrado.")


# ======================================
# AVALIAR FILME
# ======================================
def avaliar_filme():
    nome = input("Digite o nome do filme: ")

    for filme in filmes:
        if filme["titulo"].lower() == nome.lower():

            print(f"\nFilme encontrado: {filme['titulo']}")
            print("\nEscolha a avaliação:")
            print("1 - ⭐")
            print("2 - ⭐⭐")
            print("3 - ⭐⭐⭐")
            print("4 - ⭐⭐⭐⭐")
            print("5 - ⭐⭐⭐⭐⭐")

            nota = int(input("Avaliação: "))

            if nota < 1 or nota > 5:
                print("Avaliação inválida. Escolha uma nota de 1 a 5.")
                return

            filme["avaliacao"] = nota
            print("Avaliação registrada com sucesso!")
            return

    print("Filme não encontrado.")

# ======================================
# ASSISTIR FILME
# ======================================

def assistir_filme():
    nome = input("Digite o nome do filme assistido: ")

    for filme in filmes:
        if filme["titulo"].lower() == nome.lower():
            filme["visualizacoes"] += 1
            print("Visualização registrada com sucesso!")
            return

    print("Filme não encontrado.")


# ======================================
# EXIBIR ESTRELAS FILME
# ======================================
def exibir_estrelas(avaliacao):
    if avaliacao == 0:
        return "Sem avaliação"

    return "⭐" * avaliacao


# ======================================
# MENU DE FILMES
# ======================================
def menu_filmes():

    while True:

        print("\n===== SINEFLIX - CATÁLOGO =====")
        print("1 - Exibir catálogo")
        print("2 - Buscar filme")
        print("3 - Adicionar filme")
        print("4 - Avaliar filme")
        print("5 - Assistir filme")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_filmes()

        elif opcao == "2":
            buscar_filme()

        elif opcao == "3":
            adicionar_filme()

        elif opcao == "4":
            avaliar_filme()

        elif opcao == "5":
            assistir_filme()

        elif opcao == "0":
            print("\nVoltando ao menu principal...")
            break

        else:
            print("\nOpção inválida!")