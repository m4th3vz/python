# __slots__
# Define atributos fixos para economizar memória

class Pessoa:
    __slots__=['nome','idade']
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

p=Pessoa("Matheus",33)
print(p.nome,p.idade)
