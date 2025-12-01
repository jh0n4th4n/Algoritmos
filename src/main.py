from fatorial import calcular_fatorial
from fibonacci import gerar_fibonacci
from primos import eh_primo
from ordenacao import ordenar_lista
from palindromo import eh_palindromo
from mdc_mmc import calcular_mdc_mmc
from busca_linear import busca_linear
from quicksort import quicksort
from contagem_vogais import contar_vogais
from inverter_string import inverter_string
from potencia import potencia
from numero_perfeito import numero_perfeito
from busca_binaria import busca_binaria
from fatorial_recursivo import calcular_fatorial_recursivo
from decimal_binario import decimal_para_binario
from mergesort import mergesort
from hanoi import resolver_hanoi
from pilha import Pilha
from grafos import bfs, dfs
from dijkstra import dijkstra, reconstruir_caminho
from kadane import maior_soma_subarray
from kmp import kmp_busca
from edit_distance import distancia_edicao
from floyd_warshall import floyd_warshall, INF
from union_find import UnionFind
from segment_tree import SegmentTree


def menu() -> None:
    print("=== Resolvendo Algoritmos com GitHub Copilot ===")
    print("1  - Calcular fatorial (iterativo)")
    print("2  - Gerar sequência de Fibonacci")
    print("3  - Verificar se um número é primo")
    print("4  - Ordenar lista (Bubble Sort)")
    print("5  - Verificar se é palíndromo")
    print("6  - Calcular MDC e MMC")
    print("7  - Busca linear")
    print("8  - Ordenar lista (QuickSort)")
    print("9  - Contar vogais de um texto")
    print("10 - Inverter string")
    print("11 - Calcular potência")
    print("12 - Verificar número perfeito")
    print("13 - Busca binária")
    print("14 - Calcular fatorial (recursivo)")
    print("15 - Converter decimal para binário")
    print("16 - Ordenar lista (MergeSort)")
    print("17 - Torre de Hanói")
    print("18 - Demonstração de Pilha (Stack)")
    print("19 - BFS e DFS em grafo (demonstração)")
    print("20 - Menor caminho em grafo (Dijkstra)")
    print("21 - Maior soma de subarray (Kadane)")
    print("22 - Busca de padrão em texto (KMP)")
    print("23 - Distância de edição (Levenshtein)")
    print("24 - Todos os menores caminhos (Floyd–Warshall)")
    print("25 - Demonstração de Union-Find")
    print("26 - Demonstração de Segment Tree (soma em intervalo)")
    print("0  - Sair")


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_lista_inteiros(mensagem: str) -> list[int]:
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            return []
        try:
            return [int(x) for x in entrada.split()]
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros separados por espaço.")


# ================== AÇÕES DO MENU ================== #

def acao_1_fatorial() -> None:
    n = ler_inteiro("Digite um número inteiro não negativo: ")
    try:
        print(f"Fatorial de {n} é {calcular_fatorial(n)}")
    except ValueError as e:
        print(f"Erro: {e}")


def acao_2_fibonacci() -> None:
    n = ler_inteiro("Quantos termos da sequência de Fibonacci você deseja? ")
    try:
        print(f"Sequência de Fibonacci: {gerar_fibonacci(n)}")
    except ValueError as e:
        print(f"Erro: {e}")


def acao_3_primo() -> None:
    n = ler_inteiro("Digite um número inteiro: ")
    print(f"{n} é primo." if eh_primo(n) else f"{n} não é primo.")


def acao_4_bubble_sort() -> None:
    lista = ler_lista_inteiros("Digite números inteiros separados por espaço: ")
    print(f"Lista ordenada (Bubble Sort): {ordenar_lista(lista)}")


def acao_5_palindromo() -> None:
    texto = input("Digite uma palavra ou frase: ")
    print("É palíndromo!" if eh_palindromo(texto) else "Não é palíndromo.")


def acao_6_mdc_mmc() -> None:
    a = ler_inteiro("Digite o 1º número: ")
    b = ler_inteiro("Digite o 2º número: ")
    resultado = calcular_mdc_mmc(a, b)
    print(f"MDC({a},{b}) = {resultado['MDC']} | MMC({a},{b}) = {resultado['MMC']}")


def acao_7_busca_linear() -> None:
    lista = ler_lista_inteiros("Digite os números: ")
    valor = ler_inteiro("Digite o valor a buscar: ")
    print("Encontrado!" if busca_linear(lista, valor) else "Não encontrado.")


