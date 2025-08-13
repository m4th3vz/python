import os
import shutil

def organizar_arquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_arquivo):
            # Extrair a extensão de forma segura
            nome, extensao = os.path.splitext(arquivo)
            
            if extensao:  
                pasta_destino = os.path.join(diretorio, extensao[1:].lower())  # remove o ponto e padroniza
            else:
                pasta_destino = os.path.join(diretorio, "sem_extensao")

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

diretorio = input("Digite o caminho do diretório: ").strip()
organizar_arquivos(diretorio)
print("Organização concluída!")
