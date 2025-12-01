import heapq
from typing import Dict, Tuple


GrafoPonderado = Dict[str, Dict[str, int]]


def dijkstra(grafo: GrafoPonderado, origem: str) -> Dict[str, Tuple[int, str | None]]:
    """
    Algoritmo de Dijkstra para encontrar a menor distância da origem até
    todos os outros vértices de um grafo ponderado com pesos não negativos.

    :param grafo: dicionário onde a chave é um vértice e o valor é outro dicionário
                  {vizinho: peso}
    :param origem: vértice de origem
    :return: dicionário {vertice: (distancia_minima, anterior_no_caminho)}
    """
    distancias: Dict[str, int] = {v: float("inf") for v in grafo}
    anteriores: Dict[str, str | None] = {v: None for v in grafo}
    distancias[origem] = 0

    fila_prioridade: list[tuple[int, str]] = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return {v: (distancias[v], anteriores[v]) for v in grafo}


def reconstruir_caminho(resultado: Dict[str, Tuple[int, str | None]],
                        origem: str,
                        destino: str) -> list[str]:
    """
    Reconstrói o caminho mínimo da origem até o destino
    a partir do resultado retornado por dijkstra().
    """
    if destino not in resultado or resultado[destino][0] == float("inf"):
        return []

    caminho = [destino]
    atual = destino

    while atual != origem:
        _, anterior = resultado[atual]
        if anterior is None:
            return []
        caminho.append(anterior)
        atual = anterior

    caminho.reverse()
    return caminho
