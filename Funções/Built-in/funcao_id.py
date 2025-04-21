# Função id() em Python

"""
id() retorna um número único que representa o identificador de um objeto na memória.
Este valor é único e constante durante a vida útil do objeto, mas pode mudar quando o objeto for destruído e recriado.
"""

# Exemplo 1: Usando id() em variáveis simples
a = 10
b = 10
print("id(a):", id(a))  # id de 'a'
print("id(b):", id(b))  # id de 'b'

# Exemplo 2: id() de diferentes tipos de objetos
texto = "Python"
lista = [1, 2, 3]
print("id(texto):", id(texto))  # id de uma string
print("id(lista):", id(lista))  # id de uma lista

# Exemplo 3: id() e o comportamento de objetos imutáveis e mutáveis
a = [1, 2, 3]
b = a  # 'b' aponta para o mesmo objeto que 'a'
print("id(a):", id(a))  # id de 'a'
print("id(b):", id(b))  # id de 'b' (mesmo valor de id)

a.append(4)  # Alterando a lista
print("id(a) após append:", id(a))  # id de 'a' (não mudou, pois 'b' e 'a' apontam para o mesmo objeto)

# Exemplo 4: id() de objetos criados dinamicamente
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoa1 = Pessoa("Matheus")
pessoa2 = Pessoa("Ana")
print("id(pessoa1):", id(pessoa1))  # id de pessoa1
print("id(pessoa2):", id(pessoa2))  # id de pessoa2

# O id de pessoa1 e pessoa2 são diferentes, porque são objetos diferentes
