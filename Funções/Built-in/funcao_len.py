# Função len() em Python

"""
len() é usada para obter o comprimento de um objeto iterável (número de itens).
Ela retorna um valor inteiro representando o número de itens no objeto.
"""

# Exemplo 1: Usando len() com uma lista
lista = [1, 2, 3, 4, 5]
print(len(lista))  # 5, porque a lista contém 5 elementos

# Exemplo 2: Usando len() com uma string
texto = "Python"
print(len(texto))  # 6, porque a string 'Python' tem 6 caracteres

# Exemplo 3: Usando len() com uma tupla
tupla = (10, 20, 30, 40)
print(len(tupla))  # 4, porque a tupla contém 4 elementos

# Exemplo 4: Usando len() com um dicionário
dicionario = {"a": 1, "b": 2, "c": 3}
print(len(dicionario))  # 3, porque o dicionário tem 3 chaves

# Exemplo 5: Usando len() com um conjunto
conjunto = {1, 2, 3, 4}
print(len(conjunto))  # 4, porque o conjunto contém 4 elementos (não importa a ordem)

# Exemplo 6: Usando len() com listas aninhadas
listas_aninhadas = [[1, 2], [3, 4, 5], [6]]
print(len(listas_aninhadas))  # 3, porque existem 3 listas dentro da lista principal

# Exemplo 7: Usando len() em objetos personalizados
class MinhaClasse:
    def __init__(self, itens):
        self.itens = itens

    def __len__(self):
        return len(self.itens)

objeto = MinhaClasse([1, 2, 3, 4])
print(len(objeto))  # 4, porque o objeto tem 4 itens

# Exemplo 8: Usando len() em listas vazias
lista_vazia = []
print(len(lista_vazia))  # 0, porque a lista não contém nenhum elemento
