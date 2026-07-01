# Histórico de visualizações

from dados_historico import historico
from filmes import filmes
from series import series


# ======================================
# REGISTRAR HISTÓRICO
# ======================================
def registrar_historico(tipo, titulo):

    # Verifica se o conteúdo já existe no histórico
    for item in historico:

        if item["tipo"] == tipo and item["titulo"].lower() == titulo.lower():

            # Apenas incrementa a quantidade de visualizações
            item["vezes_assistido"] += 1
            return

    # Se ainda não existir, cria um novo registro
    historico.append({
        "tipo": tipo,
        "titulo": titulo,
        "vezes_assistido": 1
    })


# ======================================
# ADICIONAR HISTÓRICO MANUAL
# ======================================
def adicionar_historico():

    nome = input("Qual conteúdo você assistiu? ").strip()

    for filme in filmes:

        if filme["titulo"].lower() == nome.lower():

            filme["visualizacoes"] += 1
            registrar_historico("Filme", filme["titulo"])

            print(f"\n{filme['titulo']} assistido com sucesso!")
            return

    for serie in series:

        if serie["titulo"].lower() == nome.lower():

            serie["visualizacoes"] += 1
            registrar_historico("Série", serie["titulo"])

            print(f"\n{serie['titulo']} assistida com sucesso!")
            return

    print("\nConteúdo não encontrado no catálogo.")


# ======================================
# EXIBIR HISTÓRICO
# ======================================
def exibir_historico():

    if len(historico) == 0:
        print("\nNenhum conteúdo assistido.")
        return

    print("\n===== HISTÓRICO DE VISUALIZAÇÕES =====")

    for item in historico:

        print(
            f"[{item['tipo']}] "
            f"{item['titulo']} "
            f"({item['vezes_assistido']} visualização(ões))"
        )

    print(f"\nConteúdos diferentes assistidos: {len(historico)}")


# ======================================
# MENU HISTÓRICO
# ======================================
def menu_historico():

    while True:

        print("\n===== SINEFLIX - HISTÓRICO =====")
        print("1 - Exibir Histórico")
        print("2 - Registrar Conteúdo Assistido")
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