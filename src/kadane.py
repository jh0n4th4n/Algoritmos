from typing import List, Tuple


def maior_soma_subarray(numeros: List[int]) -> Tuple[int, int, int]:
    """
    Implementa o algoritmo de Kadane para encontrar a maior soma de subarray contínuo.

    :param numeros: lista de inteiros
    :return: tupla (maior_soma, indice_inicio, indice_fim)
    """
    if not numeros:
        return 0, 0, -1  # lista vazia

    melhor_soma = numeros[0]
    soma_atual = numeros[0]
    inicio_atual = 0
    melhor_inicio = 0
    melhor_fim = 0

    for i in range(1, len(numeros)):
        if soma_atual + numeros[i] < numeros[i]:
            soma_atual = numeros[i]
            inicio_atual = i
        else:
            soma_atual += numeros[i]

        if soma_atual > melhor_soma:
            melhor_soma = soma_atual
            melhor_inicio = inicio_atual
            melhor_fim = i

    return melhor_soma, melhor_inicio, melhor_fim
