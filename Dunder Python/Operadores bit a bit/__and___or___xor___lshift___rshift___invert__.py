# Operadores bit a bit
# __and__ = &, __or__ = |, __xor__ = ^, __lshift__ = <<, __rshift__ = >>, __invert__ = ~

class Bits:
    def __init__(self,valor):
        self.valor=valor
    def __and__(self,outro):
        return Bits(self.valor & outro.valor)
    def __or__(self,outro):
        return Bits(self.valor | outro.valor)
    def __xor__(self,outro):
        return Bits(self.valor ^ outro.valor)
    def __lshift__(self,outro):
        return Bits(self.valor << outro.valor)
    def __rshift__(self,outro):
        return Bits(self.valor >> outro.valor)
    def __invert__(self):
        return Bits(~self.valor)
    def __repr__(self):
        return f"Bits({self.valor})"

a=Bits(5)
b=Bits(3)
print(a&b,a|b,a^b,a<<b,a>>b,~a)
