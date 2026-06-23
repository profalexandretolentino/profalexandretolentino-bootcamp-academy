catalogo = [
    {
        "tipo": "Filme",
        "titulo": "Matrix",
        "categoria": "Ficção",
        "avaliacao": "⭐⭐⭐⭐⭐"
    },
    {
        "tipo": "Série",
        "titulo": "Dark",
        "categoria": "Ficção",
        "avaliacao": "⭐⭐⭐⭐"
    }
]

2 – FUNÇÃO: CATÁLOGO COMPLETO
# ======================================
# CATÁLOGO COMPLETO
# ======================================

def catalogo_completo(catalogo):

    print("\n===== CATÁLOGO COMPLETO =====")

    filmes_total = 0
    series_total = 0

    for item in catalogo:

        print("\n--------------------")

        print(f"[{item['tipo'].upper()}]")
        print(f"Título: {item['titulo']}")
        print(f"Categoria: {item['categoria']}")
        print(f"Avaliação: {item['avaliacao']}")

        # Conta separadamente
        if item["tipo"] == "Filme":
            filmes_total += 1

        elif item["tipo"] == "Série":
            series_total += 1

    total = filmes_total + series_total

    print("\n===== RESUMO =====")
    print(f"Filmes cadastrados: {filmes_total}")
    print(f"Séries cadastradas: {series_total}")
    print(f"Total de conteúdos: {total}")

    🔍 3 – BUSCA UNIFICADA
# ======================================
# BUSCAR CONTEÚDO
# ======================================

def buscar_conteudo(catalogo):

    nome = input("\nDigite o conteúdo: ")

    encontrado = False

    for item in catalogo:

        if item["titulo"].lower() == nome.lower():

            print("\n===== CONTEÚDO ENCONTRADO =====")
            print(f"Tipo: {item['tipo']}")
            print(f"Título: {item['titulo']}")
            print(f"Categoria: {item['categoria']}")
            print(f"Avaliação: {item['avaliacao']}")

            encontrado = True
            break

    if not encontrado:
        print("\nConteúdo não encontrado.")

        📦 4 – FUNÇÃO PARA ANALYTICS
# ======================================
# EXPORTAÇÃO PARA ANALYTICS
# ======================================

def obter_catalogo_completo(catalogo):

    dados = []

    for item in catalogo:

        dados.append({
            "tipo": item["tipo"],
            "titulo": item["titulo"],
            "categoria": item["categoria"],
            "avaliacao": item["avaliacao"]
        })

    return dados

🧩 5 – MENU SUGERIDO
print("\n===== CATÁLOGO =====")
print("1 - Exibir Catálogo Completo")
print("2 - Buscar Conteúdo")
print("3 - Voltar")

POR QUE ESTE EXERCÍCIO É IMPORTANTE

Este EX30 prepara diretamente para:

EX31 (Ranking e Popularidade)
frequência
ordenação
estatística
UC de Estatística
média
moda
frequência relativa
UC de Banco de Dados
tabela única de conteúdos
entidade “conteúdo”
UC de Cloud / IA futura
catálogo vira dataset