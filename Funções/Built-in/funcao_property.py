# Função property() em Python

"""
A função built-in property() permite transformar métodos em atributos acessíveis,
de forma controlada e elegante, usando getters, setters e deleters.

Ela é usada principalmente em programação orientada a objetos.
"""

# Exemplo 1: Classe sem property (forma tradicional)
class PessoaSemProperty:
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_nome(self, valor):
        print("Nome alterado para:", valor)
        self._nome = valor

p1 = PessoaSemProperty("Matheus")
print(p1.get_nome())         # Acesso via método
p1.set_nome("João")

# Exemplo 2: Usando property para um código mais limpo
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_nome(self, valor):
        print("Alterando nome para:", valor)
        self._nome = valor

    def del_nome(self):
        print("Deletando nome...")
        del self._nome

    # Criando a propriedade
    nome = property(get_nome, set_nome, del_nome, "A propriedade 'nome'")

p2 = Pessoa("Matheus")
print(p2.nome)               # Internamente chama get_nome()
p2.nome = "João"             # Internamente chama set_nome()
del p2.nome                  # Internamente chama del_nome()

# Exemplo 3: Usando decoradores (@property)
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo.")
        self._preco = valor

    @preco.deleter
    def preco(self):
        print("Preço deletado!")
        del self._preco

p = Produto(100)
print("Preço atual:", p.preco)  # Chama o getter
p.preco = 200                   # Chama o setter
# p.preco = -10  # Levanta ValueError se descomentar
del p.preco                     # Chama o deleter

"""
Resumo:
- property() cria atributos controlados por métodos (get, set, del).
- Usar @property, @nome.setter e @nome.deleter é a forma mais moderna e legível.
- Útil para validar dados, calcular valores dinamicamente, e encapsular lógica.
"""

# Dica: Você pode acessar o docstring da property assim:
print(Pessoa.nome.__doc__)
