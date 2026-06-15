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
# ADICIONAR FILMES
# ======================================
def adicionar_filme():

    print("\n===== ADICIONAR FILME =====")

    novo_filme = input("Digite o nome do filme: ")

    # Verifica se o filme já existe
    if novo_filme in filmes:
        print("Filme já cadastrado.")

    else:
        filmes.append(novo_filme)
        print("Filme adicionado com sucesso!")

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

def menu_filmes():
    while True:  # Loop infinito — só sai quando o usuário escolher "0"
        print("\n===== SINEFLIX - CÁTALOGO =====")
        print("1 - Exibir catálogo")
        print("2 - Buscar filme")
        print("3 - Adicionar um novo filme ao catálogo")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        # Estrutura if/elif para direcionar para a função correta
        if opcao == "1":
            listar_filmes() 
        elif opcao == "2":
            buscar_filme()      
        elif opcao == "3":
            adicionar_filme()
        elif opcao == "0":
            print("\nVoltando ao menu principal...")
            break                    # Interrompe o while e sai do submenu
        else:
            print("\nOpção inválida! Tente novamente.")