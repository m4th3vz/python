# Demonstração de KeyError

dicionario = {"nome": "Matheus"}
try:
    print(dicionario["idade"])  # Chave inexistente
except KeyError:
    print("Erro: chave não encontrada no dicionário.")
