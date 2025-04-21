# Função range() em Python

"""
A função built-in range() é utilizada para gerar uma sequência de números.
Ela é muito comum em loops, como o for, e é capaz de criar sequências em diferentes intervalos.
O range() pode ser utilizado de três formas:
1. range(stop): Gera números de 0 até stop-1.
2. range(start, stop): Gera números de start até stop-1.
3. range(start, stop, step): Gera números de start até stop-1, incrementando de step em step.
"""

# Exemplo 1: range() com um argumento (stop)
# Gera números de 0 até 4 (stop-1)
print("range(5):", list(range(5)))  # Saída: [0, 1, 2, 3, 4]

# Exemplo 2: range() com dois argumentos (start, stop)
# Gera números de 3 até 7 (stop-1)
print("range(3, 8):", list(range(3, 8)))  # Saída: [3, 4, 5, 6, 7]

# Exemplo 3: range() com três argumentos (start, stop, step)
# Gera números de 0 até 10, com incremento de 2
print("range(0, 11, 2):", list(range(0, 11, 2)))  # Saída: [0, 2, 4, 6, 8, 10]

# Exemplo 4: range() com números negativos
# Gera números de 10 até 1 (step negativo)
print("range(10, 0, -1):", list(range(10, 0, -1)))  # Saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Usando range() em um loop for
print("Loop usando range():")
for i in range(3, 10, 2):
    print(i)  # Saída: 3, 5, 7, 9

"""
Resumo:
- O range() é eficiente em termos de memória, pois ele gera os números sob demanda, e não os mantém na memória.
- Ele é muito usado em loops para iterar sobre um intervalo de números.
- Não inclui o número final (stop), ou seja, a sequência vai de start até stop-1.
"""

# Exemplo prático: Criando uma sequência de índices para acessar uma lista
lista = ["a", "b", "c", "d"]
for i in range(len(lista)):
    print(f"Índice {i} tem o valor: {lista[i]}")
