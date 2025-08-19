# __init__
# Chamado ao criar uma instância. Inicializa atributos do objeto.

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

p=Pessoa("Matheus",33)
print(p.nome,p.idade)
