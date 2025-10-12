"""
Script para editar arquivos de playlist XSPF, convertendo os caminhos de arquivos
entre Windows e Ubuntu. Permite substituir caminhos do Windows para Ubuntu ou o inverso.
"""

import os

def editar_caminhos_xspf(caminho_arquivo, opcao):
    try:
        # Verifica se o arquivo existe
        if not os.path.isfile(caminho_arquivo):
            print(f"Arquivo não encontrado: {caminho_arquivo}")
            return

        # Lê o conteúdo do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Substitui os caminhos especificados com base na opção
        if opcao == "1":
            conteudo_editado = conteudo.replace(
                '///C:/Users/user/Music/', '///home/matheus/M%C3%BAsicas/'
            ).replace(
                '///C:/Users/user/AppData/Roaming/', '///home/matheus/.cache/'
            )
        elif opcao == "2":
            conteudo_editado = conteudo.replace(
                '///home/matheus/M%C3%BAsicas/', '///C:/Users/user/Music/'
            ).replace(
                '///home/matheus/.cache/', '///C:/Users/user/AppData/Roaming/'
            )
        else:
            print("Opção inválida.")
            return

        # Sobrescreve o arquivo com o conteúdo editado
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_editado)

        print(f"Arquivo editado com sucesso: {caminho_arquivo}")

    except Exception as e:
        print(f"Erro ao editar o arquivo: {e}")

# Solicita o caminho do arquivo XSPF ao usuário
caminho_arquivo_xspf = input("Digite o caminho completo do arquivo XSPF: ")

# Solicita a opção ao usuário
print("Escolha uma opção:")
print("1 - Substituir caminhos de Windows para Ubuntu")
print("2 - Substituir caminhos de Ubuntu para Windows")
opcao = input("Digite sua opção (1 ou 2): ")

# Chama a função para editar o arquivo
editar_caminhos_xspf(caminho_arquivo_xspf, opcao)
