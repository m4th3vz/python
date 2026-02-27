"""
Script para converter automaticamente imagens JPG/JPEG em arquivos ICO.
O usuário informa a pasta de origem e a pasta de destino, e o programa
redimensiona as imagens para 256x256 pixels, salvando-as no formato
compatível com ícones do Windows.
"""

import os
from PIL import Image

# Entrada do usuário
PASTA_ORIGEM = input("Digite o caminho da pasta de origem: ").strip()
PASTA_DESTINO = input("Digite o caminho da pasta de destino: ").strip()

# Verifica se a pasta de origem existe
if not os.path.isdir(PASTA_ORIGEM):
    print("❌ A pasta de origem não existe.")
    exit()

# Cria a pasta de destino se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)

for arquivo in os.listdir(PASTA_ORIGEM):
    if arquivo.lower().endswith((".jpg", ".jpeg")):
        caminho_entrada = os.path.join(PASTA_ORIGEM, arquivo)
        nome_base = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(PASTA_DESTINO, f"{nome_base}.ico")

        try:
            with Image.open(caminho_entrada) as img:
                img = img.convert("RGBA")
                img = img.resize((256, 256), Image.LANCZOS)
                img.save(caminho_saida, format="ICO", sizes=[(256, 256)])

            print(f"✔ Convertido: {arquivo}")

        except Exception as e:
            print(f"❌ Erro ao converter {arquivo}: {e}")

print("\nConversão finalizada.")