def acao_8_quicksort() -> None:
    lista = ler_lista_inteiros("Digite os números: ")
    print(f"Ordenado (QuickSort): {quicksort(lista)}")


def acao_9_contar_vogais() -> None:
    texto = input("Digite um texto: ")
    print(f"Quantidade de vogais: {contar_vogais(texto)}")


def acao_10_inverter_string() -> None:
    texto = input("Digite uma string: ")
    print(f"Invertida: {inverter_string(texto)}")


def acao_11_potencia() -> None:
    base = ler_inteiro("Base: ")
    exp = ler_inteiro("Expoente: ")
    print(f"{base}^{exp} = {potencia(base, exp)}")


def acao_12_numero_perfeito() -> None:
    n = ler_inteiro("Digite um número: ")
    print("Número perfeito!" if numero_perfeito(n) else "Não é número perfeito.")


def acao_13_busca_binaria() -> None:
    lista = ler_lista_inteiros("Digite os números: ")
    valor = ler_inteiro("Valor a buscar: ")
    print("Encontrado!" if busca_binaria(lista, valor) else "Não encontrado.")


def acao_14_fatorial_recursivo() -> None:
    n = ler_inteiro("Digite um número: ")
    print(f"[Recursivo] Fatorial: {calcular_fatorial_recursivo(n)}")


def acao_15_decimal_binario() -> None:
    n = ler_inteiro("Digite um número: ")
    try:
        print(f"{n} em binário: {decimal_para_binario(n)}")
    except ValueError as e:
        print(f"Erro: {e}")


def acao_16_mergesort() -> None:
    lista = ler_lista_inteiros("Digite os números: ")
    print(f"Ordenado (MergeSort): {mergesort(lista)}")


def acao_17_hanoi() -> None:
    n = ler_inteiro("Quantidade de discos: ")
    if n > 0:
        movimentos = resolver_hanoi(n, "A", "B", "C")
        print(f"Movimentos ({len(movimentos)}):")
        for mov in movimentos:
            print(mov)
    else:
        print("Número de discos deve ser maior que zero.")


def acao_18_pilha() -> None:
    print("=== Demonstração de Pilha ===")
    pilha = Pilha()
    print("Digite valores (Enter para finalizar):")
    while True:
        item = input("Valor: ")
        if item.strip() == "":
            break
        try:
            pilha.empilhar(int(item))
        except ValueError:
            print("Digite somente números!")
    print(f"Pilha criada: {pilha}")
    print("Desempilhando...")
    while not pilha.esta_vazia():
        print("->", pilha.desempilhar())
    print("Pilha vazia!")


def acao_19_bfs_dfs() -> None:
    print("=== Demonstração de BFS e DFS em grafo ===")
    grafo_exemplo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    inicio = input("Vértice inicial (ex.: A): ").strip().upper() or "A"
    if inicio not in grafo_exemplo:
        print("Vértice não encontrado no grafo de exemplo. Usando A.")
        inicio = "A"
    print("BFS:", bfs(grafo_exemplo, inicio))
    print("DFS:", dfs(grafo_exemplo, inicio))


def acao_20_dijkstra() -> None:
    print("=== Menor caminho em grafo (Dijkstra) ===")
    grafo_ponderado = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "D": 1, "E": 3},
        "C": {"A": 5, "F": 2},
        "D": {"B": 1, "E": 1},
        "E": {"B": 3, "D": 1, "F": 2},
        "F": {"C": 2, "E": 2},
    }
    origem = input("Vértice de origem (ex.: A): ").strip().upper() or "A"
    destino = input("Vértice de destino (ex.: F): ").strip().upper() or "F"

    if origem not in grafo_ponderado or destino not in grafo_ponderado:
        print("Origem ou destino inválidos no grafo de exemplo.")
        return

    resultado = dijkstra(grafo_ponderado, origem)
    caminho = reconstruir_caminho(resultado, origem, destino)

    if not caminho:
        print("Não há caminho entre origem e destino.")
    else:
        distancia, _ = resultado[destino]
        print(f"Menor distância de {origem} até {destino}: {distancia}")
        print("Caminho:", " -> ".join(caminho))


