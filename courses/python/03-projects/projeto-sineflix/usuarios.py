# Lista de usuários
usuarios = []

# ======================================
# CADASTRO DE USUÁRIO
# ======================================
def cadastrar_usuario():

    usuario = {}

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    usuario["nome"] = nome
    usuario["idade"] = idade
    usuario["cidade"] = cidade

    usuarios.append(usuario)

    print("\nUsuário cadastrado com sucesso!")

# ======================================
# EXIBIR USUÁRIOS
# ======================================
def exibir_usuario():

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for i in range(len(usuarios)):

        print(f"\n===== PERFIL {i + 1} =====")
        print(f"Nome: {usuarios[i]['nome']}")
        print(f"Idade: {usuarios[i]['idade']}")
        print(f"Cidade: {usuarios[i]['cidade']}")
        print()

    print(f"Total de Usuários: {len(usuarios)}")


# ======================================
# MENU USUÁRIOS
# ======================================
def menu_usuarios():
    while True:  # Loop infinito — só sai quando o usuário escolher "0"
        print("\n===== SINEFLIX - USUÁRIOS =====")
        print("1 - Cadastrar novo usuário")
        print("2 - Exibir Usuários")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        # Estrutura if/elif para direcionar para a função correta
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            exibir_usuario()
        elif opcao == "0":
            print("\nVoltando ao menu principal...")
            break                    # Interrompe o while e sai do submenu
        else:
            print("\nOpção inválida! Tente novamente.")