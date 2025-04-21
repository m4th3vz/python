# Função sum() em Python

"""
A função built-in sum() é usada para somar os elementos de um iterável (como listas, tuplas ou conjuntos).
Ela retorna a soma de todos os elementos, podendo também receber um valor inicial que será somado ao total.
A sintaxe é: sum(iterable, start=0)
- iterable: O iterável cujos elementos serão somados.
- start: Um valor inicial (opcional), que será somado ao total. O valor padrão é 0.
"""

# Exemplo 1: Somando os elementos de uma lista de números
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print("Soma dos números:", soma)  # Saída: 15

# Exemplo 2: Somando os elementos de uma lista com um valor inicial
soma_com_valor_inicial = sum(numeros, 10)
print("Soma dos números com valor inicial 10:", soma_com_valor_inicial)  # Saída: 25

# Exemplo 3: Somando os elementos de uma tupla
tupla = (2, 4, 6, 8)
soma_tupla = sum(tupla)
print("Soma da tupla:", soma_tupla)  # Saída: 20

# Exemplo 4: Somando os elementos de um conjunto (set)
conjunto = {5, 10, 15, 20}
soma_conjunto = sum(conjunto)
print("Soma do conjunto:", soma_conjunto)  # Saída: 50

# Exemplo 5: Usando sum() com valores negativos
numeros_negativos = [-1, -2, -3, -4, -5]
soma_negativa = sum(numeros_negativos)
print("Soma dos números negativos:", soma_negativa)  # Saída: -15

# Exemplo 6: Usando sum() para somar com números flutuantes
numeros_float = [1.5, 2.5, 3.5, 4.5]
soma_float = sum(numeros_float)
print("Soma dos números float:", soma_float)  # Saída: 12.0

# Exemplo 7: Somando os valores de uma lista de dicionários (usando uma chave específica)
dicionarios = [{"valor": 10}, {"valor": 20}, {"valor": 30}]
soma_dicionarios = sum(d["valor"] for d in dicionarios)
print("Soma dos valores no dicionário:", soma_dicionarios)  # Saída: 60

"""
Resumo:
- A função sum() soma os elementos de um iterável (lista, tupla, conjunto, etc.).
- Você pode passar um valor inicial (start) que será somado ao total.
- Por padrão, o valor inicial é 0.
- sum() funciona bem para somar números inteiros e de ponto flutuante.
"""

# Exemplo prático: Usando sum() para calcular a soma de uma lista de distâncias percorridas
distancias = [5.5, 10.3, 8.7, 12.4]
distancia_total = sum(distancias)
print("Distância total percorrida:", distancia_total)  # Saída: 36.9
