# Exercício 39
# Criar uma matriz 3x3 contendo números inteiros.
# Depois, percorrer a matriz e mostrar os valores organizados na tela.

# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Percorre as linhas da matriz
for linha in matriz:

    # Percorre os elementos de cada linha
    for valor in linha:

        # Exibe o valor na mesma linha
        print(valor, end=" ")

    # Quebra de linha ao final de cada linha da matriz
    print()