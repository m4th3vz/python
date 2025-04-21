# Função setattr() em Python

"""
A função built-in setattr() é usada para definir o valor de um atributo de um objeto.
Ela recebe três argumentos:
1. O objeto onde o atributo será definido.
2. O nome do atributo (como uma string).
3. O valor a ser atribuído a esse atributo.
"""

# Exemplo 1: Usando setattr() para adicionar um atributo a um objeto
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa("João")

# Adicionando um novo atributo "idade" usando setattr()
setattr(pessoa, "idade", 25)
print("Atributo 'idade' da pessoa:", pessoa.idade)  # Saída: 25

# Exemplo 2: Usando setattr() para alterar o valor de um atributo existente
setattr(pessoa, "idade", 30)
print("Novo valor do atributo 'idade' da pessoa:", pessoa.idade)  # Saída: 30

# Exemplo 3: Usando setattr() para definir um atributo com um valor calculado
altura = 1.75
setattr(pessoa, "altura", altura)
print("Atributo 'altura' da pessoa:", pessoa.altura)  # Saída: 1.75

# Exemplo 4: Usando setattr() para tentar adicionar um atributo em um objeto imutável
# Objetos como tuplas são imutáveis e não permitem a adição de novos atributos.
try:
    tupla = (1, 2, 3)
    setattr(tupla, "novo_atributo", "valor")  # Isso vai causar um erro
except AttributeError as e:
    print(f"Erro: {e}")  # Saída: Erro: 'tuple' object has no attribute 'novo_atributo'

# Exemplo 5: Verificando se o atributo já existe antes de usar setattr()
if not hasattr(pessoa, "email"):
    setattr(pessoa, "email", "joao@example.com")
print("Atributo 'email' da pessoa:", pessoa.email)  # Saída: joao@example.com

"""
Resumo:
- A função setattr() permite definir ou modificar atributos de objetos em Python de maneira dinâmica.
- Pode ser usada para adicionar novos atributos a um objeto ou modificar atributos existentes.
- Use getattr() para obter o valor de um atributo de um objeto e hasattr() para verificar se o atributo existe.
"""

# Exemplo prático: Usando setattr() para alterar atributos dinamicamente
def atualizar_atributo(obj, nome_atributo, valor):
    if hasattr(obj, nome_atributo):
        setattr(obj, nome_atributo, valor)
        print(f"Atributo '{nome_atributo}' atualizado para {valor}.")
    else:
        print(f"Atributo '{nome_atributo}' não encontrado!")

# Testando a função com o objeto pessoa
atualizar_atributo(pessoa, "idade", 35)  # Saída: Atributo 'idade' atualizado para 35.
atualizar_atributo(pessoa, "profissao", "Engenheiro")  # Saída: Atributo 'profissao' não encontrado!
