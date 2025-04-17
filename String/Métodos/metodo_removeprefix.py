# Remove o prefixo da string, se ele existir. Caso contrário, retorna a string original.
# Disponível a partir do Python 3.9.

print("https://site.com".removeprefix("https://"))    # "site.com"
print("prefixoTexto".removeprefix("prefixo"))         # "Texto"
print("matheus".removeprefix("ma"))                   # "theus"
print("matheus".removeprefix("xyz"))                  # "matheus" (não muda nada)
print("python".removeprefix(""))                      # "python"
