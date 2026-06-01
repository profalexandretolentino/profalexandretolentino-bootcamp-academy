# ======================================
# SINEFLIX - P1
# Primeira Entrega do Projeto
# ======================================

# Lista de filmes disponíveis
filmes = [
    "Matrix",
    "Avatar",
    "Duna",
    "Interestelar",
    "Vingadores"
]

# Histórico de visualizações
historico = []

# Dados do usuário
usuario = {}


# ======================================
# FUNÇÃO DE BOAS-VINDAS
# ======================================
def boas_vindas():

    print("=" * 40)
    print("         BEM-VINDO AO")
    print("           SINEFLIX")
    print("=" * 40)


# ======================================
# CADASTRO DE USUÁRIO
# ======================================
def cadastrar_usuario():

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    usuario["nome"] = nome
    usuario["idade"] = idade
    usuario["cidade"] = cidade

    print("\nUsuário cadastrado com sucesso!")


# ======================================
# EXIBIR PERFIL
# ======================================
def exibir_perfil():

    if len(usuario) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("\n===== PERFIL =====")

    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Cidade: {usuario['cidade']}")


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


# ======================================
# ADICIONAR HISTÓRICO
# ======================================
def adicionar_historico():

    filme = input("Qual filme você assistiu? ")

    historico.append(filme)

    print("Filme adicionado ao histórico.")


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
# CATEGORIAS
# ======================================
def exibir_categorias():

    catalogo = {
        "Ação": ["Matrix", "Vingadores"],
        "Ficção": ["Avatar", "Duna"],
        "Drama": ["Interestelar"]
    }

    for categoria, lista_filmes in catalogo.items():

        print(f"\n{categoria}")

        for filme in lista_filmes:
            print(f"- {filme}")


# ======================================
# MENU PRINCIPAL
# ======================================
def menu():

    while True:

        print("\n===== MENU SINEFLIX =====")

        print("1 - Cadastrar usuário")
        print("2 - Exibir perfil")
        print("3 - Catálogo")
        print("4 - Buscar filme")
        print("5 - Categorias")
        print("6 - Registrar filme assistido")
        print("7 - Histórico")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            exibir_perfil()

        elif opcao == "3":
            listar_filmes()

        elif opcao == "4":
            buscar_filme()

        elif opcao == "5":
            exibir_categorias()

        elif opcao == "6":
            adicionar_historico()

        elif opcao == "7":
            exibir_historico()

        elif opcao == "8":
            print("Obrigado por utilizar o SineFlix.")
            break

        else:
            print("Opção inválida.")


# ======================================
# PROGRAMA PRINCIPAL
# ======================================

boas_vindas()
menu()