from typing import List


class SegmentTree:
    """
    Implementação simples de Árvore de Segmentos para soma em intervalo
    e atualização de um único ponto.

    Operações suportadas:
    - build a partir de uma lista
    - query(l, r): soma no intervalo [l, r]
    - update(idx, valor): atualiza a posição idx para 'valor'
    """

    def __init__(self, dados: List[int]) -> None:
        self.n = len(dados)
        # próxima potência de 2 >= n (para facilitar o layout da árvore)
        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.seg = [0] * (2 * self.size)
        self._build(dados)

    def _build(self, dados: List[int]) -> None:
        # coloca os dados nas folhas
        for i in range(self.n):
            self.seg[self.size + i] = dados[i]
        # constrói os nós internos
        for i in range(self.size - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def update(self, idx: int, valor: int) -> None:
        """
        Atualiza a posição idx (0-index) para 'valor'.
        """
        pos = self.size + idx
        self.seg[pos] = valor
        pos //= 2
        while pos >= 1:
            self.seg[pos] = self.seg[2 * pos] + self.seg[2 * pos + 1]
            pos //= 2

    def query(self, l: int, r: int) -> int:
        """
        Retorna a soma no intervalo [l, r] (0-index, inclusive).
        """
        l += self.size
        r += self.size
        resultado = 0

        while l <= r:
            if l % 2 == 1:
                resultado += self.seg[l]
                l += 1
            if r % 2 == 0:
                resultado += self.seg[r]
                r -= 1
            l //= 2
            r //= 2

        return resultado
