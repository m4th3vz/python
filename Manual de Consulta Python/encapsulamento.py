# Encapsulamento: ocultar detalhes internos de um objeto

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome          # atributo público
        self.__idade = idade      # atributo privado (convencional)

    # Método público para acessar o atributo privado
    def get_idade(self):
        return self.__idade

    # Método público para modificar o atributo privado
    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else:
            print("Idade inválida!")

p = Pessoa("Matheus", 33)

print(p.nome)         # Acesso direto ao atributo público
print(p.get_idade())  # Acesso ao atributo privado via método

p.set_idade(34)       # Alterando idade pelo método
print(p.get_idade())

p.set_idade(-5)       # Tentativa de alteração inválida

# ➤ Encapsulamento é esconder detalhes internos e proteger os dados.
# ➤ Em Python, usamos '__' no início do nome para indicar atributos privados.
# ➤ O acesso é controlado por métodos públicos (getters e setters).
