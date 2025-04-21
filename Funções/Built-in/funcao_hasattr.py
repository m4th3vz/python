# Função hasattr() em Python

"""
hasattr() verifica se um objeto possui um atributo específico.
Sintaxe:
    hasattr(objeto, 'atributo')

- objeto: o objeto que você deseja verificar.
- 'atributo': o nome do atributo como uma string.
"""

# Exemplo 1: Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe Pessoa
p = Pessoa("Matheus", 33)

# Verificando a existência de atributos com hasattr()
print("Tem o atributo 'nome'?", hasattr(p, "nome"))   # Saída: True
print("Tem o atributo 'idade'?", hasattr(p, "idade")) # Saída: True
print("Tem o atributo 'email'?", hasattr(p, "email")) # Saída: False

# Exemplo 2: Usando hasattr() em uma função
def minha_funcao():
    pass

print("A função tem o atributo '__name'?", hasattr(minha_funcao, "__name"))  # Saída: True

# Exemplo 3: Verificando métodos e funções
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando...")

carro = Carro("Fusca")

# Verificando a existência de métodos
print("Carro tem o método 'acelerar'?", hasattr(carro, "acelerar"))  # Saída: True
print("Carro tem o método 'frear'?", hasattr(carro, "frear"))      # Saída: False
