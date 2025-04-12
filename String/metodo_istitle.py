# Retorna True se a string estiver no formato de título:
# cada palavra começa com letra maiúscula seguida de minúsculas.

print("O Pequeno Príncipe".istitle())  # True
print("O pequeno príncipe".istitle())  # False
print("O Pequeno príncipe".istitle())  # False
print("123 Abc".istitle())             # True
print("".istitle())                    # False
