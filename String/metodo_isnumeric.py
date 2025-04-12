# Retorna True se a string contém qualquer tipo de número: dígitos, expoentes (²), frações ou romanos (Ⅻ). É mais amplo que isdigit().

print("123".isnumeric())        # True
print("Ⅻ".isnumeric())          # True   # número romano 12
print("²".isnumeric())          # True   # expoente 2
print("123abc".isnumeric())     # False
