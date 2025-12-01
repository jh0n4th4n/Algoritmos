from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class No:
    valor: int
    esquerdo: Optional["No"] = None
    direito: Optional["No"] = None


class ArvoreBinariaBusca:
    """
    Implementação de Árvore Binária de Busca (Binary Search Tree - BST).
    """

    def __init__(self) -> None:
        self.raiz: Optional[No] = None

    def inserir(self, valor: int) -> None:
        """Insere um novo valor na BST."""
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no: No, valor: int) -> None:
        if valor < no.valor:
            if no.esquerdo is None:
                no.esquerdo = No(valor)
            else:
                self._inserir_rec(no.esquerdo, valor)
        elif valor > no.valor:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self._inserir_rec(no.direito, valor)
        # se valor == no.valor, não insere (não permite duplicados)

    def buscar(self, valor: int) -> bool:
        """Retorna True se o valor existir na árvore, False caso contrário."""
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, no: Optional[No], valor: int) -> bool:
        if no is None:
            return False
        if valor == no.valor:
            return True
        if valor < no.valor:
            return self._buscar_rec(no.esquerdo, valor)
        return self._buscar_rec(no.direito, valor)

    def em_ordem(self) -> List[int]:
        """Retorna os valores da árvore em ordem crescente."""
        resultado: List[int] = []
        self._em_ordem_rec(self.raiz, resultado)
        return resultado

    def _em_ordem_rec(self, no: Optional[No], resultado: List[int]) -> None:
        if no is None:
            return
        self._em_ordem_rec(no.esquerdo, resultado)
        resultado.append(no.valor)
        self._em_ordem_rec(no.direito, resultado)

    def pre_ordem(self) -> List[int]:
        resultado: List[int] = []
        self._pre_ordem_rec(self.raiz, resultado)
        return resultado

    def _pre_ordem_rec(self, no: Optional[No], resultado: List[int]) -> None:
        if no is None:
            return
        resultado.append(no.valor)
        self._pre_ordem_rec(no.esquerdo, resultado)
        self._pre_ordem_rec(no.direito, resultado)

    def pos_ordem(self) -> List[int]:
        resultado: List[int] = []
        self._pos_ordem_rec(self.raiz, resultado)
        return resultado

    def _pos_ordem_rec(self, no: Optional[No], resultado: List[int]) -> None:
        if no is None:
            return
        self._pos_ordem_rec(no.esquerdo, resultado)
        self._pos_ordem_rec(no.direito, resultado)
        resultado.append(no.valor)

    def __repr__(self) -> str:
        return f"ArvoreBinariaBusca(em_ordem={self.em_ordem()})"
