# Função anext() em Python

"""
anext() é usada para obter o **próximo valor** de um iterador assíncrono.
É a versão assíncrona da função next().

Sintaxe:
    await anext(async_iterator)
    await anext(async_iterator, default)  # evita exceção se acabar

Ela deve ser usada dentro de funções async e com await.
"""

import asyncio

# Criando um iterador assíncrono simples
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
        await asyncio.sleep(0.5)  # Simula uma espera assíncrona
        return atual

# Função principal
async def main():
    contador = ContadorAssincrono(1, 4)
    iterator = aiter(contador)

    print("Usando anext() manualmente:")

    # Pegando elementos um por um
    print(await anext(iterator))  # 1
    print(await anext(iterator))  # 2
    print(await anext(iterator))  # 3

    # Usando valor padrão para evitar exceção
    print(await anext(iterator, "Fim do iterador"))  # Fim do iterador

asyncio.run(main())
