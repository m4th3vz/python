import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
imagem_entrada = os.path.join(diretorio_atual, "minha_imagem.jpg")
imagem_saida = os.path.join(diretorio_atual, "minha_imagem_convertida.png")

# Abrir a imagem
imagem = Image.open(imagem_entrada)

# Salvar em outro formato (PNG neste exemplo)
imagem.save(imagem_saida)

print(f"Imagem salva em novo formato: {imagem_saida}")
