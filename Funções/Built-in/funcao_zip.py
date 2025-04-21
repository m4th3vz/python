# Função zip() em Python

"""
A função built-in zip() é usada para combinar iteráveis (como listas, tuplas ou strings) em tuplas, 
onde o primeiro elemento de cada iterável é agrupado em uma tupla, o segundo elemento de cada iterável é agrupado em outra tupla, e assim por diante.
Ela retorna um iterador de tuplas, e é comumente usada para iterar sobre múltiplos iteráveis simultaneamente.
A sintaxe é: zip(iterable1, iterable2, ...)
- iterable1, iterable2, ...: Iteráveis (listas, tuplas, etc.) que você deseja combinar.
"""

# Exemplo 1: Usando zip() para combinar duas listas
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]

# Combinando os dois iteráveis
combinados = zip(nomes, idades)

# Convertendo o iterador resultante para uma lista
combinados_lista = list(combinados)
print("Combinados:", combinados_lista)  
# Saída: Combinados: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Exemplo 2: Usando zip() com mais de dois iteráveis
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
estados = ["SP", "RJ", "MG"]

# Combinando três listas
combinados_3 = zip(nomes, idades, cidades, estados)
combinados_lista_3 = list(combinados_3)
print("Combinados 3:", combinados_lista_3)  
# Saída: Combinados 3: [('Alice', 25, 'São Paulo', 'SP'), ('Bob', 30, 'Rio de Janeiro', 'RJ'), ('Charlie', 35, 'Belo Horizonte', 'MG')]

# Exemplo 3: Usando zip() com iteráveis de tamanhos diferentes
nomes = ["Ana", "Lucas", "Carlos"]
idades = [22, 28]

combinados_diferentes = zip(nomes, idades)
combinados_lista_diferentes = list(combinados_diferentes)
print("Combinados com tamanhos diferentes:", combinados_lista_diferentes)  
# Saída: Combinados com tamanhos diferentes: [('Ana', 22), ('Lucas', 28)]

# Exemplo 4: Desempacotando o resultado do zip()
# Podemos desempacotar os elementos de um zip diretamente em variáveis
nomes, idades = zip(*zip(nomes, idades))
print("Nomes desempacotados:", nomes)  # Saída: Nomes desempacotados: ('Ana', 'Lucas', 'Carlos')
print("Idades desempacotadas:", idades)  # Saída: Idades desempacotadas: (22, 28)

# Exemplo 5: Usando zip() com strings
string1 = "abc"
string2 = "123"

combinados_strings = zip(string1, string2)
combinados_lista_strings = list(combinados_strings)
print("Combinados com strings:", combinados_lista_strings)  
# Saída: Combinados com strings: [('a', '1'), ('b', '2'), ('c', '3')]

"""
Resumo:
- A função zip() combina elementos de múltiplos iteráveis em tuplas.
- Cada tupla contém o i-ésimo elemento de cada um dos iteráveis.
- Se os iteráveis tiverem tamanhos diferentes, o zip() irá parar quando o menor iterável se esgotar.
- Você pode usar zip() para desempacotar elementos de tuplas com a sintaxe *zip().
"""

# Exemplo prático: Usando zip() para criar um dicionário a partir de duas listas
chaves = ["nome", "idade", "cidade"]
valores = ["Ana", 25, "São Paulo"]

dicionario = dict(zip(chaves, valores))
print("Dicionário criado com zip():", dicionario)  
# Saída: Dicionário criado com zip(): {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
