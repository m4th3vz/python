# Classe base
class Pessoa:
    def apresentar(self):
        print("Olá, sou uma pessoa.")

# Classes derivadas com comportamento diferente
class Estudante(Pessoa):
    def apresentar(self):
        print("Olá, sou um estudante de TI.")

class Professor(Pessoa):
    def apresentar(self):
        print("Olá, sou um professor de Python.")

# Função que recebe qualquer tipo de Pessoa
def apresentar_alguem(pessoa):
    pessoa.apresentar()

# Criando objetos de diferentes classes
p1 = Pessoa()
p2 = Estudante()
p3 = Professor()

# Chamando a função com diferentes tipos de objeto
apresentar_alguem(p1)
apresentar_alguem(p2)
apresentar_alguem(p3)

# ➤ Polimorfismo permite que diferentes classes tenham métodos com o mesmo nome, mas com comportamentos diferentes.
# ➤ Isso facilita o uso genérico de funções que lidam com objetos diferentes.
