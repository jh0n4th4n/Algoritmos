from typing import List


def gerar_fibonacci(n: int) -> List[int]:
    """
    Gera uma lista com os n primeiros termos da sequência de Fibonacci.

    :param n: quantidade de termos (n >= 0)
    :return: lista com n termos da sequência
    :raises ValueError: se n for negativo
    """
    if n < 0:
        raise ValueError("A quantidade de termos não pode ser negativa.")

    if n == 0:
        return []

    if n == 1:
        return [0]

    sequencia = [0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia
