# Função divmod() em Python

"""
A função divmod() em Python recebe dois números como argumentos e retorna uma tupla com dois valores:
1. O quociente da divisão (parte inteira da divisão).
2. O resto da divisão (o que sobra após a divisão).

A sintaxe é:
    divmod(x, y)
    onde:
    - x é o dividendo (número a ser dividido),
    - y é o divisor (número que divide).
"""

# Exemplo 1: Usando divmod() com números inteiros
resultado = divmod(10, 3)
print("divmod(10, 3) =", resultado)
# Saída: divmod(10, 3) = (3, 1)
# 10 dividido por 3 dá 3 (parte inteira), e o resto é 1.

# Exemplo 2: Usando divmod() com números negativos
resultado_negativos = divmod(-10, 3)
print("divmod(-10, 3) =", resultado_negativos)
# Saída: divmod(-10, 3) = (-4, 2)
# -10 dividido por 3 dá -4 (parte inteira), e o resto é 2.

# Exemplo 3: Usando divmod() com números flutuantes (floats)
resultado_float = divmod(10.5, 3)
print("divmod(10.5, 3) =", resultado_float)
# Saída: divmod(10.5, 3) = (3.0, 1.5)
# 10.5 dividido por 3 dá 3.0 (parte inteira) e o resto é 1.5.

# Exemplo 4: Divisão exata
resultado_exato = divmod(12, 4)
print("divmod(12, 4) =", resultado_exato)
# Saída: divmod(12, 4) = (3, 0)
# 12 dividido por 4 dá 3, e o resto é 0.

# Usando divmod() para calcular a quantidade de cédulas em um valor
valor = 99
cedulas = divmod(valor, 50)  # Quantas cédulas de 50 cabem em 99
print(f"99 dividido por 50: {cedulas} cédulas de 50 reais.")
# Saída: (1, 49) -> 1 cédula de 50 reais e sobra 49 reais.

# Exemplo prático: Convertendo minutos em horas e minutos
minutos = 130
horas, minutos_restantes = divmod(minutos, 60)
print(f"130 minutos são {horas} horas e {minutos_restantes} minutos.")
# Saída: 130 minutos são 2 horas e 10 minutos.
