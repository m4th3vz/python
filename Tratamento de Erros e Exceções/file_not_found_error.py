# Demonstração de FileNotFoundError

try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
