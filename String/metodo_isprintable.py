# Retorna True se todos os caracteres da string forem imprimíveis (letras, números, pontuação, espaço).
# Caracteres como quebras de linha (\n), tabulação (\t) ou escape não são considerados imprimíveis.

print("Texto normal".isprintable())     # True
print("1234567890".isprintable())       # True
print("Espaço e pontuação!".isprintable())  # True
print("Linha\nquebrada".isprintable())  # False
print("Tab\tulacao".isprintable())      # False
print("".isprintable())                 # True
