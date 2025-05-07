# Lista original com elementos duplicados
lista = [1, 2, 2, 3, 1, 5, 4]

print("Lista original:")
print(lista)
print("-" * 40)

# 1. Método clássico com for e if
unicos1 = []
for i in lista:
    if i not in unicos1:
        unicos1.append(i)
print("1. Usando for e if (ordem preservada):")
print(unicos1)
print("-" * 40)

# 2. Usando dict.fromkeys() (preserva a ordem a partir do Python 3.7)
unicos2 = list(dict.fromkeys(lista))
print("2. Usando dict.fromkeys() (ordem preservada):")
print(unicos2)
print("-" * 40)

# 3. Usando set (Cuidado: set não garante ordem! Use sorted() se quiser valores ordenados.)
unicos3 = list(set(lista))
print("3. Usando set() (ordem NÃO garantida):")
print(unicos3)
print("-" * 40)

# 4. Usando set com sorted (remove duplicatas e ordena)
unicos4 = sorted(set(lista))
print("4. Usando set() com sorted() (ordenado):")
print(unicos4)
print("-" * 40)
