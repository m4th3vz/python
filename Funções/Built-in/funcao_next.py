# Função next() em Python

"""
A função built-in next() retorna o próximo item de um iterador.

Ela é usada com objetos iteráveis como listas, tuplas, strings, dicionários,
ou qualquer objeto que implemente o protocolo de iterador.

Sintaxe:
    next(iterador, valor_padrao)

- O primeiro argumento é o iterador.
- O segundo argumento (opcional) é um valor padrão que será retornado se o iterador acabar.
  Se não for fornecido e o iterador terminar, um erro StopIteration será lançado.
"""

# Exemplo 1: Usando next() com um iterador criado a partir de uma lista
lista = [10, 20, 30]
iterador = iter(lista)  # transformando a lista em um iterador

print(next(iterador))  # Saída: 10
print(next(iterador))  # Saída: 20
print(next(iterador))  # Saída: 30
# print(next(iterador))  # Isso causaria um erro StopIteration

# Exemplo 2: Usando o segundo argumento para evitar erro
print(next(iterador, "Fim da lista"))  # Saída: "Fim da lista"

# Exemplo 3: Iterando manualmente por um iterador
texto = "abc"
it = iter(texto)

while True:
    letra = next(it, None)
    if letra is None:
        break
    print(letra)

"""
Resumo:
- Use next() para pegar o próximo valor de um iterador.
- É útil quando você quer mais controle do que um loop for daria.
- Com o valor padrão, você evita exceções e deixa o código mais seguro.
"""
