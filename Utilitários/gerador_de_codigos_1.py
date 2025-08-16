import os

# Nome da pasta que conterá os arquivos
folder_name = "nome da pasta"
os.makedirs(folder_name, exist_ok=True)

# Dicionário genérico com nomes de arquivos
files_content = {
    "nome_do_arquivo_1.py": """# Comentário

Aqui fica o código!
""",
    "nome_do_arquivo_2.py": """# Comentário

Aqui fica o código!
""",
    "nome_do_arquivo_3.py": """# Comentário

Aqui fica o código!
"""
}

# Criar os arquivos dentro da pasta
for filename, content in files_content.items():
    with open(os.path.join(folder_name, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Pasta '{folder_name}' criada com {len(files_content)} arquivos genéricos.")
