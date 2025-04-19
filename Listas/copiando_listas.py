# ------------------------------------------
# Atribuição direta (vincula as variáveis)
# ------------------------------------------
print("# Atribuição direta (vincula as variáveis)")
lista_original = [1, 2, 3]
lista_vinculada = lista_original  # Ambas apontam para o mesmo objeto

lista_vinculada.append(4)

print("lista_original:", lista_original)   # [1, 2, 3, 4]
print("lista_vinculada:", lista_vinculada) # [1, 2, 3, 4]
print("-" * 40)


# ------------------------------------------
# Cópia usando fatiamento [:]
# ------------------------------------------
print("# Cópia usando fatiamento [:]")
lista_original = [1, 2, 3]
lista_copiada = lista_original[:]

lista_copiada.append(4)

print("lista_original:", lista_original)   # [1, 2, 3]
print("lista_copiada:", lista_copiada)     # [1, 2, 3, 4]
print("-" * 40)


# ------------------------------------------
# Cópia usando list()
# ------------------------------------------
print("# Cópia usando list()")
lista_original = [1, 2, 3]
lista_copiada = list(lista_original)

lista_copiada.append(4)

print("lista_original:", lista_original)   # [1, 2, 3]
print("lista_copiada:", lista_copiada)     # [1, 2, 3, 4]
print("-" * 40)


# ------------------------------------------
# Cópia usando copy()
# ------------------------------------------
print("# Cópia usando copy()")
lista_original = [1, 2, 3]
lista_copiada = lista_original.copy()

lista_copiada.append(4)

print("lista_original:", lista_original)   # [1, 2, 3]
print("lista_copiada:", lista_copiada)     # [1, 2, 3, 4]
print("-" * 40)


# ------------------------------------------
# Cópia profunda (deep copy) com listas aninhadas
# ------------------------------------------
import copy

print("# Cópia profunda (deep copy) com listas aninhadas")
lista_original = [[1, 2], [3, 4]]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0][0] = 99

print("lista_original:", lista_original)   # [[1, 2], [3, 4]]
print("lista_copiada:", lista_copiada)     # [[99, 2], [3, 4]]
print("-" * 40)
