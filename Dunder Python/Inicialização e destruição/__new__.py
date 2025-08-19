# __new__
# Cria a instância antes de __init__. Útil para classes imutáveis ou singletons.

class Pessoa:
    def __new__(cls,nome):
        print("Criando nova instância")
        return super().__new__(cls)
    def __init__(self,nome):
        self.nome=nome

p=Pessoa("Matheus")
print(p.nome)
