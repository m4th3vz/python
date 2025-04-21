# Função reversed() em Python

"""
A função built-in reversed() retorna um iterador que percorre uma sequência (como uma lista, tupla ou string)
em ordem reversa, ou seja, do último para o primeiro.
O resultado é um objeto reverso (um iterador), que pode ser convertido em outras estruturas de dados, como listas.
"""

# Exemplo 1: Usando reversed() com uma lista
lista = [1, 2, 3, 4, 5]
print("reversed([1, 2, 3, 4, 5]):", list(reversed(lista)))  # Saída: [5, 4, 3, 2, 1]

# Exemplo 2: Usando reversed() com uma string
texto = "Python"
print("reversed('Python'):", "".join(reversed(texto)))  # Saída: nohtyP

# Exemplo 3: Usando reversed() com uma tupla
tupla = (10, 20, 30, 40)
print("reversed((10, 20, 30, 40)):", tuple(reversed(tupla)))  # Saída: (40, 30, 20, 10)

# Exemplo 4: Usando reversed() em um loop
print("Loop com reversed() em uma lista:")
for item in reversed(lista):
    print(item)  # Saída: 5, 4, 3, 2, 1

# Exemplo 5: Tentando com um objeto que não suporta reversão
# O reversed() não funciona em tipos que não são iteráveis ou não têm uma ordem definida.
# Por exemplo, um número inteiro causará erro.
try:
    print(reversed(123))  # Isso vai causar um erro!
except TypeError as e:
    print(f"Erro: {e}")  # Saída: Erro: 'int' object is not iterable

"""
Resumo:
- A função reversed() retorna um iterador reverso, que permite percorrer os elementos de uma sequência na ordem inversa.
- Ela funciona com listas, strings, tuplas e outros tipos iteráveis.
- Para usar o resultado de reversed(), é necessário convertê-lo de volta em uma estrutura de dados, como lista, tupla ou string.
- reversed() é útil quando você precisa percorrer uma sequência de trás para frente, por exemplo, em loops.
"""

# Exemplo prático: Invertendo uma lista de números para verificar se ela é palíndroma
numeros = [1, 2, 3, 2, 1]
if list(reversed(numeros)) == numeros:
    print("A lista é palíndroma!")  # Saída: A lista é palíndroma!
else:
    print("A lista não é palíndroma.")
