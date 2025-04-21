# Função frozenset() em Python

"""
frozenset() cria um conjunto imutável — ou seja, depois de criado, você não pode adicionar, remover ou alterar seus elementos.

Sintaxe:
    frozenset(iterável)

- iterável: uma lista, tupla, string, ou qualquer objeto iterável.
"""

# Exemplo 1: Criando um frozenset a partir de uma lista
lista = [1, 2, 3, 2, 1]
conjunto_congelado = frozenset(lista)

print("Frozenset:", conjunto_congelado)
# Saída: Frozenset: frozenset({1, 2, 3})

# Exemplo 2: Tentando modificar um frozenset (vai dar erro)
try:
    conjunto_congelado.add(4)
except AttributeError as e:
    print("Erro:", e)
# Saída: Erro: 'frozenset' object has no attribute 'add'

# Exemplo 3: frozenset com strings (caracteres únicos, como set)
texto = "banana"
fset_texto = frozenset(texto)
print("Frozenset do texto:", fset_texto)
# Saída: Frozenset do texto: frozenset({'b', 'a', 'n'})

# Exemplo 4: Usando frozenset como chave de dicionário (o set comum não pode!)
dicionario = {
    frozenset([1, 2]): "par",
    frozenset([3, 4]): "outro par"
}
print("Valor da chave [1, 2]:", dicionario[frozenset([1, 2])])
# Saída: Valor da chave [1, 2]: par

# Exemplo 5: Operações de conjunto ainda funcionam!
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print("Interseção:", a & b)  # frozenset({3})
print("União:", a | b)       # frozenset({1, 2, 3, 4, 5})
