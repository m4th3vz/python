# __call__
# Permite chamar a instância como função

class Saudacao:
    def __call__(self):
        print("Olá!")

s=Saudacao()
s()
