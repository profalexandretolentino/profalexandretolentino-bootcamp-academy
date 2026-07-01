from filmes import filmes
from series import series
from utilitarios import exibir_estrelas


def listar_catalogo_integrado():
    print("\n===== SINEFLIX - CATÁLOGO INTEGRADO =====")

    print("\n--- FILMES ---")
    for filme in filmes:
        print(f"[FILME] {filme['titulo']} | {filme['categoria']} | ⭐ {filme['avaliacao']} | 👁 {filme['visualizacoes']}")

    print("\n--- SÉRIES ---")
    for serie in series:
        print(f"[SÉRIE] {serie['titulo']} | {serie['categoria']} | {serie['temporadas']} temporada(s) | ⭐ {serie['avaliacao']} | 👁 {serie['visualizacoes']}")


def buscar_conteudo():
    nome = input("Digite o nome do conteúdo: ")

    for filme in filmes:
        if filme["titulo"].lower() == nome.lower():
            print("\n===== FILME ENCONTRADO =====")
            print(f"Título: {filme['titulo']}")
            print(f"Categoria: {filme['categoria']}")
            print(f"Avaliação: {filme['avaliacao']}")
            print(f"Visualizações: {filme['visualizacoes']}")
            return

    for serie in series:
        if serie["titulo"].lower() == nome.lower():
            print("\n===== SÉRIE ENCONTRADA =====")
            print(f"Título: {serie['titulo']}")
            print(f"Categoria: {serie['categoria']}")
            print(f"Temporadas: {serie['temporadas']}")
            print(f"Avaliação: {exibir_estrelas(filme['avaliacao'])}")
            print(f"Visualizações: {serie['visualizacoes']}")
            return

    print("Conteúdo não encontrado.")


def menu_catalogo():
    while True:
        print("\n===== SINEFLIX - CATÁLOGO INTEGRADO =====")
        print("1 - Listar catálogo integrado")
        print("2 - Buscar conteúdo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_catalogo_integrado()

        elif opcao == "2":
            buscar_conteudo()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")