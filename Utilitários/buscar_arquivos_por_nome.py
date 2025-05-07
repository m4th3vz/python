import os

def buscar_arquivos(diretorio, nome_ou_extensao):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if nome_ou_extensao.lower() in file.lower():  # Ignora maiúsculas/minúsculas
                print(f"Encontrado: {os.path.join(root, file)}")

diretorio = input("Digite o caminho do diretório: ")
nome_ou_extensao = input("Digite o nome ou extensão do arquivo (ex: .txt ou parte do nome): ")
buscar_arquivos(diretorio, nome_ou_extensao)
