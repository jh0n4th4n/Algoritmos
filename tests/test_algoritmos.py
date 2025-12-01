import os
import sys
import pytest

# Garante que a pasta src/ entre no sys.path para os imports funcionarem
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from fatorial import calcular_fatorial
from fatorial_recursivo import calcular_fatorial_recursivo
from fibonacci import gerar_fibonacci
from primos import eh_primo
from ordenacao import ordenar_lista
from quicksort import quicksort
from mergesort import mergesort
from palindromo import eh_palindromo
from mdc_mmc import mdc, mmc, calcular_mdc_mmc
from busca_linear import busca_linear
from busca_binaria import busca_binaria
from contagem_vogais import contar_vogais
from inverter_string import inverter_string
from potencia import potencia
from numero_perfeito import numero_perfeito
from decimal_binario import decimal_para_binario
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


# ----------------- FATORIAL ----------------- #

def test_calcular_fatorial_iterativo():
    assert calcular_fatorial(0) == 1
    assert calcular_fatorial(1) == 1
    assert calcular_fatorial(5) == 120
    with pytest.raises(ValueError):
        calcular_fatorial(-1)


def test_calcular_fatorial_recursivo():
    assert calcular_fatorial_recursivo(0) == 1
    assert calcular_fatorial_recursivo(1) == 1
    assert calcular_fatorial_recursivo(5) == 120


# ----------------- FIBONACCI ----------------- #

def test_gerar_fibonacci():
    assert gerar_fibonacci(0) == []
    assert gerar_fibonacci(1) == [0]
    assert gerar_fibonacci(2) == [0, 1]
    assert gerar_fibonacci(5) == [0, 1, 1, 2, 3]
    with pytest.raises(ValueError):
        gerar_fibonacci(-1)


# ----------------- PRIMOS ----------------- #

def test_eh_primo():
    assert eh_primo(2) is True
    assert eh_primo(3) is True
    assert eh_primo(5) is True
    assert eh_primo(4) is False
    assert eh_primo(1) is False
    assert eh_primo(0) is False
    assert eh_primo(-7) is False


# ----------------- ORDENAÇÃO ----------------- #

def test_ordenar_lista_bubble_sort():
    assert ordenar_lista([]) == []
    assert ordenar_lista([1]) == [1]
    assert ordenar_lista([3, 2, 1]) == [1, 2, 3]
    assert ordenar_lista([5, -1, 3, 0]) == [-1, 0, 3, 5]


def test_quicksort():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([5, -1, 3, 0]) == [-1, 0, 3, 5]
    assert quicksort([3, 3, 1]) == [1, 3, 3]


def test_mergesort():
    assert mergesort([]) == []
    assert mergesort([1]) == [1]
    assert mergesort([3, 2, 1]) == [1, 2, 3]
    assert mergesort([5, -1, 3, 0]) == [-1, 0, 3, 5]


# ----------------- STRINGS / PALÍNDROMO ----------------- #

def test_eh_palindromo():
    assert eh_palindromo("arara") is True
    assert eh_palindromo("Arara") is True
    assert eh_palindromo("Socorram me subi no onibus em marrocos") is True
    assert eh_palindromo("python") is False


def test_contar_vogais():
    assert contar_vogais("Olá Mundo") == 3
    assert contar_vogais("BCDF") == 0
    assert contar_vogais("") == 0


def test_inverter_string():
    assert inverter_string("abc") == "cba"
    assert inverter_string("") == ""
    assert inverter_string("radar") == "radar"


# ----------------- MDC / MMC ----------------- #

def test_mdc_mmc():
    assert mdc(12, 18) == 6
    assert mmc(12, 18) == 36
    resultado = calcular_mdc_mmc(12, 18)
    assert resultado["MDC"] == 6
    assert resultado["MMC"] == 36


# ----------------- BUSCAS ----------------- #

def test_busca_linear():
    lista = [10, 20, 30, 40]
    assert busca_linear(lista, 10) is True
    assert busca_linear(lista, 25) is False


def test_busca_binaria():
    lista = [5, 1, 4, 2, 3]
    assert busca_binaria(lista, 3) is True
    assert busca_binaria(lista, 10) is False


# ----------------- POTÊNCIA / NÚMEROS ----------------- #

def test_potencia():
    assert potencia(2, 0) == 1
    assert potencia(2, 3) == 8
    assert potencia(5, 1) == 5


def test_numero_perfeito():
    assert numero_perfeito(6) is True
    assert numero_perfeito(28) is True
    assert numero_perfeito(8) is False
    assert numero_perfeito(1) is False


