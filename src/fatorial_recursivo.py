def calcular_fatorial_recursivo(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo usando recursão.

    :param n: número inteiro >= 0
    :return: fatorial de n
    :raises ValueError: se n for negativo
    """
    if n < 0:
        raise ValueError("Não existe fatorial de número negativo.")
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial_recursivo(n - 1)
