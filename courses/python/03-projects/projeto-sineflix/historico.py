# Histórico de visualizações
from filmes import filmes

historico = []

# ======================================
# ADICIONAR HISTÓRICO
# ======================================
def adicionar_historico():
    filme = input("Qual filme você assistiu? ").strip() # .strip() remove espaços extras inúteis

    # 1. Verifica se o filme existe no catálogo
    if filme not in filmes:
        print(f"Erro: O filme {filme} não existe no catálogo. Não é possível adicionar ao histórico.")
        return # Encerra a função mais cedo

    # 2. Verifica se o filme já foi assistido (evita duplicados no histórico, se desejar)
    if filme in historico:
        print(f"Você já informou que assistiu ao filme {filme} anteriormente.")
        return 

    # 3. Se passou pelas validações, adiciona ao histórico
    historico.append(filme)
    print(f"Sucesso: {filme} adicionado ao seu histórico de assistidos!")


# ======================================
# EXIBIR HISTÓRICO
# ======================================
def exibir_historico():

    if len(historico) == 0:
        print("Nenhum filme registrado.")
        return

    print("\n===== HISTÓRICO =====")

    for filme in historico:
        print(f"- {filme}")

    print(f"\nTotal assistido: {len(historico)}")

    # ======================================
# MENU HISTORICO
# ======================================
def menu_historico():

    while True:

        print("\n===== SINEFLIX - HISTÓRICO =====")
        print("1 - Exibir Historico")
        print("2 - Adicionar ao Histórico")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_historico()

        elif opcao == "2":
            adicionar_historico()

        elif opcao == "0":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")

