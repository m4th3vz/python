import os

def listar_arquivos():
    caminho = input("Digite o caminho da pasta no Windows: ")
    
    # Verifica se o caminho existe e é uma pasta
    if os.path.isdir(caminho):
        arquivos = os.listdir(caminho)
        print(f"Arquivos na pasta '{caminho}':")
        for arquivo in arquivos:
            # Mostra apenas arquivos, não subpastas
            if os.path.isfile(os.path.join(caminho, arquivo)):
                print(arquivo)
    else:
        print("O caminho digitado não é uma pasta válida.")

if __name__ == "__main__":
    listar_arquivos()
