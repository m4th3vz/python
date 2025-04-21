# Função complex() em Python

"""
A função complex() é usada para criar números complexos em Python.
Um número complexo é representado na forma a + bj, onde:
- 'a' é a parte real (um número float ou inteiro).
- 'b' é a parte imaginária (um número float ou inteiro).
- 'j' é a unidade imaginária, que é a raiz quadrada de -1.

Se não for passado valor para a parte imaginária, ela será considerada 0.
"""

# Criando números complexos

# Exemplo 1: Número complexo com parte real e parte imaginária
num1 = complex(2, 3)  # parte real = 2, parte imaginária = 3
print("complex(2, 3) =", num1)  # Saída: (2+3j)

# Exemplo 2: Número complexo apenas com parte real
num2 = complex(5)  # parte real = 5, parte imaginária = 0
print("complex(5) =", num2)  # Saída: (5+0j)

# Exemplo 3: Número complexo com parte imaginária negativa
num3 = complex(1, -4)  # parte real = 1, parte imaginária = -4
print("complex(1, -4) =", num3)  # Saída: (1-4j)

# Exemplo 4: Criando um número complexo a partir de uma string
num4 = complex("3+2j")
print('complex("3+2j") =', num4)  # Saída: (3+2j)

# A parte real e imaginária podem ser acessadas com .real e .imag
print("Parte real de num1:", num1.real)  # Saída: 2.0
print("Parte imaginária de num1:", num1.imag)  # Saída: 3.0

"""
Resumo:
- complex(a, b) cria um número complexo com 'a' como parte real e 'b' como parte imaginária.
- É possível criar números complexos a partir de strings.
- Para acessar as partes, usamos .real e .imag.
"""

# Exemplo prático: Realizando operações com números complexos
soma = num1 + num2
print(f"Soma de num1 e num2: {soma}")  # Saída: (7+3j)

multiplicacao = num1 * num3
print(f"Multiplicação de num1 e num3: {multiplicacao}")  # Saída: (14-5j)
