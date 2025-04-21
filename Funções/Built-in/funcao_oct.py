# Função oct() em Python

"""
A função built-in oct() converte um número inteiro em sua representação octal (base 8),
retornando uma string começando com '0o'.

Sintaxe:
    oct(numero_inteiro)

Ela só funciona com números inteiros (int), incluindo negativos.
"""

# Exemplo 1: Convertendo números positivos
num = 10
print("oct(10) =", oct(num))  # Saída: '0o12'
# Explicação: 10 na base decimal = 1*8 + 2 = 12 na base octal

# Exemplo 2: Convertendo números negativos
num_neg = -25
print("oct(-25) =", oct(num_neg))  # Saída: '-0o31'

# Exemplo 3: Usando oct() para visualizar permissões de arquivos (ex: no Linux)
# Permissões 755 em decimal
permissao = 0o755
print("Permissão em decimal:", permissao)          # Saída: 493
print("Permissão em octal:", oct(permissao))       # Saída: '0o755'

"""
Resumo:
- oct() é usada para converter inteiros em strings no formato octal.
- O prefixo '0o' indica que a string está em base 8.
- É útil em programação de baixo nível, manipulação de bits, e sistemas Unix.
"""
