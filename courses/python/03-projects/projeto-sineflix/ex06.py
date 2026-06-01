# Lista vazia para armazenar o histórico
historico = []

# Quantidade de filmes que serão adicionados
quantidade = int(input("Quantos filmes deseja registrar? "))

# Laço para cadastrar filmes
for i in range(quantidade):

    filme = input("Digite o nome do filme: ")

    historico.append(filme)

print("\n===== HISTÓRICO =====")

# Exibe todos os filmes registrados
for filme in historico:
    print(f"- {filme}")

# Mostra quantidade total
print(f"\nTotal de filmes assistidos: {len(historico)}")