def test_decimal_para_binario():
    assert decimal_para_binario(0) == "0"
    assert decimal_para_binario(1) == "1"
    assert decimal_para_binario(2) == "10"
    assert decimal_para_binario(10) == "1010"
    with pytest.raises(ValueError):
        decimal_para_binario(-1)


# ----------------- TORRE DE HANÓI ----------------- #

def test_resolver_hanoi():
    movimentos_1 = resolver_hanoi(1, "A", "B", "C")
    assert len(movimentos_1) == 1

    movimentos_3 = resolver_hanoi(3, "A", "B", "C")
    # Para n discos, número de movimentos = 2^n - 1
    assert len(movimentos_3) == 7
    assert movimentos_3[0].startswith("Mover disco de")
    assert movimentos_3[-1].startswith("Mover disco de")


# ----------------- PILHA ----------------- #

def test_pilha_basico():
    pilha = Pilha()
    assert pilha.esta_vazia() is True
    pilha.empilhar(10)
    pilha.empilhar(20)
    assert len(pilha) == 2
    assert pilha.topo() == 20
    assert pilha.desempilhar() == 20
    assert pilha.desempilhar() == 10
    assert pilha.esta_vazia() is True


def test_pilha_desempilhar_vazia():
    pilha = Pilha()
    with pytest.raises(IndexError):
        pilha.desempilhar()


# ----------------- GRAFOS: BFS / DFS ----------------- #

def test_bfs_dfs():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B"],
    }
    bfs_ordem = bfs(grafo, "A")
    dfs_ordem = dfs(grafo, "A")

    assert bfs_ordem[0] == "A"
    assert set(bfs_ordem) == {"A", "B", "C", "D"}
    assert dfs_ordem[0] == "A"
    assert set(dfs_ordem) == {"A", "B", "C", "D"}


# ----------------- DIJKSTRA ----------------- #

def test_dijkstra():
    grafo = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "D": 1},
        "C": {"A": 5, "D": 2},
        "D": {"B": 1, "C": 2},
    }
    resultado = dijkstra(grafo, "A")
    distancia_d, _ = resultado["D"]
    # menor caminho A -> D = A -> B -> D com custo 3
    assert distancia_d == 3

    caminho = reconstruir_caminho(resultado, "A", "D")
    assert caminho == ["A", "B", "D"]


# ----------------- KADANE ----------------- #

def test_kadane():
    numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    soma, inicio, fim = maior_soma_subarray(numeros)
    assert soma == 6
    assert numeros[inicio:fim + 1] == [4, -1, 2, 1]


# ----------------- KMP ----------------- #

def test_kmp_busca():
    texto = "ababcabcababc"
    padrao = "abc"
    posicoes = kmp_busca(texto, padrao)
    assert posicoes == [2, 5, 10]


# ----------------- DISTÂNCIA DE EDIÇÃO ----------------- #

def test_distancia_edicao():
    assert distancia_edicao("gato", "rato") == 1
    assert distancia_edicao("flor", "dor") == 2
    assert distancia_edicao("carro", "caro") == 1
    assert distancia_edicao("", "abc") == 3
    assert distancia_edicao("abc", "") == 3


# ----------------- FLOYD–WARSHALL ----------------- #

def test_floyd_warshall():
    matriz = [
        [0,   3,   INF],
        [INF, 0,   1],
        [2,   INF, 0],
    ]
    dist = floyd_warshall(matriz)
    # menor caminho 0 -> 2 = 3 + 1 = 4
    assert dist[0][2] == 4
    # menor caminho 2 -> 1 = 2 + 3 = 5
    assert dist[2][1] == 5


# ----------------- UNION-FIND ----------------- #

def test_union_find():
    uf = UnionFind()
    uf.unir("A", "B")
    uf.unir("B", "C")
    uf.unir("D", "E")

    assert uf.mesmo_conjunto("A", "C") is True
    assert uf.mesmo_conjunto("A", "D") is False
    assert uf.mesmo_conjunto("D", "E") is True
    assert uf.mesmo_conjunto("B", "E") is False


# ----------------- SEGMENT TREE ----------------- #

def test_segment_tree():
    dados = [1, 2, 3, 4]
    st = SegmentTree(dados)

    # soma [0, 3] = 1+2+3+4 = 10
    assert st.query(0, 3) == 10
    # soma [1, 2] = 2+3 = 5
    assert st.query(1, 2) == 5

    # atualiza posição 1 para 10 -> lista vira [1,10,3,4]
    st.update(1, 10)
    assert st.query(0, 3) == 1 + 10 + 3 + 4
    assert st.query(1, 1) == 10
