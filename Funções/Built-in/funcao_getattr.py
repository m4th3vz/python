# Função getattr() em Python

"""
getattr() serve para acessar o valor de um atributo de um objeto, mesmo que você não saiba o nome do atributo de antemão (ele pode estar em uma variável, por exemplo).

Sintaxe:
    getattr(objeto, "nome_do_atributo", valor_padrao_opcional)

- objeto: o objeto do qual você quer obter o atributo.
- nome_do_atributo: uma string com o nome do atributo.
- valor_padrao_opcional: valor a ser retornado caso o atributo não exista.
"""

# Exemplo 1: Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Matheus", 33)

# Acessando atributos normalmente
print("Nome:", p.nome)

# Acessando com getattr()
print("Nome (getattr):", getattr(p, "nome"))         # Saída: Matheus
print("Idade (getattr):", getattr(p, "idade"))       # Saída: 33

# Exemplo 2: Usando variável com o nome do atributo
atributo = "idade"
print("Acessando dinamicamente:", getattr(p, atributo))  # Saída: 33

# Exemplo 3: Usando valor padrão caso atributo não exista
print("Email:", getattr(p, "email", "não informado"))    # Saída: não informado

# Exemplo 4: Sem valor padrão, dá erro se o atributo não existe
try:
    print(getattr(p, "telefone"))
except AttributeError as e:
    print("Erro:", e)
# Saída: Erro: 'Pessoa' object has no attribute 'telefone'
