# Classe base (pai)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Classe derivada (filha) que herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Chama o construtor da classe base
        self.curso = curso

    def apresentar_curso(self):
        print(f"Estou estudando {self.curso}.")

# Criando um objeto da classe Estudante
estudante1 = Estudante("Matheus", 33, "Tecnologia da Informação")

estudante1.apresentar()        # Método herdado da classe Pessoa
estudante1.apresentar_curso()  # Método da classe Estudante

# ➤ Herança permite criar uma nova classe baseada em uma existente.
# ➤ A classe derivada herda atributos e métodos da classe base.
# ➤ Podemos adicionar novos métodos ou sobrescrever os existentes.
