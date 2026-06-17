# ======================================
# EX23
# Dados Discretos e Contínuos
# ======================================

def auditar_dados_usuario(usuario):

    print("\n===== AUDITORIA DE DADOS =====")

    print("\nIDADE")
    print("Tipo: Discreto")

    print("\nFILMES ASSISTIDOS")
    print("Tipo: Discreto")

    print("\nTEMPO ASSISTIDO")
    print("Tipo: Contínuo")

    print("\nValores encontrados:")

    print(f"Idade: {usuario['idade']}")

    print(
        f"Filmes Assistidos: "
        f"{usuario['filmes_assistidos']}"
    )

    print(
        f"Tempo Assistido: "
        f"{usuario['tempo_assistido']} horas"
    )