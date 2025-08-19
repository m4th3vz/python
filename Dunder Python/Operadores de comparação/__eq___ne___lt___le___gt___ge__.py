# Comparações especiais
# __eq__ = ==, __ne__ = !=, __lt__ = <, __le__ = <=, __gt__ = >, __ge__ = >=

class Numero:
    def __init__(self,valor):
        self.valor=valor
    def __eq__(self,outro):
        return self.valor==outro.valor
    def __ne__(self,outro):
        return self.valor!=outro.valor
    def __lt__(self,outro):
        return self.valor<outro.valor
    def __le__(self,outro):
        return self.valor<=outro.valor
    def __gt__(self,outro):
        return self.valor>outro.valor
    def __ge__(self,outro):
        return self.valor>=outro.valor

a=Numero(5)
b=Numero(10)
print(a==b,a!=b,a<b,a<=b,a>b,a>=b)
