from typing import List


def resolver_hanoi(n: int, origem: str, auxiliar: str, destino: str) -> List[str]:
    """
    Resolve o problema da Torre de Hanói e retorna a lista de movimentos.

    :param n: número de discos
    :param origem: nome da haste de origem
    :param auxiliar: nome da haste auxiliar
    :param destino: nome da haste de destino
    :return: lista de strings descrevendo os movimentos
    """
    movimentos: List[str] = []
    _hanoi_rec(n, origem, auxiliar, destino, movimentos)
    return movimentos


def _hanoi_rec(n: int, origem: str, auxiliar: str, destino: str, movimentos: List[str]) -> None:
    if n == 1:
        movimentos.append(f"Mover disco de {origem} para {destino}")
    else:
        _hanoi_rec(n - 1, origem, destino, auxiliar, movimentos)
        movimentos.append(f"Mover disco de {origem} para {destino}")
        _hanoi_rec(n - 1, auxiliar, origem, destino, movimentos)
