import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_binario = os.path.join(diretorio_atual, "exemplo.bin")

# Dados binários para salvar (bytes)
dados_binarios = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

# Salvar os dados binários em um arquivo
with open(arquivo_binario, "wb") as arquivo:
    arquivo.write(dados_binarios)

print(f"Arquivo binário '{arquivo_binario}' criado com sucesso!")

# Ler os dados binários do arquivo
with open(arquivo_binario, "rb") as arquivo:
    dados_lidos = arquivo.read()

print("Dados binários lidos do arquivo:")
print(dados_lidos)
