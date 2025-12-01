from typing import List


def quicksort(lista: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo QuickSort (versão recursiva).

    :param lista: lista de inteiros
    :return: nova lista ordenada
    """
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    return quicksort(esquerda) + meio + quicksort(direita)
