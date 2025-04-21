# Função memoryview() em Python

"""
memoryview() cria uma visualização de memória de um objeto, permitindo acessar e manipular dados de forma eficiente.
"""

# Exemplo 1: Usando memoryview com um objeto bytes
dados = bytes([1, 2, 3, 4, 5])

# Criando uma visualização de memória dos dados
view = memoryview(dados)

# Acessando um item da visualização de memória (não cria uma cópia)
print(view[0])  # 1

# Acessando uma fatia (slice) de dados
sliced_view = view[1:4]
print(sliced_view.tolist())  # [2, 3, 4]

# Exemplo 2: Usando memoryview com bytearray
dados_bytearray = bytearray([10, 20, 30, 40, 50])

# Criando a visualização de memória
view_bytearray = memoryview(dados_bytearray)

# Alterando os dados da visualização de memória
view_bytearray[0] = 99
print(dados_bytearray)  # bytearray(b'99 20 30 40 50')

# Exemplo 3: Trabalhando com a função tolist()
print(view_bytearray.tolist())  # [99, 20, 30, 40, 50]

# Exemplo 4: Usando memoryview com grandes dados binários (mais eficiente)
grande_lista = bytearray(range(1000000))  # Lista com 1 milhão de números
view_grande = memoryview(grande_lista)

# Acessando uma fatia sem copiar dados
slice_grande = view_grande[500:600]
print(slice_grande.tolist())  # [500, 501, ..., 599]
