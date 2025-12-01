from typing import List


def busca_linear(lista: List[int], valor: int) -> bool:
    """
    Realiza uma busca linear em uma lista de inteiros.

    :param lista: lista de inteiros
    :param valor: valor a ser buscado
    :return: True se o valor estiver na lista, False caso contrário
    """
    for elemento in lista:
        if elemento == valor:
            return True
    return False
