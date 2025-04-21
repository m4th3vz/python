# Função hash() em Python

"""
hash() retorna o valor de hash de um objeto. 
Ele é usado principalmente para comparar objetos e para armazenar objetos em dicionários ou sets.
"""

# Exemplo 1: Usando hash() em uma string
texto = "Python"
hash_texto = hash(texto)
print("Hash do texto:", hash_texto)
# Exemplo de saída: Hash do texto: 1234567890 (valor numérico depende do sistema)

# Exemplo 2: Usando hash() em uma tupla (imutável)
tupla = (1, 2, 3)
hash_tupla = hash(tupla)
print("Hash da tupla:", hash_tupla)
# Exemplo de saída: Hash da tupla: 5293440672954974510

# Exemplo 3: Usando hash() em um número (imutável)
numero = 42
hash_numero = hash(numero)
print("Hash do número:", hash_numero)
# Exemplo de saída: Hash do número: 42 (o valor é o próprio número, pois é imutável)

# Exemplo 4: Tentando usar hash() em uma lista (mutável)
try:
    lista = [1, 2, 3]
    hash_lista = hash(lista)
except TypeError as e:
    print("Erro:", e)
# Saída: Erro: unhashable type: 'list'

# Exemplo 5: Usando hash() com objetos personalizados
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __hash__(self):
        # Retorna um valor de hash com base no nome e na idade
        return hash((self.nome, self.idade))

pessoa = Pessoa("Matheus", 33)
hash_pessoa = hash(pessoa)
print("Hash da pessoa:", hash_pessoa)
# Exemplo de saída: Hash da pessoa: 4569871234
