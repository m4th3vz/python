class Pessoa:
    # Método construtor (__init__) para inicializar os atributos da classe
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo 'nome'
        self.idade = idade  # Atributo 'idade'

    # Método para exibir informações sobre a pessoa
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando uma instância (objeto) da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Chamando o método para exibir as informações
pessoa1.apresentar()
