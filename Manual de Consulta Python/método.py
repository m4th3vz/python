# Definindo uma classe com métodos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método: função dentro da classe que atua sobre o objeto
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
p = Pessoa("Matheus", 33)

# Chamando o método do objeto
p.apresentar()

# ➤ Método é uma função definida dentro de uma classe.
# ➤ Ele opera sobre os dados (atributos) do objeto (instância).
# ➤ Chamamos métodos usando a notação objeto.método().
