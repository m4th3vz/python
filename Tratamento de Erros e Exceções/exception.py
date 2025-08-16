# Demonstração de Exception

try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
        resultado = 10 / 0
except Exception as e:
    print(f"Ocorreu um erro: {e}")
