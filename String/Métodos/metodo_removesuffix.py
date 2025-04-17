# Remove o sufixo da string, se ele existir. Caso contrário, retorna a string original.
# Disponível a partir do Python 3.9.

print("arquivo.txt".removesuffix(".txt"))      # "arquivo"
print("nome-final".removesuffix("-final"))     # "nome"
print("matheus".removesuffix("us"))            # "mathe"
print("matheus".removesuffix("abc"))           # "matheus" (não muda nada)
print("texto".removesuffix(""))                # "texto"
