# Definindo uma classe chamada Pessoa
class Pessoa:
    # O método __init__ é chamado automaticamente ao criar o objeto
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo da instância
        self.idade = idade

    # Método da classe
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto (instância) da classe Pessoa
p1 = Pessoa("Matheus", 33)

# Chamando o método do objeto
p1.apresentar()

# ➤ Classe é um molde (modelo) para criar objetos.
# ➤ Objetos são instâncias da classe, com seus próprios dados (atributos) e comportamentos (métodos).
