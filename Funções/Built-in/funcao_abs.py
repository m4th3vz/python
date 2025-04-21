# Função abs() em Python

"""
A função built-in abs() retorna o valor absoluto de um número.

Ou seja, ela remove o sinal de negativo de um número, se houver.
Se o número for positivo, retorna ele mesmo.
Funciona com inteiros, floats e até números complexos.
"""

# Exemplos com números inteiros
num1 = -10
print("abs(-10) =", abs(num1))  # Saída: 10

# Exemplos com números decimais (float)
num2 = -3.14
print("abs(-3.14) =", abs(num2))  # Saída: 3.14

# Exemplos com número positivo
num3 = 7
print("abs(7) =", abs(num3))  # Saída: 7

# Também funciona com números complexos (retorna o módulo)
num4 = 3 - 4j
print("abs(3 - 4j) =", abs(num4))  # Saída: 5.0
# (porque sqrt(3² + (-4)²) = sqrt(9 + 16) = sqrt(25) = 5)

"""
Resumo:
Use abs() sempre que quiser garantir que o valor resultante
de alguma operação será positivo (ou a "distância até zero").
"""

# Exemplo prático: diferença entre dois números, ignorando o sinal
a = 8
b = 13
diferenca = abs(a - b)
print(f"A diferença entre {a} e {b} é {diferenca}")  # Saída: 5
