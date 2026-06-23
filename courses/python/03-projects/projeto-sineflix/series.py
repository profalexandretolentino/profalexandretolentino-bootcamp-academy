series = [
    {"titulo": "Dark","categoria": "Ficção","temporadas": 3,"avaliacao": 0,"visualizacoes": 0}
]

# ======================================
# ADICIONAR SÉRIE
# ======================================
def adicionar_serie():

    print("\n===== ADICIONAR SERIE =====")

    titulo = input("Título da série: ")
    categoria = input("Categoria da série: ")
    temporadas = input("Quantidade de Temporadas da série: ")

    # Verifica se já existe
    for serie in series:
        if serie["titulo"].lower() == titulo.lower():
            print("\nSerie já cadastrada.")
            return

    nova_serie = {
        "titulo": titulo,
        "categoria": categoria,
        "temporadas": temporadas,
        "avaliacao": 0,
        "visualizacoes": 0
    }

    series.append(nova_serie)

    print("\nSerie adicionada com sucesso!")

# ======================================
# LISTAR SERIES
# ======================================
def listar_series():

    print("\n===== SÉRIES =====")

    if len(series) == 0:
        print("Nenhuma série cadastrada.")
        return

    for serie in series:

        print("\n---------------------")
        print(f"Título: {serie['titulo']}")
        print(f"Categoria: {serie['categoria']}")
        print(f"Temporadas: {serie['temporadas']}")
        print(f"Avaliações: {serie['avaliacao']}")
        print(f"Visualizações: {serie['visualizacoes']}")

# ======================================
# BUSCAR SÉRIES
# ======================================
def buscar_serie():

    nome = input("Digite o nome da série: ")

    encontrado = False

    for serie in series:

        if serie["titulo"].lower() == nome.lower():

            print("\n===== SÉRIE ENCONTRADA =====")
            print(f"Título: {serie['titulo']}")
            print(f"Categoria: {serie['categoria']}")
            print(f"Temporadas: {serie['temporadas']}")
            print(f"Avaliações: {serie['avaliacao']}")
            print(f"Visualizações: {serie['visualizacoes']}")

            encontrado = True
            break

    if not encontrado:
        print("\nSérie não encontrada!")

# ======================================
# MENU SÉRIES
# ======================================
def menu_series():

    while True:

        print("\n===== SINEFLIX - SÉRIES =====")
        print("1 - Exibir série")
        print("2 - Buscar série")
        print("3 - Adicionar série")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_series()

        elif opcao == "2":
            buscar_serie()

        elif opcao == "3":
            adicionar_serie()

        elif opcao == "0":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")


