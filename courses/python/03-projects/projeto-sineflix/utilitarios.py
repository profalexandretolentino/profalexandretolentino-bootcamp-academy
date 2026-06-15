# Importa o módulo responsável por executar
# comandos do sistema operacional
import os

# ======================================
# FUNÇÃO DE BOAS-VINDAS
# ======================================
def boas_vindas():

    print("=" * 40)
    print("         BEM-VINDO AO")
    print("           SINEFLIX")
    print("=" * 40)

# ======================================
# LIMPAR TELA
# ======================================


def limpar_tela():

    # Verifica qual sistema operacional está sendo usado
    # "nt" = Windows
    # "posix" = Linux/Mac

    if os.name == "nt":

        # Comando para limpar o terminal no Windows
        os.system("cls")

    else:

        # Comando para limpar o terminal no Linux/Mac
        os.system("clear")

    
# ======================================
# PAUSAR SISTEMA
# ======================================
def pausar():

    # Aguarda o usuário pressionar ENTER
    input("\nPressione ENTER para continuar...")