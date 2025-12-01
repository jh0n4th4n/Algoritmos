from typing import List


def ordenar_lista(lista: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo Bubble Sort.

    :param lista: lista de números inteiros
    :return: nova lista ordenada em ordem crescente
    """
    # Faz uma cópia para não alterar a lista original
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        trocou = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True

        # Se nenhuma troca foi feita, a lista já está ordenada
        if not trocou:
            break

    return arr
