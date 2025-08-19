# Indexação e atribuição
# __getitem__, __setitem__, __delitem__

class MinhaLista:
    def __init__(self,itens):
        self.itens=itens
    def __getitem__(self,index):
        return self.itens[index]
    def __setitem__(self,index,valor):
        self.itens[index]=valor
    def __delitem__(self,index):
        del self.itens[index]

ml=MinhaLista([1,2,3])
print(ml[1])
ml[1]=20
print(ml.itens)
del ml[0]
print(ml.itens)
