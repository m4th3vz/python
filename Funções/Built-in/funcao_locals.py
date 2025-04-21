# Função locals() em Python

"""
locals() retorna um dicionário representando o espaço de nomes local.
Ele contém todas as variáveis e seus valores no escopo atual.
"""

# Exemplo 1: Usando locals() no escopo global
a = 10
b = 20

# Chamando locals() fora de qualquer função, para ver as variáveis globais
print(locals())  # {'a': 10, 'b': 20, '__name__': '__main__', '__doc__': None, ...}

# Exemplo 2: Usando locals() dentro de uma função
def minha_funcao():
    x = 5
    y = 15
    print(locals())  # {'x': 5, 'y': 15}

minha_funcao()

# Exemplo 3: Modificando variáveis usando locals()
def exemplo_modificacao():
    z = 30
    print(f"Antes de modificar: {locals()}")
    locals()['z'] = 50  # Modificando a variável 'z' dinamicamente no escopo local
    print(f"Depois de modificar: {locals()}")

exemplo_modificacao()

# Exemplo 4: Usando locals() com classes
class MinhaClasse:
    def __init__(self):
        self.var1 = 100
        self.var2 = 200
    
    def mostrar_locais(self):
        print(locals())  # Retorna as variáveis locais da instância da classe

objeto = MinhaClasse()
objeto.mostrar_locais()

