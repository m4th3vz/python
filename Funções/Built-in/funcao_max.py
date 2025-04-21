# Função max() em Python

"""
max() retorna o maior valor de um iterável ou o maior de múltiplos valores passados como argumentos.
"""

# Exemplo 1: Usando max() com um único iterável (lista)
numeros = [1, 2, 3, 4, 5]
maior_numero = max(numeros)
print(maior_numero)  # 5, pois 5 é o maior número na lista

# Exemplo 2: Usando max() com múltiplos valores
maior_valor = max(10, 20, 30, 40)
print(maior_valor)  # 40, pois 40 é o maior valor

# Exemplo 3: Usando max() com uma lista de strings
nomes = ["ana", "jose", "maria", "pedro"]
nome_maior = max(nomes)
print(nome_maior)  # "pedro", pois "pedro" é a maior string em ordem lexicográfica

# Exemplo 4: Usando max() com uma função key (ordenando por comprimento da string)
nomes = ["ana", "jose", "maria", "pedro"]
nome_maior_comprimento = max(nomes, key=len)
print(nome_maior_comprimento)  # "maria", pois "maria" tem o maior número de caracteres

# Exemplo 5: Usando max() com um iterável vazio (especificando o valor default)
numeros_vazios = []
maior_com_default = max(numeros_vazios, default=0)
print(maior_com_default)  # 0, pois a lista está vazia, e o valor default foi definido como 0
