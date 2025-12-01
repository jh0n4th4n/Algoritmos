def eh_palindromo(texto: str) -> bool:
    """
    Verifica se um texto é um palíndromo.
    Ignora espaços, pontuações e diferenças entre maiúsculas/minúsculas.

    :param texto: texto a ser verificado
    :return: True se for palíndromo, False caso contrário
    """
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]
