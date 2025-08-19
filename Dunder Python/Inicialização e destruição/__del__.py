# __del__
# Chamado quando o objeto é destruído (garbage collection).

class Pessoa:
    def __del__(self):
        print("Objeto destruído")

p=Pessoa()
del p
