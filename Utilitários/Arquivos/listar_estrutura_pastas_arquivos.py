'''
Script que lista todas as pastas, subpastas e arquivos de um diretório,
exibindo a estrutura hierárquica com ícones e cores personalizadas (24-bit ANSI).
As pastas usam a cor #fbdb76 (amarelo-bege) e os arquivos aparecem em branco.
'''

import os

# Códigos de cor (ANSI 24-bit)
COR_PASTA = "\033[38;2;251;219;118m"   # #fbdb76
COR_ARQUIVO = "\033[38;2;230;230;230m" # branco suave
COR_RESET = "\033[0m"                   # reset de cor

def listar_pastas(caminho_inicial, nivel=0):
    try:
        itens = sorted(os.listdir(caminho_inicial))
    except PermissionError:
        print("  " * nivel + f"[Sem permissão] {caminho_inicial}")
        return
    except FileNotFoundError:
        print(f"Caminho não encontrado: {caminho_inicial}")
        return

    # Primeiro, mostra arquivos do diretório atual
    for item in itens:
        caminho_completo = os.path.join(caminho_inicial, item)
        if os.path.isfile(caminho_completo):
            print("  " * (nivel + 1) + f"{COR_ARQUIVO}[📄] {item}{COR_RESET}")

    # Depois, mostra pastas e entra nelas
    for item in itens:
        caminho_completo = os.path.join(caminho_inicial, item)
        if os.path.isdir(caminho_completo):
            print("  " * nivel + f"{COR_PASTA}[📁] {item}{COR_RESET}")
            listar_pastas(caminho_completo, nivel + 1)

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta que deseja listar: ").strip()
    if not caminho:
        caminho = "."
    print(f"\nEstrutura de pastas em: {os.path.abspath(caminho)}\n")
    listar_pastas(caminho)
