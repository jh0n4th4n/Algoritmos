from typing import List


def mergesort(lista: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo MergeSort.

    :param lista: lista de inteiros
    :return: nova lista ordenada
    """
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])

    return _intercalar(esquerda, direita)


def _intercalar(esquerda: List[int], direita: List[int]) -> List[int]:
    resultado: List[int] = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
