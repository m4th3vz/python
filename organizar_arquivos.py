import os
import shutil  # Módulo para mover arquivos e manipular diretórios

def organizar_arquivos(diretorio):
    # Itera sobre os arquivos do diretório
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Verifica se é um arquivo (e não um diretório)
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1]  # Extrai a extensão do arquivo
            pasta_destino = os.path.join(diretorio, extensao.capitalize())  # Define o nome da pasta com a extensão

            # Cria a pasta de destino, se não existir
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Move o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

# Solicita ao usuário o caminho do diretório e organiza os arquivos
diretorio = input("Digite o caminho do diretório: ")
organizar_arquivos(diretorio)
