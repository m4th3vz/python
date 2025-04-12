# Esse método verifica se a string começa com uma certa sequência de caracteres (ou apenas um caractere). É útil para checar, por exemplo, se o número digitado tem um sinal negativo.

print("Matheus".startswith("Mat"))  # True
print("-123".startswith("-"))       # True
print("123".startswith("-"))        # False
