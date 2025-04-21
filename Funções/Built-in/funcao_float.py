# Função float() em Python

"""
A função float() converte um número ou uma string numérica para o tipo float (número decimal).

Sintaxe:
    float(valor)

- valor: pode ser um número inteiro, decimal, string numérica, ou até mesmo um booleano.
"""

# Exemplo 1: Converter inteiro para float
x = 10
print("Int para float:", float(x))  # Saída: 10.0

# Exemplo 2: Converter string numérica
s = "3.14159"
pi = float(s)
print("String para float:", pi)  # Saída: 3.14159

# Exemplo 3: Converter booleanos
print("float(True):", float(True))   # Saída: 1.0
print("float(False):", float(False)) # Saída: 0.0

# Exemplo 4: Usar float para fazer divisão precisa
a = 7
b = 2
resultado = float(a) / b
print("Divisão com float:", resultado)  # Saída: 3.5

# Exemplo 5: Tratando erro com strings inválidas
try:
    valor = float("abc")
except ValueError as e:
    print("Erro ao converter string:", e)
# Saída: Erro ao converter string: could not convert string to float: 'abc'

# Exemplo 6: Usando float() com input
entrada = input("Digite um número decimal: ")
try:
    convertido = float(entrada)
    print("Valor convertido:", convertido)
except ValueError:
    print("Entrada inválida!")
