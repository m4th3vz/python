# Retorna uma nova string com os espaços em branco removidos do início e do fim da string.
# Também pode remover caracteres específicos, se passados como argumento.

print("   Olá, mundo!   ".strip())     # "Olá, mundo!"
print("\\n\\tPython\\t\\n".strip())     # "Python"
print("$$Dinheiro$$".strip("$"))       # "Dinheiro"
print("...texto...".strip("."))        # "texto"
print("".strip())                      # ""
