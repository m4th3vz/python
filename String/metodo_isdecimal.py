# Retorna True se a string contém apenas números decimais simples (0 a 9). É mais restrito que isdigit() e não reconhece expoentes ou números romanos.

print("123".isdecimal())        # True
print("²".isdecimal())          # False
print("123.45".isdecimal())     # False
