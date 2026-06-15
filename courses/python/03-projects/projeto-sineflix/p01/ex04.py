# Lista de filmes
filmes = [
    "Matrix",
    "Avatar",
    "Duna",
    "Interestelar",
    "Vingadores"
]

# Solicita o filme desejado
busca = input("Digite o nome do filme: ")

# Verifica se existe no catálogo
if busca in filmes:
    print("Filme encontrado no catálogo.")
else:
    print("Filme não encontrado.")