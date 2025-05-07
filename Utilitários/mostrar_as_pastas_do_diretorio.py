# O módulo pathlib fornece classes para manipular caminhos de arquivos e diretórios de forma orientada a objetos, tornando o código mais limpo, legível e multiplataforma.
# Ele cuida automaticamente do uso correto das barras ('/' no Linux/macOS e '\' no Windows).
from pathlib import Path

# Define o caminho do diretório desejado (use r'' para evitar erros com barras invertidas)
caminho = Path(r'C:\Users\user\Documents\GitHub\python')

# Cria uma lista com os nomes das pastas dentro do diretório
pastas = [pasta.name for pasta in caminho.iterdir() if pasta.is_dir()]

# Exibe os nomes das pastas
for pasta in pastas:
    print(pasta)
