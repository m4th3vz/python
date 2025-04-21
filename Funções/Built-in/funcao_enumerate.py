# Função enumerate() em Python

"""
A função enumerate() é usada para adicionar um índice a um iterável (como uma lista, tupla, etc.)
e retorna um objeto enumerate que pode ser convertido em uma lista ou utilizado em um loop for.

A sintaxe é:
    enumerate(iterável, start=0)
    onde:
    - iterável: o objeto que será percorrido (como uma lista, tupla, etc.).
    - start: o índice inicial, que é 0 por padrão, mas pode ser alterado.
"""

# Exemplo 1: Usando enumerate() com uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
enumerado_frutas = enumerate(frutas)

# Convertendo o objeto enumerate para uma lista para visualização
print("Enumerate com lista:", list(enumerado_frutas))
# Saída: Enumerate com lista: [(0, 'maçã'), (1, 'banana'), (2, 'laranja'), (3, 'uva')]

# Exemplo 2: Usando enumerate() em um loop for
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
# Saída:
# Índice: 0, Fruta: maçã
# Índice: 1, Fruta: banana
# Índice: 2, Fruta: laranja
# Índice: 3, Fruta: uva

# Exemplo 3: Usando enumerate() com um índice inicial diferente
for indice, fruta in enumerate(frutas, start=1):  # Começando o índice a partir de 1
    print(f"Índice: {indice}, Fruta: {fruta}")
# Saída:
# Índice: 1, Fruta: maçã
# Índice: 2, Fruta: banana
# Índice: 3, Fruta: laranja
# Índice: 4, Fruta: uva

# Exemplo 4: Usando enumerate() com uma tupla
cores = ("azul", "verde", "vermelho")
enumerado_cores = enumerate(cores)

# Convertendo para lista
print("\nEnumerate com tupla:", list(enumerado_cores))
# Saída: Enumerate com tupla: [(0, 'azul'), (1, 'verde'), (2, 'vermelho')]

# Exemplo 5: Usando enumerate() para iterar com índice e valor e fazer algo com eles
# Vamos, por exemplo, criar um dicionário com os índices e os valores da lista
dicionario_frutas = {indice: fruta for indice, fruta in enumerate(frutas)}
print("\nDicionário com índices e valores:", dicionario_frutas)
# Saída: Dicionário com índices e valores: {0: 'maçã', 1: 'banana', 2: 'laranja', 3: 'uva'}
