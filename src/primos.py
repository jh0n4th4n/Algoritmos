import math


def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.

    :param n: número inteiro
    :return: True se for primo, False caso contrário
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.isqrt(n))
    for divisor in range(3, limite + 1, 2):
        if n % divisor == 0:
            return False

    return True
