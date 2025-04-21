# Função object() em Python

"""
A função built-in object() retorna uma nova instância do objeto base do Python.

Ela é a superclasse de todas as classes em Python — ou seja, todas as classes herdam dela,
direta ou indiretamente.

Embora a instância retornada por object() não faça muita coisa por si só,
ela pode ser útil em situações específicas, como:

- Criar sentinelas (valores únicos que servem como marcadores)
- Usar como base para novas classes
"""

# Exemplo 1: Criando um objeto básico
obj = object()
print(obj)                # Exibe o endereço do objeto
print(type(obj))          # <class 'object'>
print(isinstance(obj, object))  # True

# Exemplo 2: Usando object() como valor sentinela
sentinela = object()

def buscar_valor(dicionario, chave):
    resultado = dicionario.get(chave, sentinela)
    if resultado is sentinela:
        return "Chave não encontrada"
    return resultado

dados = {"nome": "Matheus"}
print(buscar_valor(dados, "nome"))       # Saída: Matheus
print(buscar_valor(dados, "idade"))      # Saída: Chave não encontrada

# Por que não usar None como sentinela?
# Porque o dicionário poderia conter {"chave": None} como valor legítimo,
# então object() garante uma identidade única e confiável.

"""
Resumo:
- object() cria um objeto básico, sem métodos ou atributos personalizados.
- Ideal para usar como sentinela ou como base de herança.
"""

# Exemplo 3: Classe personalizada herdando diretamente de object
class MeuObjeto(object):
    def __init__(self, valor):
        self.valor = valor

instancia = MeuObjeto(42)
print(instancia.valor)  # Saída: 42
