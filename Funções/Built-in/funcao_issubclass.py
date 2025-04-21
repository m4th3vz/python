# Função issubclass() em Python

"""
issubclass() é usada para verificar se uma classe é uma subclasse de outra classe.
Ela retorna True se a classe especificada for uma subclasse direta ou indireta da classe fornecida.
"""

# Exemplo 1: Verificando a relação de herança simples
class Animal:
    pass

class Cachorro(Animal):
    pass

print(issubclass(Cachorro, Animal))  # True, porque 'Cachorro' é uma subclasse de 'Animal'
print(issubclass(Animal, Cachorro))  # False, porque 'Animal' não é subclasse de 'Cachorro'

# Exemplo 2: Verificando uma subclasse indireta
class Mamifero(Animal):
    pass

print(issubclass(Cachorro, Mamifero))  # True, porque 'Cachorro' é uma subclasse de 'Mamifero' que é subclasse de 'Animal'

# Exemplo 3: Verificando herança múltipla
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(issubclass(C, A))  # True, porque 'C' herda de 'A'
print(issubclass(C, B))  # True, porque 'C' herda de 'B'

# Exemplo 4: Usando issubclass() para validar tipos de classes
class Veiculo:
    pass

class Carro(Veiculo):
    pass

# Verificando se Carro é subclasse de Veiculo
if issubclass(Carro, Veiculo):
    print("Carro é um tipo de Veiculo!")

# Exemplo 5: Verificando se uma classe é subclasse de `object`
# Em Python, todas as classes herdam de `object` implicitamente
print(issubclass(Carro, object))  # True, porque toda classe herda de 'object'
