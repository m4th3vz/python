# Retorna uma nova string alinhada à direita dentro de um campo de largura específica, preenchendo o restante com espaços (ou outro caractere, se especificado).

print("python".rjust(10))            # "    python"
print("curso".rjust(12, "-"))        # "-------curso"
print("42".rjust(6, "0"))            # "000042"
print("Matheus".rjust(15, "."))      # ".......Matheus"
print("".rjust(4))                   # "    "
