# Exercício 38
# Crie dois vetores:
# - Um com nomes dos produtos
# - Outro com o preço unitário de cada produto
#
# Peça ao usuário para informar o nome de um produto
# e a quantidade vendida.
# Calcule e exiba o valor total da venda.

# Vetor com os nomes dos produtos
produtos = ["Mouse", "Teclado", "Monitor", "Impressora"]

# Vetor com os preços dos produtos
precos = [50.00, 120.00, 900.00, 450.00]

# Solicita o nome do produto
nome_produto = input("Digite o nome do produto: ")

# Verifica se o produto existe no vetor
if nome_produto in produtos:

    # Localiza a posição do produto no vetor
    pos = produtos.index(nome_produto)

    # Solicita a quantidade vendida
    quantidade = int(input("Digite a quantidade vendida: "))

    # Calcula o valor total da venda
    total = precos[pos] * quantidade

    # Exibe o resultado formatado com duas casas decimais
    print(f"Total da venda: R$ {total:.2f}")

else:
    print("Produto não encontrado!")