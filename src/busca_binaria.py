def busca_binaria(lista: list[int], valor: int) -> bool:
    """
    Realiza busca binária em lista ordenada.
    Retorna True se encontrar o valor.
    """
    lista = sorted(lista)
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == valor:
            return True
        elif valor < lista[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1
    
    return False
