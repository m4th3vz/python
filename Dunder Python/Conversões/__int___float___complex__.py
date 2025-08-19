# Conversões numéricas
# __int__, __float__, __complex__

class Numero:
    def __init__(self,valor):
        self.valor=valor
    def __int__(self):
        return int(self.valor)
    def __float__(self):
        return float(self.valor)
    def __complex__(self):
        return complex(self.valor)

n=Numero(5)
print(int(n),float(n),complex(n))
