# Função list() em Python

"""
list() é usada para criar uma lista a partir de um objeto iterável.
Ela retorna uma nova lista contendo todos os itens do objeto iterável fornecido.
"""

# Exemplo 1: Convertendo uma tupla para uma lista
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
print(lista)  # [1, 2, 3, 4, 5], a tupla foi convertida para uma lista

# Exemplo 2: Convertendo uma string para uma lista de caracteres
texto = "Python"
lista_texto = list(texto)
print(lista_texto)  # ['P', 'y', 't', 'h', 'o', 'n'], cada caractere da string vira um elemento da lista

# Exemplo 3: Convertendo um conjunto (set) para uma lista
conjunto = {1, 2, 3, 4}
lista_conjunto = list(conjunto)
print(lista_conjunto)  # [1, 2, 3, 4] (em uma ordem não garantida, já que os conjuntos não mantêm ordem)

# Exemplo 4: Convertendo um intervalo (range) para uma lista
intervalo = range(1, 6)
lista_intervalo = list(intervalo)
print(lista_intervalo)  # [1, 2, 3, 4, 5], converte o intervalo em uma lista

# Exemplo 5: Convertendo um dicionário para uma lista de chaves
dicionario = {"a": 1, "b": 2, "c": 3}
lista_chaves = list(dicionario)
print(lista_chaves)  # ['a', 'b', 'c'], os dicionários se convertem em listas das suas chaves

# Exemplo 6: Criando uma lista a partir de um iterador
iterador = iter([10, 20, 30])
lista_iterador = list(iterador)
print(lista_iterador)  # [10, 20, 30], converte o iterador em uma lista

# Exemplo 7: Criando uma lista vazia
lista_vazia = list()
print(lista_vazia)  # [], uma lista vazia

# Exemplo 8: Usando list() com compreensão de listas
compreensao_lista = list(x * 2 for x in range(5))
print(compreensao_lista)  # [0, 2, 4, 6, 8], cria uma lista com os valores dobrados de 0 a 4
