# Função isinstance() em Python

"""
isinstance() é usada para verificar se um objeto é uma instância de uma classe ou de uma tupla de classes.
Ela retorna True se o objeto for uma instância da classe especificada ou de suas subclasses.
"""

# Exemplo 1: Verificando se um objeto é uma instância de uma classe
numero = 42
print(isinstance(numero, int))  # True, porque 42 é um inteiro

# Exemplo 2: Verificando se uma lista é uma instância de uma classe
lista = [1, 2, 3]
print(isinstance(lista, list))  # True, porque 'lista' é uma lista

# Exemplo 3: Verificando se um objeto é uma instância de mais de uma classe
texto = "Olá"
print(isinstance(texto, (int, str)))  # True, porque 'texto' é uma string (str)

# Exemplo 4: Verificando com herança
class Animal:
    pass

class Cachorro(Animal):
    pass

dog = Cachorro()
print(isinstance(dog, Cachorro))  # True, porque 'dog' é uma instância de Cachorro
print(isinstance(dog, Animal))    # True, porque 'Cachorro' herda de 'Animal'

# Exemplo 5: Usando isinstance() para verificar tipos compostos
numeros = [1, 2, 3]
print(isinstance(numeros, (list, tuple)))  # True, porque 'numeros' é uma lista

# Exemplo 6: Usando isinstance() para evitar erros de tipo
def processar_item(item):
    if isinstance(item, int):
        return item * 2
    elif isinstance(item, str):
        return item.upper()
    else:
        raise TypeError("Tipo de dado não suportado")

print(processar_item(5))   # 10
print(processar_item("abc"))  # ABC
