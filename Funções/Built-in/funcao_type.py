# Função type() em Python

"""
A função built-in type() é usada para retornar o tipo de um objeto em Python.
Ela pode ser usada para verificar o tipo de qualquer variável ou valor.
A sintaxe é: type(objeto)
- objeto: Qualquer objeto do qual você deseja verificar o tipo.
"""

# Exemplo 1: Verificando o tipo de um número inteiro
numero = 42
tipo_numero = type(numero)
print("Tipo de número:", tipo_numero)  # Saída: <class 'int'>

# Exemplo 2: Verificando o tipo de um número de ponto flutuante
numero_float = 3.14
tipo_numero_float = type(numero_float)
print("Tipo de número float:", tipo_numero_float)  # Saída: <class 'float'>

# Exemplo 3: Verificando o tipo de uma string
texto = "Python"
tipo_texto = type(texto)
print("Tipo de texto:", tipo_texto)  # Saída: <class 'str'>

# Exemplo 4: Verificando o tipo de uma lista
lista = [1, 2, 3, 4]
tipo_lista = type(lista)
print("Tipo de lista:", tipo_lista)  # Saída: <class 'list'>

# Exemplo 5: Verificando o tipo de um dicionário
dicionario = {"nome": "Maria", "idade": 30}
tipo_dicionario = type(dicionario)
print("Tipo de dicionário:", tipo_dicionario)  # Saída: <class 'dict'>

# Exemplo 6: Verificando o tipo de um conjunto (set)
conjunto = {1, 2, 3}
tipo_conjunto = type(conjunto)
print("Tipo de conjunto:", tipo_conjunto)  # Saída: <class 'set'>

# Exemplo 7: Verificando o tipo de uma tupla
tupla = (1, 2, 3)
tipo_tupla = type(tupla)
print("Tipo de tupla:", tipo_tupla)  # Saída: <class 'tuple'>

# Exemplo 8: Verificando o tipo de uma função
def minha_funcao():
    return "Olá!"
tipo_funcao = type(minha_funcao)
print("Tipo de função:", tipo_funcao)  # Saída: <class 'function'>

# Exemplo 9: Verificando o tipo de uma classe personalizada
class Carro:
    pass

carro = Carro()
tipo_carro = type(carro)
print("Tipo de carro:", tipo_carro)  # Saída: <class '__main__.Carro'>

"""
Resumo:
- A função type() retorna o tipo do objeto passado como argumento.
- Ela pode ser usada para verificar o tipo de variáveis, objetos, funções, etc.
- Retorna um tipo de classe, como <class 'int'>, <class 'str'>, etc.
"""

# Exemplo prático: Usando type() para verificar tipos de dados em um programa
def identificar_tipo(valor):
    tipo = type(valor)
    print(f"O valor {valor} é do tipo {tipo}.")

identificar_tipo(10)           # Saída: O valor 10 é do tipo <class 'int'>.
identificar_tipo("Python")     # Saída: O valor Python é do tipo <class 'str'>.
identificar_tipo([1, 2, 3])    # Saída: O valor [1, 2, 3] é do tipo <class 'list'>.
identificar_tipo({'a': 1})     # Saída: O valor {'a': 1} é do tipo <class 'dict'>.
