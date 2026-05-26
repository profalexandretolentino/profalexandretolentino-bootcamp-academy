# Exercício 44
# Caça ao Tesouro com Matriz Bidimensional
#
# Requisitos:
# - Utilizar matriz bidimensional
# - Utilizar funções
# - Utilizar procedimentos
# - Mostrar o tabuleiro

# -----------------------------
# Função para criar o tabuleiro
# -----------------------------
def criarTabuleiro():
    return [
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"]
    ]

# -----------------------------------
# Procedimento para mostrar o tabuleiro
# -----------------------------------
def mostrarTabuleiro(tabuleiro):
    for linha in tabuleiro:
        for coluna in linha:
            print(coluna, end=" ")
        print()

# -----------------------------------------
# Função para verificar se acertou o tesouro
# -----------------------------------------
def verificarTesouro(linhaJogador, colunaJogador, linhaTesouro, colunaTesouro):
    return linhaJogador == linhaTesouro and colunaJogador == colunaTesouro

# ====================
# Programa principal
# ====================

# Cria o tabuleiro
tabuleiro = criarTabuleiro()

# Posição do tesouro (escondida)
linhaTesouro = 2
colunaTesouro = 2

# Solicita a tentativa do jogador
linhaJogador = int(input("Digite a linha (0 a 4): "))
colunaJogador = int(input("Digite a coluna (0 a 4): "))

# Marca a tentativa no tabuleiro
tabuleiro[linhaJogador][colunaJogador] = "X"

# Mostra o tabuleiro
print("\nTabuleiro:")
mostrarTabuleiro(tabuleiro)

# Verifica resultado
if verificarTesouro(
    linhaJogador,
    colunaJogador,
    linhaTesouro,
    colunaTesouro
):
    print("\nTesouro encontrado!")
else:
    print("\nÁgua!")