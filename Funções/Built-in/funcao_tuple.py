# Função tuple() em Python

"""
A função built-in tuple() é usada para criar uma tupla em Python. 
Uma tupla é uma coleção ordenada e imutável de elementos, que pode conter qualquer tipo de dados.
A sintaxe é: tuple(iterable)
- iterable: Qualquer iterável (lista, string, etc.) que será convertido para uma tupla.
"""

# Exemplo 1: Convertendo uma lista para tupla
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print("Tupla criada a partir da lista:", tupla)  # Saída: (1, 2, 3, 4, 5)

# Exemplo 2: Convertendo uma string para tupla
string = "Python"
tupla_string = tuple(string)
print("Tupla criada a partir da string:", tupla_string)  # Saída: ('P', 'y', 't', 'h', 'o', 'n')

# Exemplo 3: Criando uma tupla diretamente
tupla_direta = (10, 20, 30)
print("Tupla direta:", tupla_direta)  # Saída: (10, 20, 30)

# Exemplo 4: Convertendo um conjunto (set) para tupla
conjunto = {7, 8, 9}
tupla_conjunto = tuple(conjunto)
print("Tupla criada a partir do conjunto:", tupla_conjunto)  # Saída: (7, 8, 9) (a ordem pode variar)

# Exemplo 5: Tupla vazia
tupla_vazia = tuple()
print("Tupla vazia:", tupla_vazia)  # Saída: ()

# Exemplo 6: Tupla com um único elemento
tupla_unica = (42,)
print("Tupla com um único elemento:", tupla_unica)  # Saída: (42,)

# Exemplo 7: Tupla com múltiplos tipos de dados
tupla_mista = (1, "Python", 3.14, True)
print("Tupla com múltiplos tipos de dados:", tupla_mista)  # Saída: (1, 'Python', 3.14, True)

"""
Resumo:
- A função tuple() converte um iterável (como lista, string, ou conjunto) em uma tupla.
- Tuplas são imutáveis, ou seja, não podem ser alteradas após sua criação.
- Tuplas podem conter elementos de tipos diferentes, como inteiros, strings, listas, etc.
- Uma tupla com um único elemento deve ter uma vírgula após o elemento (por exemplo, (42,)) para ser reconhecida como tupla.
"""

# Exemplo prático: Usando tuplas para armazenar dados imutáveis
dados_pessoa = ("Maria", 25, "Brasil")
nome, idade, pais = dados_pessoa
print(f"Nome: {nome}, Idade: {idade}, País: {pais}")
# Saída: Nome: Maria, Idade: 25, País: Brasil
