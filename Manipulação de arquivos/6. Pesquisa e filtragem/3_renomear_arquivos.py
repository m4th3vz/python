import os

# Solicitar informações ao usuário
pasta = input("Digite o caminho da pasta: ").strip()
novo_nome = input("Digite o novo nome base para os arquivos: ").strip()

# Extensões que deseja renomear
# extensoes = [".jpg", ".png", ".txt"]

# Deixe vazio [] para renomear todos os arquivos
extensoes = []

# Contador para diferenciar os arquivos
contador = 1

for nome_arquivo in os.listdir(pasta):
    caminho_antigo = os.path.join(pasta, nome_arquivo)

    # Pular pastas
    if os.path.isdir(caminho_antigo):
        continue

    # Verificar extensão, se filtrada
    nome, ext = os.path.splitext(nome_arquivo)
    if extensoes and ext.lower() not in extensoes:
        continue

    # Criar novo nome
    novo_nome_arquivo = f"{novo_nome}_{contador}{ext}"
    caminho_novo = os.path.join(pasta, novo_nome_arquivo)

    # Renomear
    os.rename(caminho_antigo, caminho_novo)
    print(f"Renomeado: {nome_arquivo} → {novo_nome_arquivo}")

    contador += 1

print("Renomeação concluída!")
