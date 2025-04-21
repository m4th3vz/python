# Função super() em Python

"""
A função built-in super() é usada para chamar métodos de uma classe pai (superclasse) a partir de uma classe filha (subclasse).
Ela é frequentemente usada dentro de métodos de subclasses para garantir que o comportamento da classe pai seja mantido, enquanto você pode adicionar ou modificar a funcionalidade.
A sintaxe é: super().método() ou super(classe, instância).método()
"""

# Exemplo 1: Usando super() em uma herança simples
class Animal:
    def fazer_som(self):
        return "Som de animal"

class Cachorro(Animal):
    def fazer_som(self):
        # Chamando o método da classe pai
        som_animal = super().fazer_som()
        return f"{som_animal}, mas com latido!"

# Criando uma instância da subclasse Cachorro
cachorro = Cachorro()
print(cachorro.fazer_som())  # Saída: Som de animal, mas com latido!

# Exemplo 2: Usando super() em um construtor (__init__)
class Veiculo:
    def __init__(self, cor):
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, cor, modelo):
        # Chamando o construtor da classe pai
        super().__init__(cor)
        self.modelo = modelo

# Criando uma instância da subclasse Carro
carro = Carro("vermelho", "Fusca")
print(f"Cor do carro: {carro.cor}, Modelo: {carro.modelo}")
# Saída: Cor do carro: vermelho, Modelo: Fusca

# Exemplo 3: Usando super() com múltiplas heranças
class A:
    def metodo(self):
        print("Método da classe A")

class B:
    def metodo(self):
        print("Método da classe B")

class C(A, B):
    def metodo(self):
        # Chamando o método da classe A usando super()
        super().metodo()

# Criando uma instância da subclasse C
objeto_c = C()
objeto_c.metodo()  # Saída: Método da classe A

# Exemplo 4: Usando super() com múltiplas heranças em uma ordem específica
class D:
    def metodo(self):
        print("Método da classe D")

class E(D):
    def metodo(self):
        print("Método da classe E")
        super().metodo()

class F(E):
    def metodo(self):
        print("Método da classe F")
        super().metodo()

# Criando uma instância da subclasse F
objeto_f = F()
objeto_f.metodo()
# Saída:
# Método da classe F
# Método da classe E
# Método da classe D

"""
Resumo:
- A função super() é usada para acessar métodos de classes pai (superclasses) a partir de subclasses.
- Ela é útil para garantir que o comportamento da classe pai seja preservado, mesmo quando você adicionar novos comportamentos.
- super() também pode ser usada em múltiplas heranças para garantir que a ordem certa de chamadas de métodos seja seguida.
"""

# Exemplo prático: Usando super() para modificar o comportamento de uma classe pai
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        # Chamando o construtor da classe Pessoa
        super().__init__(nome)
        self.curso = curso
    
    def saudacao(self):
        # Chamando o método saudação da classe Pessoa
        saudacao_pessoa = super().saudacao()
        return f"{saudacao_pessoa} e estou estudando {self.curso}!"

# Criando uma instância da subclasse Estudante
estudante = Estudante("Lucas", "Engenharia")
print(estudante.saudacao())  # Saída: Olá, sou Lucas e estou estudando Engenharia!
