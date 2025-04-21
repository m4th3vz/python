# Função callable() em Python

"""
A função built-in callable() verifica se o objeto passado pode ser chamado como uma função.
- Retorna True se o objeto for invocável (como uma função ou método).
- Retorna False caso contrário (por exemplo, se o objeto for uma variável ou classe sem um método __call__).
"""

# Exemplo 1: Verificando uma função
def minha_funcao():
    return "Olá, Mundo!"

print("minha_funcao é callable?", callable(minha_funcao))  # Saída: True

# Exemplo 2: Verificando um número (não invocável)
numero = 42
print("numero é callable?", callable(numero))  # Saída: False

# Exemplo 3: Verificando um objeto de classe sem __call__ (não invocável)
class MinhaClasse:
    pass

objeto = MinhaClasse()
print("objeto é callable?", callable(objeto))  # Saída: False

# Exemplo 4: Verificando uma instância de classe com __call__ (invocável)
class MinhaClasseCallable:
    def __call__(self):
        return "Instância invocada!"

objeto_callable = MinhaClasseCallable()
print("objeto_callable é callable?", callable(objeto_callable))  # Saída: True

# Exemplo 5: Verificando um método (que é invocável)
class OutraClasse:
    def meu_metodo(self):
        return "Método invocado!"

objeto_metodo = OutraClasse()
print("meu_metodo é callable?", callable(objeto_metodo.meu_metodo))  # Saída: True

# Exemplo 6: Verificando uma classe (não invocável diretamente, mas pode ser instanciada)
print("MinhaClasse é callable?", callable(MinhaClasse))  # Saída: True, pois a classe pode ser instanciada
