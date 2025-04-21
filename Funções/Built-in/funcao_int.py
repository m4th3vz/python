# Função int() em Python

"""
int() é usada para converter valores para inteiros.
Ela pode converter strings numéricas, floats ou até números em diferentes bases para inteiros.
"""

# Exemplo 1: Convertendo uma string para inteiro
numero_str = "42"
numero_int = int(numero_str)  # Converte a string "42" para o número inteiro 42
print("Número convertido de string:", numero_int)

# Exemplo 2: Convertendo um número flutuante para inteiro
numero_float = 3.14159
numero_int = int(numero_float)  # Converte o número float para inteiro, descartando a parte decimal
print("Número convertido de float:", numero_int)  # Saída: 3

# Exemplo 3: Convertendo números em bases diferentes (binário, octal, hexadecimal)
# Converting binary string to int (base 2)
binario = "1010"
numero_binario = int(binario, 2)  # A string '1010' em binário representa o número 10 em decimal
print(f"Binário {binario} convertido para inteiro:", numero_binario)

# Convertendo hexadecimal para inteiro
hexadecimal = "1f"
numero_hex = int(hexadecimal, 16)  # A string '1f' em hexadecimal representa o número 31 em decimal
print(f"Hexadecimal {hexadecimal} convertido para inteiro:", numero_hex)

# Exemplo 4: Usando int() com valor default (0)
numero_invalido = "não é número"
try:
    numero_int = int(numero_invalido)  # Vai gerar um erro porque a string não pode ser convertida para um inteiro
except ValueError as e:
    print("Erro de conversão:", e)

# Exemplo 5: Convertendo valores numéricos com diferentes bases
octal = "17"  # O número octal 17 representa 15 em decimal
numero_octal = int(octal, 8)  # Convertendo de octal para decimal
print(f"Octal {octal} convertido para inteiro:", numero_octal)
