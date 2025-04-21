# Função classmethod() em Python

"""
A função classmethod() permite criar métodos de classe, ou seja, métodos que recebem
a própria classe como primeiro parâmetro, em vez de uma instância da classe.
Esses métodos podem ser chamados diretamente na classe, sem necessidade de uma instância.
"""

class Carro:
    # Atributo de classe
    numero_de_rodas = 4

    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    # Método de instância
    def descricao(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Rodas: {self.numero_de_rodas}"

    # Método de classe
    @classmethod
    def descricao_geral(cls):
        return f"Os carros têm {cls.numero_de_rodas} rodas."

# Criando uma instância de Carro
carro = Carro("Fusca", "azul")

# Chamando o método de instância
print(carro.descricao())  # Saída: Modelo: Fusca, Cor: azul, Rodas: 4

# Chamando o método de classe diretamente na classe
print(Carro.descricao_geral())  # Saída: Os carros têm 4 rodas.

# Chamando o método de classe a partir de uma instância
print(carro.descricao_geral())  # Saída: Os carros têm 4 rodas.
