# Retorna uma nova string com os espaços em branco (ou caracteres específicos) removidos apenas do início (lado esquerdo) da string.

print("   Olá, mundo!".lstrip())       # "Olá, mundo!"
print("\\n\\tPython".lstrip())          # "Python"
print(">>>Comando".lstrip("><"))       # "Comando"
print("...texto".lstrip("."))          # "texto"
print("".lstrip())                     # ""
