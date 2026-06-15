# ============================================================
# SINEFLIX - Sistema de Recomendações de Filmes
# Módulo utilizado: random (biblioteca padrão do Python)
# ============================================================
# O módulo random permite gerar valores aleatórios.
# Não precisa instalar nada — já vem com o Python!
# Basta importar com: import random
# ============================================================

import random  # Importa o módulo random da biblioteca padrão

# ------------------------------------------------------------
# CATÁLOGO DE FILMES
# Uma lista (list) com os filmes disponíveis na plataforma.
# É a base de dados que todas as funções vão utilizar importado
# do modulo filmes.
# ------------------------------------------------------------
from filmes import filmes

# ============================================================
# PARTE 1 - random.choice()
# ============================================================
# random.choice(sequência) escolhe UM elemento aleatório
# de qualquer sequência: lista, tupla ou string.
# Cada elemento tem a mesma probabilidade de ser escolhido.
# Exemplo: random.choice(["A", "B", "C"]) → pode retornar "A", "B" ou "C"
# ============================================================
def recomendacao_do_dia():
    print("\n===== RECOMENDAÇÃO DO DIA =====")

    # random.choice() recebe a lista e devolve um item aleatório
    filme_recomendado = random.choice(filmes)

    print(f"Filme recomendado: {filme_recomendado}")


# ============================================================
# PARTE 2 - random.randint()
# ============================================================
# random.randint(a, b) gera um número inteiro aleatório
# entre a e b, sendo que AMBOS OS EXTREMOS são incluídos.
# Exemplo: random.randint(1, 5) → pode gerar 1, 2, 3, 4 ou 5
# Diferente do range(), aqui o valor final (b) É incluído!
# ============================================================
def sortear_nota():
    print("\n===== NOTA DE RECOMENDAÇÃO =====")

    # randint(1, 5) garante uma nota entre 1 e 5 estrelas (inclusivo)
    nota = random.randint(1, 5)

    # Multiplica a string "⭐" pelo valor da nota para exibir visualmente
    # Exemplo: nota = 3 → "⭐" * 3 → "⭐⭐⭐"
    estrelas = "⭐" * nota

    print(f"`Nota sorteada: {nota} estrela(s) {estrelas}")


# ============================================================
# PARTE 3 - random.randrange()
# ============================================================
# random.randrange(stop) gera um inteiro aleatório de 0 até stop-1.
# Também aceita: random.randrange(start, stop, step)
# ATENÇÃO: o valor de stop NÃO é incluído (igual ao range())!
# Exemplo: random.randrange(5) → pode gerar 0, 1, 2, 3 ou 4
#
# Aqui usamos len(filmes) como stop para garantir que o índice
# gerado sempre seja válido para acessar um elemento da lista.
# ============================================================
def filme_por_posicao():
    print("\n===== FILME POR POSIÇÃO ALEATÓRIA =====")

    # len(filmes) retorna o tamanho da lista (ex: 8)
    # randrange(8) gera um índice entre 0 e 7 — todos válidos!
    posicao = random.randrange(len(filmes))

    # Usa o índice sorteado para acessar o filme na posição correspondente
    print(f"Filme sorteado da posição {posicao}: {filmes[posicao]}")


# ============================================================
# PARTE 4 - random.shuffle()
# ============================================================
# random.shuffle(lista) embaralha os elementos de uma lista
# de forma ALEATÓRIA e IN-PLACE — ou seja, modifica a própria
# lista passada como argumento, sem criar uma nova.
#
# IMPORTANTE: por isso usamos .copy() antes de embaralhar,
# para preservar o catálogo original intacto!
# Se passássemos o catálogo diretamente, ele seria alterado
# permanentemente e as outras funções seriam afetadas.
# ============================================================
def embaralhar_catalogo():
    print("\n===== CATÁLOGO ORIGINAL =====")

    # enumerate(lista, start=1) percorre a lista retornando
    # o índice e o valor de cada elemento. start=1 faz a
    # numeração começar em 1 (em vez do padrão 0).
    for i, filme in enumerate(filmes, start=1):
        print(f"{i} - {filme}")

    # .copy() cria uma cópia independente da lista original
    # Assim, o shuffle não vai alterar a variável 'filmes' original
    filmes_embaralhado = filmes.copy()

    # shuffle() embaralha a cópia in-place (sem retorno)
    # Após essa linha, catalogo_embaralhado estará em nova ordem
    random.shuffle(filmes_embaralhado)

    print("\n===== CATÁLOGO EMBARALHADO =====")
    for i, filme in enumerate(filmes_embaralhado, start=1):
        print(f"{i} - {filme}")


# ============================================================
# SUBMENU - Menu de Recomendações
# ============================================================
# Função responsável por exibir as opções de recomendação
# e chamar a função correspondente à escolha do usuário.
#
# O loop while True mantém o menu ativo até o usuário
# digitar "0" para voltar ao menu principal.
# ============================================================
def menu_recomendacoes():
    while True:  # Loop infinito — só sai quando o usuário escolher "0"
        print("\n===== SINEFLIX - RECOMENDAÇÕES =====")
        print("1 - Recomendação do dia")
        print("2 - Sortear nota de recomendação")
        print("3 - Filme por posição aleatória")
        print("4 - Embaralhar catálogo")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        # Estrutura if/elif para direcionar para a função correta
        if opcao == "1":
            recomendacao_do_dia()    # Chama a Parte 1 — random.choice()
        elif opcao == "2":
            sortear_nota()           # Chama a Parte 2 — random.randint()
        elif opcao == "3":
            filme_por_posicao()      # Chama a Parte 3 — random.randrange()
        elif opcao == "4":
            embaralhar_catalogo()    # Chama a Parte 4 — random.shuffle()
        elif opcao == "0":
            print("\nVoltando ao menu principal...")
            break                    # Interrompe o while e sai do submenu
        else:
            print("\nOpção inválida! Tente novamente.")