def encontrar_repetidos(lista):
    vistos = set()
    repetidos = set()

    for numero in lista:
        if numero in vistos:
            repetidos.add(numero)
        else:
            vistos.add(numero)
    
    return list(repetidos)
    # Se não usarmos 'return', a função não saberá qual resultado deve ser devolvido:
    # se é o conteúdo de 'repetidos', de 'vistos', ou nenhum deles.
    # Em Python, quando não há 'return', o retorno padrão é 'None'.
    # Por isso, usamos 'return list(repetidos)' para indicar que queremos que
    # o resultado da função seja especificamente os números repetidos encontrados.

a = [1, 2, 3, 4, 4, 4, 5, 5]
b = encontrar_repetidos(a)

print("Números repetidos:", b)
