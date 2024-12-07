class Nome_e_Idade:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos de idade")

# Pedir o nome e a idade fora da classe
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))

# Criar uma instância da classe com os dados fornecidos
mostrar = Nome_e_Idade(nome1, idade1)
mostrar.exibir()
