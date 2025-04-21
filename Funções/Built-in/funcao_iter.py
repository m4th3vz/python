# Função iter() em Python

"""
iter() é usada para obter um iterador de um objeto iterável.
Um objeto iterável é qualquer objeto que pode ser percorrido elemento por elemento, como listas, tuplas, strings, dicionários, etc.
"""

# Exemplo 1: Criando um iterador a partir de uma lista
numeros = [1, 2, 3, 4, 5]
iterador = iter(numeros)  # Criando um iterador a partir da lista

# Usando next() para percorrer os elementos do iterador
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3

# Exemplo 2: Usando iter() com strings
texto = "Python"
iterador_texto = iter(texto)

print(next(iterador_texto))  # 'P'
print(next(iterador_texto))  # 'y'

# Exemplo 3: Usando iter() em um dicionário
dicionario = {"a": 1, "b": 2, "c": 3}
iterador_dict = iter(dicionario)

print(next(iterador_dict))  # 'a' (A primeira chave do dicionário)
print(next(iterador_dict))  # 'b'

# Exemplo 4: Usando iter() com loop for
for valor in numeros:
    print(valor)

# Também podemos usar iter() em loops manualmente
iterador = iter(numeros)
try:
    while True:
        print(next(iterador))
except StopIteration:
    print("Fim da iteração")

# Exemplo 5: Usando iter() com um objeto personalizado
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration  # Levanta uma exceção quando não há mais elementos

contador = Contador(3)
iterador_contador = iter(contador)

# Iterando com next()
print(next(iterador_contador))  # 1
print(next(iterador_contador))  # 2
print(next(iterador_contador))  # 3
try:
    print(next(iterador_contador))  # Levanta StopIteration
except StopIteration:
    print("Fim da contagem")
