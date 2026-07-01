"""
analytics.py

Módulo responsável pelas funcionalidades analíticas do SineFlix.

Ex18 -> Crescimento da Plataforma (Função Linear)
Ex19 -> Viralização de Trailer (Função Exponencial)
Ex20 -> Popularidade de Filmes (Função Polinomial)
Ex21 -> Inteligência de Recomendação (Função Logarítmica)

Professor Alexandre Tolentino
Projeto Integrador SineFlix
"""

import math
import random
import platform


# ==================================================
# EX18 - FUNÇÃO LINEAR
# ==================================================

def prever_usuarios(dias):
    """
    Calcula a previsão de usuários da plataforma.

    Fórmula:
    usuários = (50 * dias) + 1000
    """

    return (50 * dias) + 1000


# ==================================================
# EX19 - FUNÇÃO EXPONENCIAL
# ==================================================

def prever_views(dias):
    """
    Simula a viralização de um trailer.

    Fórmula:
    views = 100 * (2 ** dias)
    """

    return 100 * (2 ** dias)


# ==================================================
# EX20 - FUNÇÃO POLINOMIAL
# ==================================================

def calcular_popularidade(dia):
    """
    Simula a popularidade de um filme.

    Fórmula:
    f(x) = -2x² + 20x + 15
    """

    return (-2 * (dia ** 2)) + (20 * dia) + 15


# ==================================================
# EX21 - FUNÇÃO LOGARÍTMICA
# ==================================================

def calcular_precisao(avaliacoes):
    """
    Calcula a precisão do algoritmo de recomendação.

    Fórmula:
    precisão = log10(avaliações) * 25
    """

    return math.log10(avaliacoes) * 25


# ==================================================
# FUNÇÕES DE DEMONSTRAÇÃO
# ==================================================

def crescimento_plataforma():
    """
    Executa o simulador de crescimento.
    """

    print("\n===== CRESCIMENTO DA PLATAFORMA =====")

    dias = int(input("Informe a quantidade de dias: "))

    usuarios = prever_usuarios(dias)

    print()
    print(f"Dias analisados: {dias}")
    print(f"Usuários previstos: {usuarios}")


def viralizacao_trailer():
    """
    Executa o simulador de viralização.
    """

    print("\n===== VIRALIZAÇÃO DE TRAILER =====")

    dias = int(input("Informe a quantidade de dias: "))

    views = prever_views(dias)

    print()
    print(f"Dias analisados: {dias}")
    print(f"Visualizações previstas: {views}")


def popularidade_filme():
    """
    Executa o simulador de popularidade.
    """

    print("\n===== POPULARIDADE DE FILMES =====")

    dia = int(input("Informe o dia analisado: "))

    popularidade = calcular_popularidade(dia)

    print()
    print(f"Dia analisado: {dia}")
    print(f"Popularidade calculada: {popularidade}")


def inteligencia_recomendacao():
    """
    Executa o simulador logarítmico.
    """

    print("\n===== INTELIGÊNCIA DE RECOMENDAÇÃO =====")

    avaliacoes = int(
        input("Quantidade de avaliações recebidas: ")
    )

    precisao = calcular_precisao(avaliacoes)

    print()
    print(f"Avaliações analisadas: {avaliacoes}")
    print(f"Precisão estimada: {precisao:.2f}%")


# ==================================================
# PAINEL ANALYTICS (P03)
# ==================================================

def painel_analytics():
    """
    Integra todas as funcionalidades do módulo.
    """

    usuarios_previstos = prever_usuarios(30)

    views_previstas = prever_views(5)

    popularidade = calcular_popularidade(4)

    precisao = calcular_precisao(1000)

    print("\n===== PAINEL ANALYTICS =====\n")

    print(
        f"Usuários previstos em 30 dias: "
        f"{usuarios_previstos}"
    )

    print(
        f"Visualizações previstas em 5 dias: "
        f"{views_previstas}"
    )

    print(
        f"Popularidade do filme: "
        f"{popularidade}"
    )

    print(
        f"Precisão do algoritmo: "
        f"{precisao:.2f}%"
    )

    print()


# ==================================================
# MENU ANALYTICS
# ==================================================

def menu_analytics():

    while True:

        print("\n===== SINEFLIX ANALYTICS =====")
        print("1 - Crescimento da Plataforma")
        print("2 - Viralização de Trailer")
        print("3 - Popularidade de Filmes")
        print("4 - Inteligência de Recomendação")
        print("5 - Painel Analytics")
        print("6 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            crescimento_plataforma()

        elif opcao == "2":

            viralizacao_trailer()

        elif opcao == "3":

            popularidade_filme()

        elif opcao == "4":

            inteligencia_recomendacao()

        elif opcao == "5":

            painel_analytics()

        elif opcao == "6":

            print("\nRetornando ao menu principal...")
            break

        else:

            print("\nOpção inválida!")