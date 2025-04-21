# Função map() em Python

"""
map() é usada para aplicar uma função a cada item de um iterável e retorna um novo iterável com os resultados.
"""

# Exemplo 1: Aplicando uma função simples a cada item de uma lista
def quadrado(x):
    return x ** 2

lista = [1, 2, 3, 4, 5]
resultado = map(quadrado, lista)

# Como map() retorna um iterador, usamos list() para visualizar o resultado
print(list(resultado))  # [1, 4, 9, 16, 25]

# Exemplo 2: Usando lambda para aplicar uma função anônima
lista2 = [10, 20, 30, 40]
resultado2 = map(lambda x: x + 5, lista2)
print(list(resultado2))  # [15, 25, 35, 45], adiciona 5 a cada elemento

# Exemplo 3: Usando map() com múltiplos iteráveis
lista3 = [1, 2, 3, 4]
lista4 = [5, 6, 7, 8]
resultado3 = map(lambda x, y: x + y, lista3, lista4)
print(list(resultado3))  # [6, 8, 10, 12], soma os elementos correspondentes de cada lista

# Exemplo 4: Usando map() para converter todos os elementos de uma lista para strings
numeros = [1, 2, 3, 4, 5]
resultado4 = map(str, numeros)
print(list(resultado4))  # ['1', '2', '3', '4', '5'], converte todos os números para strings

# Exemplo 5: Usando map() para aplicar uma função a uma lista de strings
nomes = ["ana", "jose", "maria"]
resultado5 = map(lambda nome: nome.upper(), nomes)
print(list(resultado5))  # ['ANA', 'JOSE', 'MARIA'], converte todos os nomes para maiúsculas
