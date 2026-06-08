# Lista de filmes disponíveis
filmes = [
    "Matrix",
    "Avatar",
    "Duna",
    "Interestelar",
    "Vingadores",
    "O Poderoso Chefão",
    "Clube da Luta",
    "Inception",
    "Pulp Fiction"
]

# ======================================
# LISTAR FILMES
# ======================================
def listar_filmes():

    print("\n===== CATÁLOGO =====")

    for indice, filme in enumerate(filmes, start=1):
        print(f"{indice} - {filme}")


# ======================================
# BUSCAR FILME
# ======================================
def buscar_filme():

    filme = input("Digite o nome do filme: ")

    if filme in filmes:
        print("Filme encontrado.")

    else:
        print("Filme não encontrado.")