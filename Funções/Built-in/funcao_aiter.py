# Função aiter() em Python

"""
aiter() é usada para obter um iterador assíncrono de um objeto assíncrono iterável.
Ou seja, ela serve para trabalhar com loops assíncronos, como em `async for`.

Disponível a partir do Python 3.10.

Sintaxe:
    aiter(async_iterable)
"""

import asyncio

# Criando um iterador assíncrono de exemplo
class ContadorAssincrono:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.atual >= self.fim:
            raise StopAsyncIteration
        atual = self.atual
        self.atual += 1
        await asyncio.sleep(0.5)  # Simula uma operação assíncrona
        return atual

# Função principal assíncrona
async def main():
    async_iterador = aiter(ContadorAssincrono(1, 5))

    print("Valores gerados pelo iterador assíncrono:")
    async for valor in async_iterador:
        print(valor)

# Executando o script assíncrono
asyncio.run(main())
