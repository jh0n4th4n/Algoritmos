def mdc(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) entre dois inteiros usando o algoritmo de Euclides.
    """
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def mmc(a: int, b: int) -> int:
    """
    Calcula o Mínimo Múltiplo Comum (MMC) entre dois inteiros,
    a partir do MDC.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mdc(a, b)


def calcular_mdc_mmc(a: int, b: int) -> dict:
    """
    Retorna um dicionário contendo MDC e MMC entre dois números.
    """
    return {"MDC": mdc(a, b), "MMC": mmc(a, b)}
