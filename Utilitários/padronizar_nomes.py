"""
Script para renomear todos os arquivos de um diretório (e suas subpastas),
deixando apenas a primeira letra maiúscula e o restante em minúsculo,
preservando os acentos.
"""


import os

def renomear_arquivos(diretorio):
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho_antigo = os.path.join(raiz, nome_arquivo)

            # Separa nome e extensão
            nome, extensao = os.path.splitext(nome_arquivo)

            # Primeira letra maiúscula e resto minúsculo
            novo_nome = nome.capitalize() + extensao.lower()

            caminho_novo = os.path.join(raiz, novo_nome)

            # Evita sobrescrever caso já exista
            if caminho_antigo != caminho_novo:
                os.rename(caminho_antigo, caminho_novo)
                print(f'Renomeado: "{caminho_antigo}" -> "{caminho_novo}"')

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ").strip()
    
    if os.path.isdir(pasta):
        renomear_arquivos(pasta)
        print("\n✅ Renomeação concluída!")
    else:
        print("❌ Caminho inválido. Verifique e tente novamente.")
