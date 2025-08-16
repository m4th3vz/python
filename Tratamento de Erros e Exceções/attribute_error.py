# Demonstração de AttributeError

objeto = 10
try:
    objeto.append(5)
except AttributeError:
    print("Erro: atributo ou método não existe.")
