# Retorna True se a string contém apenas dígitos de 0 a 9. Não aceita sinais negativos, vírgulas ou pontos.

print("123".isdigit())      # True
print("abc".isdigit())      # False
print("123abc".isdigit())   # False
print("-123".isdigit())     # False