def acao_21_kadane() -> None:
    print("=== Maior soma de subarray (Kadane) ===")
    lista = ler_lista_inteiros("Digite números inteiros separados por espaço: ")
    if not lista:
        print("Lista vazia. A maior soma é 0.")
        return
    melhor_soma, inicio, fim = maior_soma_subarray(lista)
    subarray = lista[inicio:fim + 1]
    print(f"Maior soma: {melhor_soma}")
    print(f"Subarray correspondente: {subarray} (índices {inicio}..{fim})")


def acao_22_kmp() -> None:
    print("=== KMP - Busca de padrão em texto ===")
    texto = input("Digite o texto: ")
    padrao = input("Digite o padrão a ser buscado: ")
    posicoes = kmp_busca(texto, padrao)
    if not posicoes:
        print("Padrão não encontrado no texto.")
    else:
        print(f"Padrão encontrado nas posições: {posicoes}")


def acao_23_distancia_edicao() -> None:
    print("=== Distância de edição (Levenshtein) ===")
    a = input("Digite a primeira string: ")
    b = input("Digite a segunda string: ")
    dist = distancia_edicao(a, b)
    print(f"Distância de edição entre '{a}' e '{b}': {dist}")


def acao_24_floyd_warshall() -> None:
    print("=== Floyd–Warshall: todos os menores caminhos ===")
    print("Usando uma matriz de exemplo 3x3.")
    matriz = [
        [0,   3,   INF],
        [INF, 0,   1],
        [2,   INF, 0],
    ]
    dist = floyd_warshall(matriz)
    print("Matriz de distâncias mínimas:")
    for linha in dist:
        print(linha)


def acao_25_union_find() -> None:
    print("=== Demonstração de Union-Find ===")
    uf = UnionFind()
    elementos = ["A", "B", "C", "D", "E"]
    print("Uniões: (A,B), (B,C), (D,E)")
    uf.unir("A", "B")
    uf.unir("B", "C")
    uf.unir("D", "E")
    for x in elementos:
        for y in elementos:
            if x < y:
                mesmo = uf.mesmo_conjunto(x, y)
                print(f"{x} e {y} estão no mesmo conjunto? {mesmo}")


def acao_26_segment_tree() -> None:
    print("=== Demonstração de Segment Tree (soma em intervalo) ===")
    lista = ler_lista_inteiros("Digite números inteiros para a lista base: ")
    if not lista:
        print("Lista vazia, nada a fazer.")
        return

    st = SegmentTree(lista)
    print("Segment Tree criada.")
    while True:
        print("\n1 - Consultar soma em intervalo [l, r]")
        print("2 - Atualizar posição específica")
        print("0 - Voltar ao menu principal")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            l = ler_inteiro("Início do intervalo (l): ")
            r = ler_inteiro("Fim do intervalo (r): ")
            if 0 <= l <= r < len(lista):
                print(f"Soma em [{l}, {r}] = {st.query(l, r)}")
            else:
                print("Intervalo inválido.")
        elif escolha == "2":
            idx = ler_inteiro("Índice a atualizar: ")
            if 0 <= idx < len(lista):
                valor = ler_inteiro("Novo valor: ")
                lista[idx] = valor
                st.update(idx, valor)
                print("Valor atualizado.")
            else:
                print("Índice inválido.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")


OPCOES = {
    "1": acao_1_fatorial,
    "2": acao_2_fibonacci,
    "3": acao_3_primo,
    "4": acao_4_bubble_sort,
    "5": acao_5_palindromo,
    "6": acao_6_mdc_mmc,
    "7": acao_7_busca_linear,
    "8": acao_8_quicksort,
    "9": acao_9_contar_vogais,
    "10": acao_10_inverter_string,
    "11": acao_11_potencia,
    "12": acao_12_numero_perfeito,
    "13": acao_13_busca_binaria,
    "14": acao_14_fatorial_recursivo,
    "15": acao_15_decimal_binario,
    "16": acao_16_mergesort,
    "17": acao_17_hanoi,
    "18": acao_18_pilha,
    "19": acao_19_bfs_dfs,
    "20": acao_20_dijkstra,
    "21": acao_21_kadane,
    "22": acao_22_kmp,
    "23": acao_23_distancia_edicao,
    "24": acao_24_floyd_warshall,
    "25": acao_25_union_find,
    "26": acao_26_segment_tree,
}


def main() -> None:
    while True:
        print()
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo... Obrigado por utilizar o programa!")
            break

        acao = OPCOES.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
