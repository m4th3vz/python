# Junta os itens de uma sequência (como listas ou tuplas) em uma única string, usando a string que chama o método como separador.

print("-".join(["um", "dois", "três"]))         # "um-dois-três"
print(" ".join(("Python", "é", "legal")))       # "Python é legal"
print("".join(["a", "b", "c"]))                 # "abc"
print(", ".join("ABC"))                         # "A, B, C"
print("X".join([]))                             # ""
