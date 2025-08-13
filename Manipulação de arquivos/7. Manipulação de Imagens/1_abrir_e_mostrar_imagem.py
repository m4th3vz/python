import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(diretorio_atual, "minha_imagem.jpg")

# Abrir a imagem
imagem = Image.open(caminho_imagem)

# Mostrar a imagem em uma janela
imagem.show()
