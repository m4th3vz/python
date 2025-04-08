# Operadores de Pertinência: in, not in

# Lista
frutas = ["maçã", "banana", "laranja"]

print("maçã" in frutas)        # True
print("uva" not in frutas)     # True

# Tupla
cores = ("vermelho", "azul", "verde")

print("azul" in cores)         # True
print("amarelo" not in cores)  # True

# String
texto = "Python é incrível"

print("Python" in texto)       # True
print("legal" not in texto)    # True

# Dicionário (verifica as chaves)
pessoa = {"nome": "Ana", "idade": 30}

print("nome" in pessoa)        # True
print("altura" not in pessoa)  # True

# Conjunto
numeros = {1, 2, 3, 4, 5}

print(3 in numeros)            # True
print(10 not in numeros)       # True
