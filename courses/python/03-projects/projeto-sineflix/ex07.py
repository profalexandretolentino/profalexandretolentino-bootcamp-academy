while True:

    print("\n===== SINEFLIX =====")
    print("1 - Ver catálogo")
    print("2 - Buscar filme")
    print("3 - Histórico")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Abrindo catálogo...")

    elif opcao == "2":
        print("Abrindo busca...")

    elif opcao == "3":
        print("Abrindo histórico...")

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")