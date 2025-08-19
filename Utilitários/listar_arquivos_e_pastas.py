import os

# Cores ANSI para terminal
VERDE = "\033[92m"    # Pastas
AZUL = "\033[94m"     # Arquivos
RESET = "\033[0m"     # Resetar cor

# Ícones
ICONE_PASTA = "📁"
ICONE_ARQUIVO = "📄"

def listar_arquivos(caminho):
    arquivos = [item for item in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, item))]
    if arquivos:
        print(f"\n{AZUL}Arquivos no diretório '{caminho}':{RESET}")
        for arquivo in arquivos:
            print(f"{AZUL}{ICONE_ARQUIVO} {arquivo}{RESET}")
    else:
        print("Nenhum arquivo encontrado.")

def listar_pastas(caminho):
    pastas = [item for item in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, item))]
    if pastas:
        print(f"\n{VERDE}Pastas no diretório '{caminho}':{RESET}")
        for pasta in pastas:
            print(f"{VERDE}{ICONE_PASTA} {pasta}{RESET}")
    else:
        print("Nenhuma pasta encontrada.")

def listar_conteudo():
    caminho = input("Digite o caminho da pasta no Windows: ")
    
    if not os.path.isdir(caminho):
        print("O caminho digitado não é uma pasta válida.")
        return
    
    print("\nEscolha o que deseja listar:")
    print("1 - Arquivos")
    print("2 - Pastas")
    print("3 - Ambos (Arquivos e Pastas)")
    
    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        listar_arquivos(caminho)
    elif opcao == "2":
        listar_pastas(caminho)
    elif opcao == "3":
        listar_pastas(caminho)
        listar_arquivos(caminho)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    listar_conteudo()
