"""
Script para criar automaticamente um arquivo .gitignore padrão em um projeto Python.
Inclui regras comuns para arquivos de ambiente, bytecode, logs, configurações do VSCode
e pastas de virtualenv.
"""

import os

conteudo = """# Arquivos de ambiente
.env

# Bytecode do Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Arquivos de log
*.log

# Configurações do VSCode (se usar)
.vscode/

# Arquivos temporários de sistema
.DS_Store
Thumbs.db

# Pastas de virtualenv
venv/
env/
"""

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_gitignore = os.path.join(diretorio_do_script, '.gitignore')

with open(caminho_gitignore, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)

print(f'.gitignore criado com sucesso em: {caminho_gitignore}')
