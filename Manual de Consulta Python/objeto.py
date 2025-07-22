# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Matheus", 33)

# Usando o objeto
pessoa1.apresentar()

# ➤ Objeto é uma instância de uma classe.
# ➤ Ele possui atributos (dados) e métodos (comportamentos).
# ➤ No exemplo acima, 'pessoa1' é um objeto da classe Pessoa.
