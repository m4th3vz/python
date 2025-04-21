# Função bytes() em Python

"""
A função built-in bytes() cria uma sequência imutável de bytes.
Pode ser útil quando você precisa trabalhar com dados binários que não devem ser alterados.
"""

# Exemplo criando um bytes vazio
vazio = bytes()
print("bytes vazio:", vazio)  # Saída: b''

# Exemplo criando bytes a partir de uma lista de inteiros
dados = bytes([65, 66, 67])  # Representa 'A', 'B', 'C'
print("bytes a partir de lista:", dados)  # Saída: b'ABC'

# Exemplo criando bytes a partir de uma string
texto = "Python"
dados_texto = bytes(texto, 'utf-8')  # Converte a string para bytes (com codificação 'utf-8')
print("bytes de texto:", dados_texto)  # Saída: b'Python'

# Exemplo com slice: acessando um segmento de bytes
segmento = dados[1:3]  # Pega os elementos de índice 1 a 2 (B, C)
print("segmento de bytes:", segmento)  # Saída: b'BC'

# Exemplo convertendo bytes de volta para uma string
texto_decodificado = dados_texto.decode('utf-8')
print("Texto decodificado:", texto_decodificado)  # Saída: 'Python'

# Exemplo de uso de bytes com arquivos binários
with open('arquivo.bin', 'wb') as f:
    f.write(dados)  # Escreve os bytes no arquivo

# Lendo bytes de um arquivo binário
with open('arquivo.bin', 'rb') as f:
    conteudo = f.read()
    print("Conteúdo lido de arquivo:", conteudo)  # Saída: b'ABC'
