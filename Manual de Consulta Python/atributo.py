# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        # Atributos da instância (pertencem ao objeto)
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Matheus", 33)

# Acessando os atributos
print(pessoa1.nome)   # Imprime: Matheus
print(pessoa1.idade)  # Imprime: 33

# ➤ Atributo é uma variável que pertence a um objeto.
# ➤ Neste exemplo, 'nome' e 'idade' são atributos da instância pessoa1.
# ➤ Usamos self.atributo para defini-los dentro da classe.
