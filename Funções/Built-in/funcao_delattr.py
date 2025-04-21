# Função delattr() em Python

"""
A função delattr() é usada para deletar (remover) um atributo de um objeto em Python.
Ela recebe dois parâmetros:
1. O objeto do qual o atributo será removido.
2. O nome do atributo (em formato de string).
Se o atributo não existir no objeto, um erro do tipo AttributeError será gerado.
"""

# Exemplo básico com uma classe

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Criando um objeto da classe Carro
carro1 = Carro("Toyota", "Corolla")

# Verificando os atributos antes de usar delattr()
print("Antes de usar delattr():")
print(f"Marca: {carro1.marca}")  # Saída: Toyota
print(f"Modelo: {carro1.modelo}")  # Saída: Corolla

# Usando delattr() para remover o atributo 'modelo'
delattr(carro1, 'modelo')

print("\nApós usar delattr():")
# Tentando acessar o atributo 'modelo' após a remoção
try:
    print(f"Modelo: {carro1.modelo}")
except AttributeError as e:
    print(f"Erro: {e}")  # Saída: 'Carro' object has no attribute 'modelo'

# Usando delattr() em um atributo inexistente
try:
    delattr(carro1, 'ano')  # O atributo 'ano' não existe no objeto
except AttributeError as e:
    print(f"Erro ao tentar excluir atributo inexistente: {e}")
