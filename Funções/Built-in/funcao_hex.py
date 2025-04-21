# Função hex() em Python

"""
hex() converte um número inteiro para uma string representando esse número em base 16 (hexadecimal).
A string retornada começa com '0x', que é um prefixo indicando que o número está em formato hexadecimal.
"""

# Exemplo 1: Convertendo um número inteiro para hexadecimal
numero = 255
hex_numero = hex(numero)
print("Número em hexadecimal:", hex_numero)  # Saída: 0xff

# Exemplo 2: Convertendo números negativos
numero_negativo = -255
hex_numero_negativo = hex(numero_negativo)
print("Número negativo em hexadecimal:", hex_numero_negativo)  # Saída: -0xff

# Exemplo 3: Convertendo um número grande
numero_grande = 123456
hex_numero_grande = hex(numero_grande)
print("Número grande em hexadecimal:", hex_numero_grande)  # Saída: 0x1e240

# Exemplo 4: Convertendo diferentes tipos numéricos
numero_float = 5.75
try:
    print(hex(numero_float))  # Isso vai gerar um erro, pois hex() só funciona com inteiros
except TypeError as e:
    print("Erro:", e)  # Saída: 'float' object cannot be interpreted as an integer

# Exemplo 5: Usando hex() para manipulação de valores em gráficos ou sistemas de cores
cor_decimal = 16711680  # Cor em formato decimal (vermelho puro em RGB)
cor_hexadecimal = hex(cor_decimal)
print("Cor em hexadecimal:", cor_hexadecimal)  # Saída: 0xff0000
