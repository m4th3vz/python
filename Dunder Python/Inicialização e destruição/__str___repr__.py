# __str__ e __repr__
# __str__ define a representação legível (para usuário).
# __repr__ define a representação oficial (para desenvolvedor).

class Pessoa:
    def __init__(self,nome):
        self.nome=nome
    def __str__(self):
        return f"Pessoa: {self.nome}"
    def __repr__(self):
        return f"Pessoa(nome='{self.nome}')"

p=Pessoa("Matheus")
print(str(p))
print(repr(p))
