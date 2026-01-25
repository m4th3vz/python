import os

# Pasta raiz (entrada do usuário)
PASTA_RAIZ = input("Digite o caminho da pasta raiz: ").strip()

# Verifica se a pasta existe
if not os.path.isdir(PASTA_RAIZ):
    print("❌ A pasta informada não existe.")
    exit()

for pasta_atual, subpastas, arquivos in os.walk(PASTA_RAIZ):
    for arquivo in arquivos:
        if arquivo.lower().endswith(".ico") and arquivo.lower() != "favicon.ico":
            caminho_antigo = os.path.join(pasta_atual, arquivo)
            caminho_novo = os.path.join(pasta_atual, "favicon.ico")

            try:
                os.rename(caminho_antigo, caminho_novo)
                print(f"✔ Renomeado em: {pasta_atual}")

            except Exception as e:
                print(f"❌ Erro em {pasta_atual}: {e}")

print("\nRenomeação finalizada.")
