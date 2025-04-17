# Retorna True se a string contém apenas espaços, quebras de linha (\n), tabulações (\t) ou outros caracteres de espaço em branco.

print("   ".isspace())          # True
print("\n\t".isspace())         # True
print(" abc ".isspace())        # False
print("".isspace())             # False   # string vazia não conta
