# Função repr() em Python

"""
A função built-in repr() retorna uma string que representa um objeto de forma "oficial", ou seja, 
como ele seria exibido em uma sessão interativa do Python ou como um código Python válido (quando possível).
O objetivo é gerar uma representação precisa do objeto, geralmente para fins de depuração.
"""

# Exemplo 1: Usando repr() com strings
texto = "Olá, Mundo!"
print("repr('Olá, Mundo!') =", repr(texto))  # Saída: 'Olá, Mundo!'

# Exemplo 2: Usando repr() com números
numero = 123
print("repr(123) =", repr(numero))  # Saída: 123

# Exemplo 3: Usando repr() com listas
lista = [1, 2, 3, "teste"]
print("repr([1, 2, 3, 'teste']) =", repr(lista))  # Saída: [1, 2, 3, 'teste']

# Exemplo 4: Usando repr() com objetos personalizados
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __repr__(self):
        return f"Carro(modelo={self.modelo}, cor={self.cor})"

carro = Carro("Fusca", "azul")
print("repr(carro) =", repr(carro))  # Saída: Carro(modelo=Fusca, cor=azul)

# Exemplo 5: Comparando com str()
# A diferença entre repr() e str() é que o str() foca em apresentar uma string amigável,
# enquanto o repr() tenta gerar uma representação mais detalhada e precisa do objeto.

print("str(carro) =", str(carro))  # Saída: <__main__.Carro object at 0x7f9b6b7b1f70>
print("repr(carro) =", repr(carro))  # Saída: Carro(modelo=Fusca, cor=azul)

"""
Resumo:
- A função repr() tenta gerar uma string representando um objeto de forma precisa.
- Ela é especialmente útil para depuração, pois fornece uma visão clara de como o objeto foi criado.
- Quando você define __repr__ em uma classe, você pode personalizar como o objeto será exibido.
- A diferença entre repr() e str() é que o str() é mais voltado para uma "apresentação amigável", enquanto o repr() foca em uma representação exata.
"""

# Exemplo prático: Verificando a saída de objetos no console
# Usando repr em uma lista para depuração
lista_de_numeros = [1, 2, 3, 4, 5]
print("Lista de números:", repr(lista_de_numeros))
