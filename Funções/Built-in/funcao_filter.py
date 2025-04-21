# Função filter() em Python

"""
A função filter() filtra elementos de um iterável com base em uma função que retorna True ou False.

Sintaxe:
    filter(funcao, iteravel)

- funcao: uma função que retorna True para os elementos que devem ser mantidos.
- iteravel: uma sequência (lista, tupla, string, etc.) a ser filtrada.
"""

# Exemplo 1: Filtrar números pares de uma lista
def eh_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(eh_par, numeros)

# Convertendo o resultado para lista
print("Números pares:", list(pares))
# Saída: Números pares: [2, 4, 6]

# Exemplo 2: Usando filter() com lambda
impares = filter(lambda x: x % 2 != 0, numeros)
print("Números ímpares:", list(impares))
# Saída: Números ímpares: [1, 3, 5]

# Exemplo 3: Filtrar strings com mais de 5 letras
nomes = ["Ana", "Fernando", "Bruno", "Carla", "Beatriz"]
longos = filter(lambda nome: len(nome) > 5, nomes)
print("Nomes longos:", list(longos))
# Saída: Nomes longos: ['Fernando', 'Beatriz']

# Exemplo 4: Filtrar valores não nulos
valores = [None, 0, "", "Python", [], [1, 2], False, True]
nao_vazios = filter(None, valores)
print("Valores não vazios:", list(nao_vazios))
# Saída: Valores não vazios: ['Python', [1, 2], True]

"""
Dica: Quando a função usada no filter() for simples, prefira usar lambda para clareza.
"""

# Exemplo 5: Criar uma nova lista de números positivos
numeros_mistos = [-3, -1, 0, 2, 4, -7]
positivos = list(filter(lambda n: n > 0, numeros_mistos))
print("Números positivos:", positivos)
# Saída: Números positivos: [2, 4]
