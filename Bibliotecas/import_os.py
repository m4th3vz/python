# Interage com o sistema operacional, permitindo a manipulação de arquivos, diretórios e variáveis de ambiente.
import os

# Listando arquivos e pastas no diretório atual
print("\nArquivos e pastas no diretório atual:")
for item in os.listdir():
    print("-", item)
