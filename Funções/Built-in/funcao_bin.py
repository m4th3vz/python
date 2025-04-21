# Função bin() em Python

"""
A função built-in bin() converte um número inteiro para sua representação binária.
A saída é uma string que começa com '0b' para indicar que é um número binário.
"""

# Exemplo com números inteiros positivos
num1 = 10
print("bin(10) =", bin(num1))  # Saída: '0b1010'

# Exemplo com número zero
num2 = 0
print("bin(0) =", bin(num2))  # Saída: '0b0'

# Exemplo com números negativos
num3 = -5
print("bin(-5) =", bin(num3))  # Saída: '-0b101'

"""
A função bin() sempre retorna um número binário precedido de '0b', indicando a base binária.
Porém, a conversão de números negativos segue a notação de complemento de 2.
"""

# Exemplo de números maiores
num4 = 255
print("bin(255) =", bin(num4))  # Saída: '0b11111111'

# Exemplo com um número grande
num5 = 1024
print("bin(1024) =", bin(num5))  # Saída: '0b10000000000'

"""
Resumo:
- bin() converte inteiros em suas representações binárias.
- Ideal para trabalhar com operações de bit, como máscaras de bits, manipulação de dados binários, etc.
"""

# Exemplo prático: verificar se um número é par ou ímpar usando binário
numero = 7
print(f"binário de {numero}: {bin(numero)}")
if bin(numero)[-1] == '0':
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
