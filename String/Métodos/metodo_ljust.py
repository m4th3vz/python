# Retorna uma nova string alinhada à esquerda dentro de um campo de largura específica, preenchendo o restante com espaços (ou outro caractere, se especificado).

print("python".ljust(10))            # "python    "
print("curso".ljust(12, "-"))        # "curso-------"
print("42".ljust(6, "0"))            # "420000"
print("Matheus".ljust(15, "."))      # "Matheus......."
print("".ljust(4))                   # "    "
