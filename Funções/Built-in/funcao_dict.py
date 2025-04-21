# Função dict() em Python

"""
A função dict() é usada para criar dicionários em Python. Um dicionário é uma coleção
de pares chave-valor, onde cada chave é única e associada a um valor.

A sintaxe básica é:
    dict(chave1=valor1, chave2=valor2, ...)
    ou
    dict({chave1: valor1, chave2: valor2, ...})
"""

# Exemplo 1: Criando um dicionário usando a função dict() com argumentos nomeados
dicionario1 = dict(nome="Matheus", idade=33, cidade="Barueri")
print("Dicionário 1:", dicionario1)
# Saída: Dicionário 1: {'nome': 'Matheus', 'idade': 33, 'cidade': 'Barueri'}

# Exemplo 2: Criando um dicionário a partir de uma lista de tuplas
lista_tuplas = [("nome", "Matheus"), ("idade", 33), ("cidade", "Barueri")]
dicionario2 = dict(lista_tuplas)
print("Dicionário 2:", dicionario2)
# Saída: Dicionário 2: {'nome': 'Matheus', 'idade': 33, 'cidade': 'Barueri'}

# Exemplo 3: Criando um dicionário vazio
dicionario_vazio = dict()
print("Dicionário Vazio:", dicionario_vazio)
# Saída: Dicionário Vazio: {}

# Exemplo 4: Criando um dicionário a partir de um objeto iterable de pares chave-valor
pares = [("a", 1), ("b", 2), ("c", 3)]
dicionario3 = dict(pares)
print("Dicionário 3:", dicionario3)
# Saída: Dicionário 3: {'a': 1, 'b': 2, 'c': 3}

# Acessando e manipulando valores em um dicionário
print("Valor da chave 'nome':", dicionario1["nome"])  # Saída: Matheus

# Modificando um valor
dicionario1["idade"] = 34
print("Dicionário após alteração:", dicionario1)
# Saída: Dicionário após alteração: {'nome': 'Matheus', 'idade': 34, 'cidade': 'Barueri'}

# Verificando se uma chave existe no dicionário
print("Chave 'cidade' existe?", "cidade" in dicionario1)  # Saída: True

# Removendo um item
del dicionario1["cidade"]
print("Dicionário após remoção de 'cidade':", dicionario1)
# Saída: Dicionário após remoção de 'cidade': {'nome': 'Matheus', 'idade': 34}

"""
Resumo:
- dict() cria um dicionário em Python, que é uma coleção de pares chave-valor.
- É possível criar dicionários de diferentes maneiras, usando argumentos nomeados ou listas/tuplas.
- Dicionários podem ser manipulados (adicionar, remover e modificar elementos).
"""

# Exemplo prático: armazenando informações sobre estudantes
estudantes = dict()
estudantes["Lucas"] = {"idade": 20, "curso": "TI"}
estudantes["Ana"] = {"idade": 22, "curso": "Engenharia"}

print("Estudantes:", estudantes)
# Saída: Estudantes: {'Lucas': {'idade': 20, 'curso': 'TI'}, 'Ana': {'idade': 22, 'curso': 'Engenharia'}}
