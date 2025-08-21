import os

def listar_arquivos(diretorio, extensao=None):
    arquivos_encontrados = []

    # Percorre todos os diretórios e subdiretórios
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if extensao:
                if arquivo.endswith(extensao):
                    arquivos_encontrados.append(os.path.join(raiz, arquivo))
            else:
                arquivos_encontrados.append(os.path.join(raiz, arquivo))

    return arquivos_encontrados

def main():
    diretorio = input("Digite o diretório para procurar os arquivos: ").strip()
    escolha = input("Deseja procurar arquivos com alguma extensão específica? (Digite a extensão ou deixe vazio para mostrar todos): ").strip()

    # Se o usuário deixar vazio, será None
    extensao = escolha if escolha else None

    arquivos = listar_arquivos(diretorio, extensao)

    if arquivos:
        print("\nArquivos encontrados:")
        for arquivo in arquivos:
            print(arquivo)
        print(f"\nTotal de arquivos encontrados: {len(arquivos)}")
    else:
        print("Nenhum arquivo encontrado.")

if __name__ == "__main__":
    main()
