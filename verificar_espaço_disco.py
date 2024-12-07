import shutil

def verificar_espaco(diretorio):
    total, usado, livre = shutil.disk_usage(diretorio)
    print(f"Espaço total: {total // (2**30)} GB")
    print(f"Espaço usado: {usado // (2**30)} GB")
    print(f"Espaço livre: {livre // (2**30)} GB")

diretorio = input("Digite o diretório (ex: C:\\): ")
verificar_espaco(diretorio)
