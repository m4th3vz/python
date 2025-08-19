# Controle de atributos
# __getattr__, __setattr__, __delattr__, __dir__

class Pessoa:
    def __init__(self,nome):
        self.nome=nome
    def __getattr__(self,attr):
        return f"Atributo {attr} não existe"
    def __setattr__(self,attr,valor):
        super().__setattr__(attr,valor)
    def __delattr__(self,attr):
        super().__delattr__(attr)
    def __dir__(self):
        return ['nome','idade']

p=Pessoa("Matheus")
print(p.nome)
print(p.idade)
p.sobrenome="Silva"
print(p.sobrenome)
del p.nome
print(dir(p))
