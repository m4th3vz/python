import os
import zipfile

def compactar_pasta(pasta_origem):
    # Nome do ZIP será o mesmo da pasta
    nome_pasta = os.path.basename(os.path.normpath(pasta_origem))
    pasta_destino_zip = os.path.abspath(os.path.join(pasta_origem, os.pardir))
    caminho_zip = os.path.join(pasta_destino_zip, f"{nome_pasta}.zip")

    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                caminho_relativo = os.path.relpath(caminho_arquivo, pasta_origem)
                zipf.write(caminho_arquivo, caminho_relativo)
    print(f"\nPasta '{pasta_origem}' compactada em '{caminho_zip}' com sucesso!")

def descompactar_zip(arquivo_zip):
    # Define o diretório destino como o mesmo onde está o arquivo ZIP
    pasta_destino = os.path.dirname(os.path.abspath(arquivo_zip))

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
        compactar_pasta(pasta)

    elif escolha == '2':
        arquivo_zip = input("Digite o caminho do arquivo zip para descompactar: ").strip()
        descompactar_zip(arquivo_zip)

    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
