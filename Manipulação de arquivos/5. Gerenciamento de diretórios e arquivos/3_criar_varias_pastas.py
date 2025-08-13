import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Lista com caminhos de pastas para criar (relativos ao diretório do script)
# Dentro da pasta 'projetos' será criada as pastas 'python' e 'javascript' e dentro da pasta 'documentos' será criada as pastas 'textos' e 'imagens'
pastas_para_criar = [
    "projetos/python",
    "projetos/javascript",
    "documentos/textos",
    "documentos/imagens"
]

for pasta_relativa in pastas_para_criar:
    caminho_completo = os.path.join(diretorio_atual, pasta_relativa)
    if not os.path.exists(caminho_completo):
        os.makedirs(caminho_completo)
        print(f"Pasta criada: {caminho_completo}")
    else:
        print(f"Pasta já existe: {caminho_completo}")
