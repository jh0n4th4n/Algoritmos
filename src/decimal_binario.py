def decimal_para_binario(n: int) -> str:
    """
    Converte um número inteiro decimal para sua representação binária em string,
    sem usar a função builtin bin().

    :param n: número inteiro >= 0
    :return: string representando o número em binário
    :raises ValueError: se n for negativo
    """
    if n < 0:
        raise ValueError("Apenas números inteiros não negativos são suportados.")

    if n == 0:
        return "0"

    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2

    bits.reverse()
    return "".join(bits)
