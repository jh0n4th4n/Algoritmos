class Pilha:
    """
    Implementação simples de uma Pilha (Stack) usando lista Python.
    Opera no modo LIFO (Last In, First Out).
    """

    def __init__(self) -> None:
        self._dados: list[int] = []

    def empilhar(self, valor: int) -> None:
        """Empilha um novo valor no topo da pilha."""
        self._dados.append(valor)

    def desempilhar(self) -> int:
        """
        Remove e retorna o valor do topo da pilha.
        :raises IndexError: se a pilha estiver vazia
        """
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar: pilha vazia.")
        return self._dados.pop()

    def topo(self) -> int:
        """
        Retorna o valor do topo da pilha sem remover.
        :raises IndexError: se a pilha estiver vazia
        """
        if self.esta_vazia():
            raise IndexError("Pilha vazia, não há topo.")
        return self._dados[-1]

    def esta_vazia(self) -> bool:
        """Retorna True se a pilha estiver vazia."""
        return len(self._dados) == 0

    def __len__(self) -> int:
        """Retorna a quantidade de elementos na pilha."""
        return len(self._dados)

    def __repr__(self) -> str:
        """Representação em string da pilha."""
        return f"Pilha({self._dados})"
