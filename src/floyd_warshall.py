from typing import List


INF = float("inf")


def floyd_warshall(matriz_adj: List[List[float]]) -> List[List[float]]:
    """
    Implementa o algoritmo de Floyd–Warshall para encontrar
    as menores distâncias entre todos os pares de vértices.

    :param matriz_adj: matriz de adjacência contendo pesos das arestas.
                       Use INF (float('inf')) para ausência de aresta.
                       A diagonal deve ser 0.
    :return: matriz de distâncias mínimas.
    """
    n = len(matriz_adj)
    # cria uma cópia para não modificar a matriz original
    dist = [[matriz_adj[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
