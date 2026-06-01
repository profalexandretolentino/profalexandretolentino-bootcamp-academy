# Lista contendo os filmes cadastrados
filmes = [
    "Matrix",
    "Avatar",
    "Duna",
    "Interestelar",
    "Vingadores"
]

print("\n===== CATÁLOGO =====")

# Percorre a lista mostrando cada filme
for indice, filme in enumerate(filmes, start=1):
    print(f"{indice} - {filme}")