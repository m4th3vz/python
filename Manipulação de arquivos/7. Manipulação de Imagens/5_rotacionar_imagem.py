import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
imagem_entrada = os.path.join(diretorio_atual, "minha_imagem.jpg")
imagem_saida = os.path.join(diretorio_atual, "minha_imagem_rotacionada.jpg")

# Abrir a imagem
imagem = Image.open(imagem_entrada)

# Rotacionar a imagem 90 graus no sentido anti-horário
imagem_rotacionada = imagem.rotate(90, expand=True)

# Salvar a imagem rotacionada
imagem_rotacionada.save(imagem_saida)

print(f"Imagem rotacionada salva como '{imagem_saida}'.")
