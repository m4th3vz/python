# Iteração
# __iter__ retorna iterador, __next__ retorna próximo elemento.

class Contador:
    def __init__(self,limite):
        self.limite=limite
        self.atual=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.atual<self.limite:
            self.atual+=1
            return self.atual
        else:
            raise StopIteration

for n in Contador(3):
    print(n)
