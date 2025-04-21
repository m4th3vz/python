# Função set() em Python

"""
A função built-in set() é usada para criar um conjunto (set) em Python.
Conjuntos são coleções não ordenadas de elementos únicos (sem repetições).
Eles são úteis quando você precisa garantir que não haverá valores duplicados.
"""

# Exemplo 1: Criando um conjunto a partir de uma lista com valores duplicados
lista = [1, 2, 3, 3, 4, 5, 5]
conjunto = set(lista)
print("set([1, 2, 3, 3, 4, 5, 5]) =", conjunto)  # Saída: {1, 2, 3, 4, 5}

# Exemplo 2: Criando um conjunto com elementos diferentes
conjunto2 = set([10, 20, 30, 40])
print("set([10, 20, 30, 40]) =", conjunto2)  # Saída: {40, 10, 20, 30}

# Exemplo 3: Criando um conjunto a partir de uma string
# As strings são iteráveis, então cada caractere será um elemento no conjunto.
conjunto3 = set("abracadabra")
print("set('abracadabra') =", conjunto3)  # Saída: {'a', 'b', 'r', 'c', 'd'}

# Exemplo 4: Operações com conjuntos (União, Interseção, Diferença)
conjuntoA = {1, 2, 3, 4}
conjuntoB = {3, 4, 5, 6}

# União (todos os elementos de A e B)
uniao = conjuntoA | conjuntoB
print("União (A | B):", uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção (elementos comuns a A e B)
intersecao = conjuntoA & conjuntoB
print("Interseção (A & B):", intersecao)  # Saída: {3, 4}

# Diferença (elementos de A que não estão em B)
diferenca = conjuntoA - conjuntoB
print("Diferença (A - B):", diferenca)  # Saída: {1, 2}

# Exemplo 5: Usando set() para verificar se uma lista tem elementos duplicados
lista_com_duplicados = [1, 2, 3, 4, 4, 5]
tem_duplicados = len(lista_com_duplicados) != len(set(lista_com_duplicados))
print("A lista tem duplicados?", tem_duplicados)  # Saída: True

"""
Resumo:
- A função set() cria um conjunto com elementos únicos.
- Conjuntos são desordenados, então a ordem dos elementos não é garantida.
- Você pode realizar várias operações em conjuntos, como união, interseção e diferença.
- Conjuntos são muito úteis quando você precisa garantir que não haja duplicação de elementos.
"""

# Exemplo prático: Removendo duplicatas de uma lista mantendo os elementos únicos
lista_com_duplicados = [1, 2, 3, 4, 4, 5]
lista_sem_duplicados = list(set(lista_com_duplicados))
print("Lista sem duplicados:", lista_sem_duplicados)  # Saída: [1, 2, 3, 4, 5]
