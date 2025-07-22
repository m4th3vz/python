# Definindo uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando uma instância (objeto) da classe Pessoa
p1 = Pessoa("Matheus", 33)

# Usando a instância
p1.apresentar()

# ➤ Instância é um objeto criado a partir de uma classe.
# ➤ Ao escrever p1 = Pessoa("Matheus", 33), estamos instanciando a classe Pessoa.
# ➤ Cada instância tem seus próprios atributos e pode usar os métodos da classe.
