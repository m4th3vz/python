# Operadores aritméticos
# __add__ = +, __sub__ = -, __mul__ = *, __truediv__ = /, __floordiv__ = //, __mod__ = %, __pow__ = **

class Numero:
    def __init__(self,valor):
        self.valor=valor
    def __add__(self,outro):
        return Numero(self.valor+outro.valor)
    def __sub__(self,outro):
        return Numero(self.valor-outro.valor)
    def __mul__(self,outro):
        return Numero(self.valor*outro.valor)
    def __truediv__(self,outro):
        return Numero(self.valor/outro.valor)
    def __floordiv__(self,outro):
        return Numero(self.valor//outro.valor)
    def __mod__(self,outro):
        return Numero(self.valor%outro.valor)
    def __pow__(self,outro):
        return Numero(self.valor**outro.valor)
    def __neg__(self):
        return Numero(-self.valor)
    def __pos__(self):
        return Numero(+self.valor)
    def __abs__(self):
        return Numero(abs(self.valor))
    def __repr__(self):
        return f"Numero({self.valor})"

a=Numero(10)
b=Numero(3)
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b,-a,+a,abs(a))
