# ======================================
# SINEFLIX - P02
# Segunda Entrega do Projeto
# ======================================

from usuarios import(
    cadastrar_usuario,
    exibir_usuario,
    menu_usuarios
)

from filmes import(
    adicionar_filme,
    listar_filmes,
    buscar_filme,
    menu_filmes
)

from historico import(
    adicionar_historico,
    exibir_historico
)

from categorias import(
    exibir_categorias
)

from utilitarios import(
    boas_vindas,
    limpar_tela,
    pausar
)

from recomendacoes import (
    menu_recomendacoes
)

from sistema import (
    mostrar_sistema
)

from estatisticas import(
    mostrar_estatisticas
)

# ============================================================
# MAIN - Ponto de entrada do programa
# ============================================================
def main():

    while True:

        # Limpa a tela antes do menu
        limpar_tela()

        print("\n===== MENU SINEFLIX =====")

        print("1 - Usuários")
        print("2 - Catálogo de Filmes")
        print("3 - Exibir filmes por categorias")
        print("4 - Registrar filme assistido")
        print("5 - Exibir Histórico")
        print("6 - Recomendações")
        print("7 - Diagnostico de Sistema")
        print("8 - Estatisticas")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        # Limpa a tela após escolher uma opção
        limpar_tela()

        if opcao == "1":
            menu_usuarios()

        elif opcao == "2":
            menu_filmes()

        elif opcao == "3":
            exibir_categorias()

        elif opcao == "4":
            adicionar_historico()

        elif opcao == "5":
            exibir_historico()

        elif opcao == "6":
            menu_recomendacoes()

        elif opcao == "7":
            mostrar_sistema()

        elif opcao == "8":
            mostrar_estatisticas()

        elif opcao == "9":
            print("Obrigado por utilizar o SineFlix.")
            break

        else:
            print("Opção inválida.")

        # Pausa o sistema ao final da operação
        pausar()


# ======================================
# PROGRAMA PRINCIPAL
# ======================================
boas_vindas()

# ======================================
# BLOCO DE EXECUÇÃO DIRETA
# ======================================
if __name__ == "__main__":
    main()