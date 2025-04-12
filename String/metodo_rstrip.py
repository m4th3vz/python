# Retorna uma nova string com os espaços em branco (ou caracteres específicos) removidos apenas do final (lado direito) da string.

print("Olá, mundo!   ".rstrip())        # "Olá, mundo!"
print("Python\\n\\t".rstrip())           # "Python"
print("Comando<<<".rstrip("<"))         # "Comando"
print("texto...".rstrip("."))           # "texto"
print("".rstrip())                      # ""
