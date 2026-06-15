import math


def calcular_precisao(avaliacoes):
    """
    Calcula a precisão do algoritmo.

    Fórmula:
    precisão = log10(avaliações) * 25
    """

    return math.log10(avaliacoes) * 25