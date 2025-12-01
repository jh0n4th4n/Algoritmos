from typing import Dict, Hashable


class UnionFind:
    """
    Implementação de Disjoint Set Union (Union-Find) com
    path compression e union by rank.

    Útil para:
    - Componentes conectados em grafos
    - Algoritmo de Kruskal (MST)
    - Agrupamentos (clusters) básicos
    """

    def __init__(self) -> None:
        self.pai: Dict[Hashable, Hashable] = {}
        self.rank: Dict[Hashable, int] = {}

    def _criar_conjunto(self, x: Hashable) -> None:
        if x not in self.pai:
            self.pai[x] = x
            self.rank[x] = 0

    def encontrar(self, x: Hashable) -> Hashable:
        """
        Encontra o representante (raiz) do conjunto que contém x.
        Aplica path compression.
        """
        self._criar_conjunto(x)
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x: Hashable, y: Hashable) -> None:
        """
        Une os conjuntos que contêm x e y.
        Usa union by rank.
        """
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)

        if raiz_x == raiz_y:
            return

        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

    def mesmo_conjunto(self, x: Hashable, y: Hashable) -> bool:
        """Retorna True se x e y estiverem no mesmo conjunto."""
        return self.encontrar(x) == self.encontrar(y)
