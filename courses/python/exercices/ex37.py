# Exercício 37
# Crie dois vetores:
# - Um com nomes de produtos
# - Outro com a quantidade em estoque de cada produto
#
# Peça ao usuário o nome de um produto e a quantidade vendida.
# Atualize o estoque e exiba o valor restante.

# Vetor com os nomes dos produtos
vetor_nomes = ["Mouse", "Teclado", "Monitor", "Impressora"]

# Vetor com as quantidades em estoque
estoque = [15, 10, 8, 5]

# Solicita ao usuário o nome do produto
produto = input("Digite o nome do produto vendido: ")

# Verifica se o produto existe no vetor
if produto in vetor_nomes:

    # Localiza a posição do produto no vetor
    pos = vetor_nomes.index(produto)

    # Solicita a quantidade vendida
    quantidade = int(input("Digite a quantidade vendida: "))

    # Verifica se há estoque suficiente
    if quantidade <= estoque[pos]:

        # Atualiza o estoque
        estoque[pos] -= quantidade

        # Exibe o estoque restante
        print(f"Estoque restante de {produto}: {estoque[pos]} unidades")

    else:
        print("Quantidade maior que o estoque disponível!")

else:
    print("Produto não encontrado!")