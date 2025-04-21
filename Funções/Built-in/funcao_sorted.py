# Função sorted() em Python

"""
A função built-in sorted() é usada para ordenar os elementos de um iterável (como listas, tuplas, strings) de forma crescente ou decrescente.
Ela retorna uma nova lista com os elementos ordenados, sem modificar o iterável original.
A sintaxe é: sorted(iterable, key=None, reverse=False)
- iterable: O iterável que você deseja ordenar (lista, tupla, string, etc.).
- key: Uma função que será usada para extrair uma chave de comparação para cada elemento. (opcional)
- reverse: Se True, a lista será ordenada em ordem decrescente. (opcional)
"""

# Exemplo 1: Usando sorted() para ordenar uma lista de números
numeros = [5, 2, 9, 1, 5, 6]
lista_ordenada = sorted(numeros)
print("Lista ordenada:", lista_ordenada)  # Saída: [1, 2, 5, 5, 6, 9]

# Exemplo 2: Usando sorted() para ordenar em ordem decrescente
lista_ordenada_descrescente = sorted(numeros, reverse=True)
print("Lista ordenada em ordem decrescente:", lista_ordenada_descrescente)  # Saída: [9, 6, 5, 5, 2, 1]

# Exemplo 3: Usando sorted() em uma lista de strings
frutas = ["banana", "maçã", "laranja", "abacaxi"]
lista_frutas_ordenada = sorted(frutas)
print("Lista de frutas ordenada:", lista_frutas_ordenada)  # Saída: ['abacaxi', 'banana', 'laranja', 'maçã']

# Exemplo 4: Usando sorted() com o parâmetro key
# O parâmetro key é uma função que define como os elementos devem ser comparados.
# Neste caso, vamos ordenar as palavras pelo comprimento delas.
lista_frutas_por_comprimento = sorted(frutas, key=len)
print("Lista de frutas ordenada por comprimento:", lista_frutas_por_comprimento)  # Saída: ['maçã', 'banana', 'laranja', 'abacaxi']

# Exemplo 5: Usando sorted() em uma lista de tuplas
pessoas = [("João", 25), ("Maria", 22), ("Pedro", 30), ("Ana", 20)]
# Ordenando pela idade (segundo elemento da tupla)
pessoas_ordenadas_por_idade = sorted(pessoas, key=lambda pessoa: pessoa[1])
print("Pessoas ordenadas por idade:", pessoas_ordenadas_por_idade)  # Saída: [('Ana', 20), ('Maria', 22), ('João', 25), ('Pedro', 30)]

# Exemplo 6: Usando sorted() em uma string
# A função sorted() também pode ser usada para ordenar os caracteres de uma string.
texto = "python"
caracteres_ordenados = sorted(texto)
print("Texto com caracteres ordenados:", ''.join(caracteres_ordenados))  # Saída: 'hnopty'

"""
Resumo:
- A função sorted() retorna uma nova lista com os elementos de um iterável ordenados.
- Você pode ordenar em ordem crescente ou decrescente utilizando o parâmetro reverse.
- O parâmetro key permite ordenar os elementos com base em uma função específica.
- sorted() funciona em vários tipos de iteráveis como listas, tuplas e strings.
"""

# Exemplo prático: Ordenando um dicionário com base nos valores
dicionario = {"banana": 2, "maçã": 3, "laranja": 1, "abacaxi": 4}
# Ordenando pelas chaves (nomes das frutas)
dicionario_ordenado_por_chave = sorted(dicionario.items(), key=lambda item: item[0])
print("Dicionário ordenado por chave:", dicionario_ordenado_por_chave)
# Saída: [('abacaxi', 4), ('banana', 2), ('laranja', 1), ('maçã', 3)]
