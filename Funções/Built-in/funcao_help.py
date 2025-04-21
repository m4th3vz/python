# Função help() em Python

"""
help() exibe a documentação de um objeto, função, classe, módulo, ou até mesmo a documentação do próprio Python.
Isso ajuda a entender como utilizar um recurso sem precisar buscar na internet ou em livros.
"""

# Exemplo 1: Usando help() para obter ajuda sobre a função `print`
help(print)

# Exemplo 2: Usando help() para obter ajuda sobre um módulo específico (exemplo com o módulo `math`)
import math
help(math)

# Exemplo 3: Usando help() em uma classe definida pelo usuário
class Pessoa:
    """
    Classe que representa uma pessoa.
    """

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Obtendo ajuda sobre a classe `Pessoa`
help(Pessoa)

# Exemplo 4: Ajuda sobre um método específico de uma classe
help(Pessoa.apresentar)

# Exemplo 5: Obtendo ajuda interativa (usa a função `help()` diretamente no terminal ou no ambiente interativo)
help()  # Isso abrirá o modo de ajuda interativa, onde você pode pesquisar sobre módulos, funções, etc.
