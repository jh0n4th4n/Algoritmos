def calcular_lps(padrao: str) -> list[int]:
    """
    Calcula a tabela LPS (Longest Prefix Suffix)
    usada pelo algoritmo KMP.
    """
    lps = [0] * len(padrao)
    comprimento = 0
    i = 1

    while i < len(padrao):
        if padrao[i] == padrao[comprimento]:
            comprimento += 1
            lps[i] = comprimento
            i += 1
        else:
            if comprimento != 0:
                comprimento = lps[comprimento - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_busca(texto: str, padrao: str) -> list[int]:
    """
    Retorna todas as posições em que o padrão ocorre dentro do texto usando o algoritmo KMP.
    """
    if not padrao or not texto:
        return []

    lps = calcular_lps(padrao)
    i = 0  # índice no texto
    j = 0  # índice no padrão
    posicoes: list[int] = []

    while i < len(texto):
        if texto[i] == padrao[j]:
            i += 1
            j += 1

        if j == len(padrao):
            posicoes.append(i - j)
            j = lps[j - 1]  # continua a busca

        elif i < len(texto) and texto[i] != padrao[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return posicoes
