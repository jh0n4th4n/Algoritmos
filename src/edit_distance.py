from typing import List


def distancia_edicao(a: str, b: str) -> int:
    """
    Calcula a distância de edição (Levenshtein) entre duas strings.
    Operações permitidas: inserção, remoção e substituição.

    :param a: primeira string
    :param b: segunda string
    :return: número mínimo de operações para transformar a em b
    """
    n, m = len(a), len(b)

    # dp[i][j] = resposta para a[0..i-1] e b[0..j-1]
    dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    # base: transformar vazio em b (inserções) ou a em vazio (remoções)
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            custo_substituicao = 0 if a[i - 1] == b[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,                # remoção
                dp[i][j - 1] + 1,                # inserção
                dp[i - 1][j - 1] + custo_substituicao  # substituição
            )

    return dp[n][m]
