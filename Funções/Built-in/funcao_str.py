# Função str() em Python

"""
A função built-in str() é usada para converter objetos em suas representações em formato de string. 
Ela pode ser aplicada a números, listas, tuplas, dicionários e outros tipos de dados, transformando-os em uma sequência de caracteres.
A sintaxe é: str(objeto)
"""

# Exemplo 1: Convertendo um número inteiro para string
numero = 123
numero_str = str(numero)
print("Número como string:", numero_str)  # Saída: '123'

# Exemplo 2: Convertendo um número de ponto flutuante para string
numero_float = 3.14
numero_float_str = str(numero_float)
print("Número float como string:", numero_float_str)  # Saída: '3.14'

# Exemplo 3: Convertendo uma lista para string
lista = [1, 2, 3, 4]
lista_str = str(lista)
print("Lista como string:", lista_str)  # Saída: '[1, 2, 3, 4]'

# Exemplo 4: Convertendo um dicionário para string
dicionario = {"nome": "João", "idade": 25}
dicionario_str = str(dicionario)
print("Dicionário como string:", dicionario_str)  # Saída: "{'nome': 'João', 'idade': 25}"

# Exemplo 5: Convertendo um objeto personalizado para string
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Pessoa(nome="{self.nome}", idade={self.idade})'

pessoa = Pessoa("Maria", 30)
pessoa_str = str(pessoa)
print("Objeto Pessoa como string:", pessoa_str)  # Saída: 'Pessoa(nome="Maria", idade=30)'

# Exemplo 6: Convertendo uma tupla para string
tupla = (10, 20, 30)
tupla_str = str(tupla)
print("Tupla como string:", tupla_str)  # Saída: '(10, 20, 30)'

# Exemplo 7: Usando str() para criar uma string de texto
texto = str("Python é incrível!")
print("Texto como string:", texto)  # Saída: 'Python é incrível!'

"""
Resumo:
- A função str() converte qualquer objeto em uma string.
- Pode ser usada para converter números, listas, tuplas, dicionários, entre outros, para suas representações textuais.
- A conversão de objetos personalizados pode ser feita definindo o método __str__() na classe.
"""

# Exemplo prático: Usando str() em um cálculo e formatando a string
numero_1 = 7
numero_2 = 3
resultado = numero_1 + numero_2
resultado_str = str(resultado)

print("Resultado da soma como string:", "O resultado de " + str(numero_1) + " + " + str(numero_2) + " é " + resultado_str)  
# Saída: O resultado de 7 + 3 é 10
