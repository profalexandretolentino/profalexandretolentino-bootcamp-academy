# ======================================
# SINEFLIX - P02
# Segunda Entrega do Projeto
# ======================================
from usuarios import(
    cadastrar_usuario,
    exibir_perfil
)
from filmes import(
    listar_filmes,
    buscar_filme
)
from historico import(
    adicionar_historico,
    exibir_historico
)

from categorias import(
    exibir_categorias
)

from utilitarios import(
    boas_vindas
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
# A função main() é o menu principal da aplicação.
# Ela chama menu_recomendacoes() como uma das opções,
# mantendo o código organizado e fácil de expandir.
# ============================================================
def main():

    while True:

        print("\n===== MENU SINEFLIX =====")

        print("1 - Cadastrar usuário")
        print("2 - Exibir perfil")
        print("3 - Catálogo")
        print("4 - Buscar filme")
        print("5 - Categorias")
        print("6 - Registrar filme assistido")
        print("7 - Histórico")
        print("8 - Menu de Recomendações")
        print("9 - Diagnostico de Sistema")
        print("10 - Estatisticas")
        print("11 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            exibir_perfil()

        elif opcao == "3":
            listar_filmes()

        elif opcao == "4":
            buscar_filme()

        elif opcao == "5":
            exibir_categorias()

        elif opcao == "6":
            adicionar_historico()

        elif opcao == "7":
            exibir_historico()

        elif opcao == "8":
            menu_recomendacoes()

        elif opcao == "9":
            mostrar_sistema() 

        elif opcao == "10":
            mostrar_estatisticas()

        elif opcao == "11":
            print("Obrigado por utilizar o SineFlix.")
            break

        else:
            print("Opção inválida.")


# ======================================
# PROGRAMA PRINCIPAL
# ======================================
boas_vindas()
# ======================================
# BLOCO DE EXECUÇÃO DIRETA
# ======================================
# O bloco abaixo só executa quando este arquivo é rodado
# diretamente (ex: python recomendacoes.py).
#
# Se este arquivo for importado por outro módulo,
# o main() NÃO será chamado automaticamente.
# Isso é uma boa prática em Python para organizar projetos
# com múltiplos arquivos.
# ============================================================
if __name__ == "__main__":
    main()
 
