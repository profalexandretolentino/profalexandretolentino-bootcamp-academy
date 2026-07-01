# ============================================
# SineFlix Educational Platform
# Version: P04
# Release: Platform Integration Dashboard
# Status: Stable
# ============================================
from analytics import menu_analytics

from usuarios import(
    menu_usuarios
)

from filmes import(
    menu_filmes
)

from historico import(
    menu_historico
)

from categorias import(
    menu_categorias
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

from simulacao import(
    mostrar_simulacao
)

from series import (
    menu_series
)

from catalogo import menu_catalogo

from dashboard import mostrar_dashboard

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
        print("3 - Catálogo de Séries")
        print("4 - Catálogo Integrado")
        print("5 - Categorias")
        print("6 - Histórico")
        print("7 - Recomendações")
        print("8 - Diagnóstico de Sistema")
        print("9 - Simulação Matemática")
        print("10 - Analytics")
        print("11 - Dashboard")
        print("12 - Sair")

        opcao = input("Escolha uma opção: ")

        # Limpa a tela após escolher uma opção
        limpar_tela()

        if opcao == "1":
            menu_usuarios()

        elif opcao == "2":
            menu_filmes()

        elif opcao == "3":
            menu_series()

        elif opcao == "4":
            menu_catalogo()

        elif opcao == "5":
            menu_categorias()

        elif opcao == "6":
            menu_historico()

        elif opcao == "7":
            menu_recomendacoes()

        elif opcao == "8":
            mostrar_sistema()

        elif opcao == "9":
            mostrar_simulacao()

        elif opcao == "10":
            menu_analytics() 

        elif opcao == "11":
            mostrar_dashboard()

        elif opcao == "12":
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