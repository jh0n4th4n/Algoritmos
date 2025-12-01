def contar_vogais(texto: str) -> int:
    """
    Conta quantas vogais existem em um texto (ignorando maiúsculas/minúsculas).
    """
    vogais = "aeiou"
    return sum(1 for letra in texto.lower() if letra in vogais)
