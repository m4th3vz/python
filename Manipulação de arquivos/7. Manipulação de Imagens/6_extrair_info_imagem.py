import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
imagem_entrada = os.path.join(diretorio_atual, "minha_imagem.jpg")

# Abrir a imagem
imagem = Image.open(imagem_entrada)

# Extrair informações
formato = imagem.format          # Ex: JPEG, PNG
tamanho = imagem.size            # (largura, altura)
modo = imagem.mode               # Ex: RGB, RGBA, L (tons de cinza)

print(f"Formato: {formato}")
print(f"Tamanho: {tamanho[0]} x {tamanho[1]} pixels")
print(f"Modo de cor: {modo}")
