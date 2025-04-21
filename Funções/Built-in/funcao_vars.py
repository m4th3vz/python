# Função vars() em Python

"""
A função built-in vars() é usada para retornar o __dict__ de um objeto. 
O __dict__ é um dicionário que contém os atributos e valores de um objeto.
Se usado sem argumentos, vars() retorna o __dict__ do objeto global (como se fosse o globals()).
Se usado com um objeto como argumento, retorna o dicionário de atributos e valores desse objeto.
A sintaxe é: vars([objeto])
- objeto: O objeto cujos atributos serão retornados como um dicionário. Se nenhum objeto for passado, a função retornará o dicionário global.
"""

# Exemplo 1: Usando vars() com uma classe e seus atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Ana", 25)

# Obtendo o dicionário de atributos da instância de Pessoa
atributos_pessoa = vars(pessoa)
print("Atributos da pessoa:", atributos_pessoa)  
# Saída: Atributos da pessoa: {'nome': 'Ana', 'idade': 25}

# Exemplo 2: Usando vars() sem argumentos para obter o dicionário global
variavel_global = 10
dicionario_global = vars()
print("Dicionário global:", dicionario_global)  
# Saída: Dicionário global: {'variavel_global': 10}

# Exemplo 3: Usando vars() com uma função para obter os atributos de uma função
def minha_funcao():
    pass

atributos_funcao = vars(minha_funcao)
print("Atributos da função:", atributos_funcao)  
# Saída: Atributos da função: {}

# Exemplo 4: Modificando atributos de um objeto usando o __dict__ acessado via vars()
pessoa.idade = 30
atributos_pessoa_atualizado = vars(pessoa)
print("Atributos da pessoa após atualização:", atributos_pessoa_atualizado)  
# Saída: Atributos da pessoa após atualização: {'nome': 'Ana', 'idade': 30}

# Exemplo 5: Usando vars() para explorar um dicionário de uma instância de uma classe
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.fabricante = "Toyota"

carro = Carro("Corolla", "Prata")
atributos_carro = vars(carro)
print("Atributos do carro:", atributos_carro)  
# Saída: Atributos do carro: {'modelo': 'Corolla', 'cor': 'Prata', 'fabricante': 'Toyota'}

"""
Resumo:
- A função vars() retorna o __dict__ de um objeto, que é um dicionário com seus atributos e valores.
- Quando chamada sem argumentos, ela retorna o dicionário global.
- É útil para inspecionar ou modificar atributos de objetos.
"""

# Exemplo prático: Usando vars() para acessar e modificar os atributos de um objeto
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

livro = Livro("1984", "George Orwell", 1949)

# Exibindo atributos do livro
print("Atributos do livro:", vars(livro))  
# Saída: Atributos do livro: {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949}

# Modificando o ano do livro
vars(livro)['ano'] = 2020
print("Atributos do livro após modificação:", vars(livro))  
# Saída: Atributos do livro após modificação: {'titulo': '1984', 'autor': 'George Orwell', 'ano': 2020}
