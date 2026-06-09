# Dados do usuário
usuario = {}

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
