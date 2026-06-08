# ============================================================
# SINEFLIX - Estatísticas do Catálogo
# Módulo utilizado: math (biblioteca padrão do Python)
# ============================================================
# O módulo math oferece funções matemáticas prontas para uso.
# Todas baseadas na biblioteca C padrão — rápidas e precisas.
#
# Não precisa instalar nada — já vem com o Python!
# Basta importar com: import math
# ============================================================

import math  # Importa o módulo math da biblioteca padrão


# Catálogo de filmes usado como base para os cálculos
from filmes import filmes

# Total de filmes cadastrados — usado em várias funções abaixo
total_filmes = len(filmes)  # Retorna 8


# ============================================================
# PARTE 1 - math.sqrt()
# ============================================================
# math.sqrt(x) calcula a raiz quadrada de x.
# Sempre retorna um float (número decimal).
# Exemplo: math.sqrt(9) → 3.0 | math.sqrt(8) → 2.8284...
#
# Uso aqui: descobrir a "raiz" do catálogo, útil para
# algoritmos de escala e distribuição de conteúdo.
# ============================================================
def calcular_raiz_filmes():
    print("\n===== PARTE 1 - RAIZ QUADRADA DO CATÁLOGO =====")

    # math.sqrt() recebe o total de filmes e retorna um float
    raiz = math.sqrt(total_filmes)

    # :.2f formata o float para exibir apenas 2 casas decimais
    print(f"Total de filmes: {total_filmes}")
    print(f"Raiz quadrada:   {raiz:.2f}")


# ============================================================
# PARTE 2 - math.pow()
# ============================================================
# math.pow(x, y) calcula x elevado à potência y.
# Sempre retorna um float, mesmo que o resultado seja inteiro.
# Exemplo: math.pow(3, 2) → 9.0 | math.pow(2, 10) → 1024.0
#
# Diferença do operador **: math.pow() sempre retorna float,
# enquanto 3 ** 2 pode retornar int.
# ============================================================
def calcular_quadrado_filmes():
    print("\n===== PARTE 2 - QUADRADO DO CATÁLOGO =====")

    # math.pow(total_filmes, 2) eleva o total à potência 2
    quadrado = math.pow(total_filmes, 2)

    print(f"Total de filmes:  {total_filmes}")
    print(f"Total ao quadrado: {quadrado:.0f}")  # :.0f remove as casas decimais


# ============================================================
# PARTE 3 - math.floor() e math.ceil()
# ============================================================
# math.floor(x) → arredonda para BAIXO (piso)
# Retorna o maior inteiro menor ou igual a x.
# Exemplo: math.floor(2.7) → 2 | math.floor(2.1) → 2
#
# math.ceil(x) → arredonda para CIMA (teto)
# Retorna o menor inteiro maior ou igual a x.
# Exemplo: math.ceil(2.7) → 3 | math.ceil(2.1) → 3
#
# Uso aqui: estimar o tempo mínimo e máximo de visualização.
# ============================================================
def calcular_horas_visualizacao():
    print("\n===== PARTE 3 - ESTIMATIVA DE HORAS =====")

    horas_estimadas = 2.7  # Horas estimadas para assistir as recomendações

    # floor() garante o mínimo de horas completas (sem arredondar para cima)
    horas_minimas = math.floor(horas_estimadas)

    # ceil() garante o máximo de horas completas (sem arredondar para baixo)
    horas_maximas = math.ceil(horas_estimadas)

    print(f"Horas estimadas:         {horas_estimadas}h")
    print(f"Horas mínimas completas: {horas_minimas}h  (math.floor)")
    print(f"Horas máximas completas: {horas_maximas}h  (math.ceil)")


# ============================================================
# PARTE 4 - math.fabs()
# ============================================================
# math.fabs(x) retorna o valor absoluto (módulo) de x.
# Ou seja: sempre retorna o número sem o sinal negativo.
# Sempre retorna um float.
# Exemplo: math.fabs(-15) → 15.0 | math.fabs(15) → 15.0
#
# Diferença de abs(): abs() é nativo do Python e pode retornar
# int ou float. math.fabs() sempre retorna float.
#
# Uso aqui: converter diferença negativa em valor positivo
# para exibir em relatórios de visualizações.
# ============================================================
def corrigir_diferenca_visualizacoes():
    print("\n===== PARTE 4 - DIFERENÇA DE VISUALIZAÇÕES =====")

    diferenca = -15  # Valor negativo registrado pelo sistema

    # math.fabs() converte qualquer valor para seu módulo positivo
    diferenca_corrigida = math.fabs(diferenca)

    print(f"Diferença registrada: {diferenca}")
    print(f"Valor absoluto:       {diferenca_corrigida:.0f}")


# ============================================================
# PARTE 5 - math.factorial()
# ============================================================
# math.factorial(n) calcula o fatorial de n.
# O fatorial de n é o produto de todos os inteiros de 1 até n.
# Notação matemática: n!
# Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# Uso aqui: calcular o total de combinações possíveis de
# categorias para um ranking simbólico do catálogo.
#
# ATENÇÃO: só aceita inteiros não negativos.
# math.factorial(-1) ou math.factorial(2.5) geram erro!
# ============================================================
def calcular_ranking_categorias():
    print("\n===== PARTE 5 - RANKING DE CATEGORIAS =====")

    categorias = 5  # Número de categorias cadastradas no sistema

    # math.factorial(5) calcula 5! = 5 × 4 × 3 × 2 × 1 = 120
    combinacoes = math.factorial(categorias)

    print(f"{categorias} categorias cadastradas")
    print(f"Total de combinações possíveis: {combinacoes}")


# ============================================================
# FUNÇÃO PRINCIPAL - Chama todas as estatísticas
# ============================================================
def mostrar_estatisticas():
    print("\n========================================")
    print("   SINEFLIX - ESTATÍSTICAS DO SISTEMA   ")
    print("========================================")

    calcular_raiz_filmes()        # Parte 1 — math.sqrt()
    calcular_quadrado_filmes()    # Parte 2 — math.pow()
    calcular_horas_visualizacao()   # Parte 3 — math.floor() e math.ceil()
    corrigir_diferenca_visualizacoes()  # Parte 4 — math.fabs()
    calcular_ranking_categorias()   # Parte 5 — math.factorial()