import pytest

from src.fatorial import calcular_fatorial
from src.fibonacci import gerar_fibonacci
from src.primos import eh_primo
from src.ordenacao import ordenar_lista
from src.palindromo import eh_palindromo
from src.mdc_mmc import mdc, mmc, calcular_mdc_mmc
from src.busca_linear import busca_linear
from src.quicksort import quicksort
from src.contagem_vogais import contar_vogais
from src.inverter_string import inverter_string
from src.potencia import potencia
from src.numero_perfeito import numero_perfeito
from src.busca_binaria import busca_binaria
from src.fatorial_recursivo import calcular_fatorial_recursivo
from src.decimal_binario import decimal_para_binario
from src.mergesort import mergesort
from src.hanoi import resolver_hanoi
from src.pilha import Pilha


# ----------------- FATORIAL ----------------- #

def test_calcular_fatorial_valores_basicos():
    assert calcular_fatorial(0) == 1
    assert calcular_fatorial(1) == 1
    assert calcular_fatorial(5) == 120


def test_calcular_fatorial_valor_invalido():
    with pytest.raises(ValueError):
        calcular_fatorial(-1)


def test_calcular_fatorial_recursivo():
    assert calcular_fatorial_recursivo(0) == 1
    assert calcular_fatorial_recursivo(1) == 1
    assert calcular_fatorial_recursivo(5) == 120


# ----------------- FIBONACCI ----------------- #

def test_gerar_fibonacci():
    assert gerar_fibonacci(0) == []
    assert gerar_fibonacci(1) == [0]
    assert gerar_fibonacci(2) == [0, 1]
    assert gerar_fibonacci(5) == [0, 1, 1, 2, 3]


def test_gerar_fibonacci_invalido():
    with pytest.raises(ValueError):
        gerar_fibonacci(-1)


# ----------------- PRIMOS ----------------- #

def test_eh_primo():
    assert eh_primo(2) is True
    assert eh_primo(3) is True
    assert eh_primo(5) is True
    assert eh_primo(4) is False
    assert eh_primo(1) is False
    assert eh_primo(0) is False
    assert eh_primo(-7) is False


# ----------------- ORDENAÇÃO ----------------- #

def test_ordenar_lista_bubble_sort():
    assert ordenar_lista([]) == []
    assert ordenar_lista([1]) == [1]
    assert ordenar_lista([3, 2, 1]) == [1, 2, 3]
    assert ordenar_lista([5, -1, 3, 0]) == [-1, 0, 3, 5]


def test_quicksort():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([5, -1, 3, 0]) == [-1, 0, 3, 5]
    assert quicksort([3, 3, 1]) == [1, 3, 3]


def test_mergesort():
    assert mergesort([]) == []
    assert mergesort([1]) == [1]
    assert mergesort([3, 2, 1]) == [1, 2, 3]
    assert mergesort([5, -1, 3, 0]) == [-1, 0, 3, 5]


# ----------------- PALÍNDROMO ----------------- #

def test_eh_palindromo():
    assert eh_palindromo("arara") is True
    assert eh_palindromo("Arara") is True
    assert eh_palindromo("Socorram me subi no onibus em Marrocos") is True
    assert eh_palindromo("python") is False


# ----------------- MDC / MMC ----------------- #

def test_mdc_mmc():
    assert mdc(12, 18) == 6
    assert mmc(12, 18) == 36
    resultado = calcular_mdc_mmc(12, 18)
    assert resultado["MDC"] == 6
    assert resultado["MMC"] == 36


# ----------------- BUSCAS ----------------- #

def test_busca_linear():
    lista = [10, 20, 30, 40]
    assert busca_linear(lista, 10) is True
    assert busca_linear(lista, 25) is False


def test_busca_binaria():
    lista = [5, 1, 4, 2, 3]
    assert busca_binaria(lista, 3) is True
    assert busca_binaria(lista, 10) is False


# ----------------- STRINGS / TEXTO ----------------- #

def test_contar_vogais():
    assert contar_vogais("Olá Mundo") == 3
    assert contar_vogais("BCDF") == 0
    assert contar_vogais("") == 0


def test_inverter_string():
    assert inverter_string("abc") == "cba"
    assert inverter_string("") == ""
    assert inverter_string("radar") == "radar"


# ----------------- POTÊNCIA ----------------- #

def test_potencia():
    assert potencia(2, 0) == 1
    assert potencia(2, 3) == 8
    assert potencia(5, 1) == 5


# ----------------- NÚMERO PERFEITO ----------------- #

def test_numero_perfeito():
    assert numero_perfeito(6) is True
    assert numero_perfeito(28) is True
    assert numero_perfeito(8) is False
    assert numero_perfeito(1) is False


# ----------------- DECIMAL -> BINÁRIO ----------------- #

def test_decimal_para_binario():
    assert decimal_para_binario(0) == "0"
    assert decimal_para_binario(1) == "1"
    assert decimal_para_binario(2) == "10"
    assert decimal_para_binario(10) == "1010"


def test_decimal_para_binario_invalido():
    with pytest.raises(ValueError):
        decimal_para_binario(-1)


# ----------------- TORRE DE HANÓI ----------------- #

def test_resolver_hanoi():
    movimentos_1 = resolver_hanoi(1, "A", "B", "C")
    assert len(movimentos_1) == 1

    movimentos_3 = resolver_hanoi(3, "A", "B", "C")
    # Pra n discos, número de movimentos = 2^n - 1
    assert len(movimentos_3) == 7
    assert movimentos_3[0].startswith("Mover disco de")
    assert movimentos_3[-1].startswith("Mover disco de")


# ----------------- PILHA ----------------- #

def test_pilha_basico():
    pilha = Pilha()
    assert pilha.esta_vazia() is True
    pilha.empilhar(10)
    pilha.empilhar(20)
    assert len(pilha) == 2
    assert pilha.topo() == 20
    assert pilha.desempilhar() == 20
    assert pilha.desempilhar() == 10
    assert pilha.esta_vazia() is True


def test_pilha_desempilhar_vazia():
    pilha = Pilha()
    with pytest.raises(IndexError):
        pilha.desempilhar()
