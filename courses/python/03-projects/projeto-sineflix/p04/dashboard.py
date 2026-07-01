from usuarios import usuarios
from filmes import filmes
from series import series
from categorias import obter_frequencia_categorias


def obter_mais_visto(lista):
    if len(lista) == 0:
        return None

    return max(lista, key=lambda item: item["visualizacoes"])


def obter_melhor_avaliado(lista):
    if len(lista) == 0:
        return None

    return max(lista, key=lambda item: item["avaliacao"])


def mostrar_dashboard():
    total_filmes = len(filmes)
    total_series = len(series)
    total_conteudos = total_filmes + total_series
    total_usuarios = len(usuarios)

    frequencias = obter_frequencia_categorias()

    filme_mais_visto = obter_mais_visto(filmes)
    serie_mais_vista = obter_mais_visto(series)

    filme_melhor_avaliado = obter_melhor_avaliado(filmes)
    serie_melhor_avaliada = obter_melhor_avaliado(series)

    print("\n=================================")
    print("        SINEFLIX DASHBOARD        ")
    print("=================================")

    print("Versão: P04")
    print("Release: Platform Integration Dashboard")

    print("\n===== INDICADORES GERAIS =====")
    print(f"Usuários cadastrados: {total_usuarios}")
    print(f"Filmes cadastrados: {total_filmes}")
    print(f"Séries cadastradas: {total_series}")
    print(f"Total de conteúdos: {total_conteudos}")
    print(f"Categorias disponíveis: {len(frequencias)}")

    print("\n===== DESTAQUES =====")

    if filme_mais_visto:
        print(f"Filme mais visto: {filme_mais_visto['titulo']} ({filme_mais_visto['visualizacoes']} views)")

    if serie_mais_vista:
        print(f"Série mais vista: {serie_mais_vista['titulo']} ({serie_mais_vista['visualizacoes']} views)")

    if filme_melhor_avaliado:
        print(f"Filme melhor avaliado: {filme_melhor_avaliado['titulo']} ({filme_melhor_avaliado['avaliacao']} estrelas)")

    if serie_melhor_avaliada:
        print(f"Série melhor avaliada: {serie_melhor_avaliada['titulo']} ({serie_melhor_avaliada['avaliacao']} estrelas)")

    print("\n===== FUNCIONALIDADES DISPONÍVEIS =====")
    print("- Cadastro de usuários")
    print("- Catálogo de filmes")
    print("- Catálogo de séries")
    print("- Catálogo integrado")
    print("- Categorias dinâmicas")
    print("- Histórico")
    print("- Recomendações")
    print("- Simulação matemática")
    print("- Analytics")
    print("- Dashboard")