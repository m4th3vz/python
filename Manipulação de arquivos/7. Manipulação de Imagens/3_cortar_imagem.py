import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
imagem_entrada = os.path.join(diretorio_atual, "minha_imagem.jpg")
imagem_saida = os.path.join(diretorio_atual, "minha_imagem_cortada.jpg")

# Abrir a imagem
imagem = Image.open(imagem_entrada)

# Definir a área a ser cortada (box): (esquerda, superior, direita, inferior)
# Exemplo: cortar um retângulo começando em (100, 100) até (400, 400)
caixa = (100, 100, 400, 400)

# Cortar a imagem
imagem_cortada = imagem.crop(caixa)

# Salvar a imagem cortada
imagem_cortada.save(imagem_saida)

print(f"Imagem cortada salva como '{imagem_saida}'.")
