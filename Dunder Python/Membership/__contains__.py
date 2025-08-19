# __contains__
# Define comportamento do operador in

class MinhaLista:
    def __init__(self,itens):
        self.itens=itens
    def __contains__(self,item):
        return item in self.itens

ml=MinhaLista([1,2,3])
print(2 in ml, 5 in ml)
