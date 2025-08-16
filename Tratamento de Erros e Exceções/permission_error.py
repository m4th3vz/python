# Demonstração de PermissionError

try:
    with open("/root/arquivo.txt", "r") as f:
        f.read()
except PermissionError:
    print("Erro: permissão negada para acessar o arquivo.")
