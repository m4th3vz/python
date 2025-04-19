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