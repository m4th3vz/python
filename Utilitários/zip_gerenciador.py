import os
import zipfile

def compactar_pasta(pasta_origem, arquivo_zip):
    # Pega o diretório pai da pasta a ser compactada (onde o ZIP vai ficar)
    pasta_destino_zip = os.path.abspath(os.path.join(pasta_origem, os.pardir))
    caminho_zip = os.path.join(pasta_destino_zip, arquivo_zip)

    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                caminho_relativo = os.path.relpath(caminho_arquivo, pasta_origem)
                zipf.write(caminho_arquivo, caminho_relativo)
    print(f"\nPasta '{pasta_origem}' compactada em '{caminho_zip}' com sucesso!")

def descompactar_zip(arquivo_zip, pasta_destino):
    with zipfile.ZipFile(arquivo_zip, 'r') as zipf:
        zipf.extractall(pasta_destino)
    print(f"\nArquivo '{arquivo_zip}' descompactado em '{pasta_destino}' com sucesso!")

def main():
    print("O que deseja fazer?")
    print("1 - Compactar pasta")
    print("2 - Descompactar arquivo ZIP")
    escolha = input("Digite 1 ou 2: ").strip()

    if escolha == '1':
        pasta = input("Digite o caminho da pasta para compactar: ").strip()
        arquivo_zip = input("Digite o nome do arquivo zip a criar (ex: backup.zip): ").strip()
        compactar_pasta(pasta, arquivo_zip)

    elif escolha == '2':
        arquivo_zip = input("Digite o caminho do arquivo zip para descompactar: ").strip()
        pasta_destino = input("Digite o caminho da pasta onde extrair os arquivos: ").strip()
        descompactar_zip(arquivo_zip, pasta_destino)

    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
