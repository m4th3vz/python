import os
from PIL import Image

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
imagem_entrada = os.path.join(diretorio_atual, "minha_imagem.jpg")
imagem_saida = os.path.join(diretorio_atual, "minha_imagem_redimensionada.jpg")

# Abrir a imagem
imagem = Image.open(imagem_entrada)

# Novo tamanho mantendo proporção (exemplo: largura = 300px)
nova_largura = 300
largura_original, altura_original = imagem.size
nova_altura = int((nova_largura / largura_original) * altura_original)

# Redimensionar usando o filtro LANCZOS
imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)

# Salvar a imagem redimensionada
imagem_redimensionada.save(imagem_saida)

print(f"Imagem redimensionada salva como '{imagem_saida}'.")
