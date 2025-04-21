# Função dir() em Python

"""
A função dir() é usada para obter uma lista dos atributos e métodos de um objeto.
Quando chamada sem argumentos, retorna a lista de nomes no escopo atual (variáveis e funções definidas).
Quando chamada com um objeto como argumento, retorna os atributos e métodos do objeto.
"""

# Exemplo 1: Usando dir() sem argumentos
print("dir() sem argumentos:", dir())
# Saída: Lista de variáveis e funções no escopo atual (isso pode variar dependendo do ambiente)

# Exemplo 2: Usando dir() com um objeto (como uma string)
texto = "Olá, Mundo!"
atributos_texto = dir(texto)
print("\nAtributos e métodos da string:", atributos_texto)
# Saída: Lista de métodos e atributos da classe string, como 'lower', 'upper', 'strip', etc.

# Exemplo 3: Usando dir() com uma classe personalizada
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Criando um objeto da classe Pessoa
pessoa = Pessoa("Matheus", 33)

# Obtendo os atributos e métodos da instância pessoa
atributos_pessoa = dir(pessoa)
print("\nAtributos e métodos da instância Pessoa:", atributos_pessoa)
# Saída: Lista com atributos e métodos de 'pessoa', como '__init__', 'nome', 'idade', 'saudacao', etc.

# Exemplo 4: Usando dir() com um módulo (como o módulo math)
import math
atributos_math = dir(math)
print("\nAtributos e métodos do módulo math:", atributos_math)
# Saída: Lista com funções e atributos do módulo math, como 'sqrt', 'pi', 'cos', etc.

"""
Resumo:
- dir() é útil para explorar objetos, módulos e o escopo atual, retornando uma lista dos atributos e métodos.
- Quando usada sem argumentos, retorna o escopo atual (variáveis e funções).
- Quando usada com um objeto, retorna os métodos e atributos desse objeto.
"""

# Exemplo prático: verificando os métodos disponíveis em uma lista
minha_lista = [1, 2, 3, 4]
atributos_lista = dir(minha_lista)
print("\nAtributos e métodos da lista:", atributos_lista)
# Saída: Lista de métodos de listas, como 'append', 'pop', 'remove', etc.
