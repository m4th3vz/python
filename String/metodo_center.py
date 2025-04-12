# Retorna uma nova string centralizada em um campo de largura específica, preenchendo com espaços (ou outro caractere, se especificado) dos dois lados.

print("python".center(10))             # "  python  "
print("curso".center(11, "-"))         # "---curso---"
print("42".center(6, "0"))             # "004200"
print("Matheus".center(15, "."))       # "....Matheus...."
print("".center(4))                    # "    "
