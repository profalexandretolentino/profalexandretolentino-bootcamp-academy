# ======================================
# EX22
# Variáveis Qualitativas e Quantitativas
# ======================================

def perfil_estatistico_usuario(usuario):

    print("\n===== PERFIL ESTATÍSTICO =====")

    print("\nVARIÁVEIS QUALITATIVAS")
    print("Nome")
    print("Cidade")
    print("Categoria Favorita")

    print("\nVARIÁVEIS QUANTITATIVAS")
    print("Idade")
    print("Filmes Assistidos")
    print("Tempo Assistido")

    print("\nDados do usuário:")

    print(f"Nome: {usuario['nome']}")
    print(f"Cidade: {usuario['cidade']}")
    print(
        f"Categoria Favorita: "
        f"{usuario['categoria_favorita']}"
    )

    print(f"Idade: {usuario['idade']}")

    print(
        f"Filmes Assistidos: "
        f"{usuario['filmes_assistidos']}"
    )

    print(
        f"Tempo Assistido: "
        f"{usuario['tempo_assistido']} horas"
    )