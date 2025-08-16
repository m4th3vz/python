import os

folder_name = "nome_da_pasta"
os.makedirs(folder_name, exist_ok=True)

conteudo = """# Comentário

Aqui fica o código!
"""

# número de arquivos que deseja
quantidade = 6  

for i in range(1, quantidade + 1):
    filename = f"nome_do_arquivo_{i}.py"
    with open(os.path.join(folder_name, filename), "w", encoding="utf-8") as f:
        f.write(conteudo)

print(f"Pasta '{folder_name}' criada com {quantidade} arquivos genéricos.")
