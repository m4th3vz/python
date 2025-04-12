# Insere valores em marcadores {} dentro da string.
# Pode usar índices, nomes de variáveis ou ordem automática.

print("Olá, {}!".format("Matheus"))                        # "Olá, Matheus!"
print("Você tem {} anos.".format(33))                      # "Você tem 33 anos."
print("Número: {}, texto: {}".format(42, "teste"))         # "Número: 42, texto: teste"
print("Nome: {nome}, Idade: {idade}".format(nome="Ana", idade=30))  # "Nome: Ana, Idade: 30"
print("{0} + {0} = {1}".format("Python", "Muito"))          # "Python + Python = Muito"
