from collections import deque
from typing import Dict, List


GrafoNaoDirigido = Dict[str, List[str]]


def bfs(grafo: GrafoNaoDirigido, inicio: str) -> List[str]:
    """
    Busca em largura (Breadth-First Search) em um grafo não dirigido.

    :param grafo: dicionário onde a chave é um vértice e o valor é a lista de vizinhos
    :param inicio: vértice inicial
    :return: lista de vértices na ordem em que foram visitados
    """
    visitados = set()
    ordem_visita: List[str] = []
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            ordem_visita.append(vertice)

            for vizinho in grafo.get(vertice, []):
                if vizinho not in visitados:
                    fila.append(vizinho)

    return ordem_visita


def dfs(grafo: GrafoNaoDirigido, inicio: str) -> List[str]:
    """
    Busca em profundidade (Depth-First Search) em um grafo não dirigido.

    :param grafo: dicionário onde a chave é um vértice e o valor é a lista de vizinhos
    :param inicio: vértice inicial
    :return: lista de vértices na ordem em que foram visitados
    """
    visitados = set()
    ordem_visita: List[str] = []

    def _dfs_rec(vertice: str) -> None:
        visitados.add(vertice)
        ordem_visita.append(vertice)

        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                _dfs_rec(vizinho)

    _dfs_rec(inicio)
    return ordem_visita
