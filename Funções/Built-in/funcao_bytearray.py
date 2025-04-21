# Função bytearray() em Python

"""
A função built-in bytearray() cria um objeto mutável do tipo bytearray.
Ela pode ser útil para manipular dados binários ou quando você precisa alterar um objeto de bytes.
"""

# Exemplo criando um bytearray vazio
vazio = bytearray()
print("bytearray vazio:", vazio)  # Saída: bytearray(b'')

# Exemplo criando um bytearray com valores numéricos (de 0 a 255)
dados = bytearray([65, 66, 67])  # Representa 'A', 'B', 'C'
print("bytearray com valores:", dados)  # Saída: bytearray(b'ABC')

# Exemplo criando um bytearray a partir de uma string
texto = "Python"
dados_texto = bytearray(texto, 'utf-8')  # Converte a string para bytes (com codificação 'utf-8')
print("bytearray de texto:", dados_texto)  # Saída: bytearray(b'Python')

# Modificando um bytearray
dados[0] = 90  # Alterando o primeiro valor (A -> Z)
print("bytearray modificado:", dados)  # Saída: bytearray(b'ZBC')

# Exemplo convertendo de volta para uma string
novo_texto = dados_texto.decode('utf-8')  # Decodificando de volta para string
print("Texto decodificado:", novo_texto)  # Saída: 'Python'

# Exemplo com um bytearray e um loop
for byte in dados_texto:
    print(byte, end=" ")  # Saída: 80 121 116 104 111 110
