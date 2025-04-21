# Função globals() em Python

"""
globals() retorna um dicionário com todas as variáveis e funções no escopo global.
Você pode acessar ou modificar variáveis globais usando esse dicionário.
"""

# Exemplo 1: Usando globals() para acessar variáveis globais
a = 10
b = 20

# Acessando variáveis globais com globals()
print("Valor de 'a' via globals():", globals()['a'])  # Saída: 10
print("Valor de 'b' via globals():", globals()['b'])  # Saída: 20

# Exemplo 2: Modificando uma variável global via globals()
globals()['a'] = 30
print("Novo valor de 'a' via globals():", a)  # Saída: 30

# Exemplo 3: Usando globals() para verificar todas as variáveis globais
print("\nTodas as variáveis globais:")
for chave, valor in globals().items():
    print(f"{chave}: {valor}")

# Exemplo 4: Usando globals() dentro de uma função
def minha_funcao():
    var_local = "Sou local"
    print("Dentro da função, variáveis globais:")
    for chave, valor in globals().items():
        print(f"{chave}: {valor}")

minha_funcao()
# Exemplo de saída:
# Dentro da função, variáveis globais:
# __name__: __main__
# __doc__: None
# __package__: None
# a: 30
# b: 20
# globals: <built-in function globals>
# ...
