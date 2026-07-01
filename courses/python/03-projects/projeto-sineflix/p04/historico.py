from filmes import filmes
from series import series

historico = []


def adicionar_historico():
    nome = input("Qual conteúdo você assistiu? ").strip()

    for filme in filmes:
        if filme["titulo"].lower() == nome.lower():

            registro = {
                "tipo": "Filme",
                "titulo": filme["titulo"]
            }

            historico.append(registro)
            filme["visualizacoes"] += 1

            print(f"{filme['titulo']} adicionado ao histórico.")
            print("Visualização registrada automaticamente.")
            return

    for serie in series:
        if serie["titulo"].lower() == nome.lower():

            registro = {
                "tipo": "Série",
                "titulo": serie["titulo"]
            }

            historico.append(registro)
            serie["visualizacoes"] += 1

            print(f"{serie['titulo']} adicionada ao histórico.")
            print("Visualização registrada automaticamente.")
            return

    print(f"Erro: {nome} não existe no catálogo.")


def exibir_historico():

    if len(historico) == 0:
        print("Nenhum conteúdo registrado.")
        return

    print("\n===== HISTÓRICO =====")

    for item in historico:
        print(f"- [{item['tipo']}] {item['titulo']}")

    print(f"\nTotal assistido: {len(historico)}")


def menu_historico():

    while True:

        print("\n===== SINEFLIX - HISTÓRICO =====")
        print("1 - Exibir Histórico")
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