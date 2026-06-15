# ============================================================
# SINEFLIX - Diagnóstico do Sistema
# Módulo utilizado: platform (biblioteca padrão do Python)
# ============================================================
# O módulo platform permite coletar informações sobre o
# ambiente onde o programa está sendo executado:
# sistema operacional, versão, hardware e Python.
#
# Não precisa instalar nada — já vem com o Python!
# Basta importar com: import platform
# ============================================================

import platform  # Importa o módulo platform da biblioteca padrão


# ============================================================
# FUNÇÃO - mostrar_sistema()
# ============================================================
# Responsável por coletar e exibir as informações do sistema
# utilizando as funções disponíveis no módulo platform.
# ============================================================
def mostrar_sistema():
    print("\n===== DIAGNÓSTICO DO SINEFLIX =====")

    # platform.system() → retorna o nome do sistema operacional
    # Exemplos de retorno: "Windows", "Linux", "Darwin" (macOS)
    print(f"Sistema Operacional: {platform.system()}")

    # platform.release() → retorna a versão/release do sistema
    # Exemplos: "11" (Windows 11), "10" (Windows 10), "22.04" (Ubuntu)
    print(f"Versão:              {platform.release()}")

    # platform.machine() → retorna a arquitetura do hardware
    # Exemplos: "AMD64", "x86_64", "ARM64"
    print(f"Arquitetura:         {platform.machine()}")

    # platform.processor() → retorna o nome do processador
    # Exemplos: "Intel64 Family 6", "AMD Ryzen 5", "arm"
    # Obs: em alguns sistemas Linux pode retornar uma string vazia
    print(f"Processador:         {platform.processor()}")

    # platform.python_version() → retorna a versão do Python em uso
    # Exemplo de retorno: "3.13.0"
    # Útil para verificar compatibilidade do ambiente
    print(f"Python:              {platform.python_version()}")