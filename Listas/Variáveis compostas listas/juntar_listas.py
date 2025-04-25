# Este script demonstra as principais formas de juntar listas em Python.
# Ele faz parte da categoria "Variáveis Compostas".

# Listas de exemplo
a = [1, 2]
b = [3, 4]

print("Lista a:", a)
print("Lista b:", b)
print()

# 1. Concatenação com operador +
print("# 1. Concatenação com operador '+'")
c = a + b
print("Resultado de a + b:", c)
print()

# 2. Usando o método extend()
print("# 2. Usando o método extend()")
d = a.copy()  # copia para não modificar a original
d.extend(b)
print("Resultado de a.extend(b):", d)
print()

# 3. Usando unpacking com *
print("# 3. Usando unpacking com '*'")
e = [*a, *b]
print("Resultado de [*a, *b]:", e)
print()

# 4. Usando list comprehension
print("# 4. Usando list comprehension")
f = [x for x in a + b]
print("Resultado de list comprehension:", f)
print()

# 5. Usando itertools.chain()
print("# 5. Usando itertools.chain()")
from itertools import chain
g = list(chain(a, b))
print("Resultado de list(chain(a, b)):", g)
print()

# 6. Lista aninhada (listas dentro de uma lista)
print("# 6. Lista aninhada (sem unir elementos)")
h = [a, b]
print("Resultado de [a, b]:", h)
print("Acessando h[0]:", h[0])
print("Acessando h[1]:", h[1])
print()

# Conclusão
print("Esses são os principais métodos para juntar listas em Python.")
print("Escolha a abordagem de acordo com o resultado que você quer obter.")
