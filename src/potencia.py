def potencia(base: int, expoente: int) -> int:
    """
    Calcula base^expoente usando recursão.
    """
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)
