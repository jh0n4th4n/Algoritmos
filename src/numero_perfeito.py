def numero_perfeito(n: int) -> bool:
    """
    Verifica se um número é perfeito (ex.: 6 -> 1 + 2 + 3 = 6).
    """
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n
