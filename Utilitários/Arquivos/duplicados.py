"""
Script para identificar arquivos duplicados em uma pasta e suas subpastas.
O programa calcula o hash MD5 de cada arquivo (ignorando arquivos ocultos)
e agrupa todos os arquivos que possuem conteúdo idêntico. Ao final, exibe
cada grupo de duplicatas, mostrando o caminho completo de todos os arquivos
iguais, incluindo o arquivo original e suas cópias.
"""

import os
import hashlib
import ctypes

# Constante do Windows para identificar arquivo oculto
FILE_ATTRIBUTE_HIDDEN = 0x02

def arquivo_oculto(caminho):
    """Retorna True se o arquivo for oculto."""
    try:
        atributos = ctypes.windll.kernel32.GetFileAttributesW(caminho)
        if atributos == -1:
            return False
        return bool(atributos & FILE_ATTRIBUTE_HIDDEN)
    except:
        return False

def hash_arquivo(caminho):
    """Calcula o hash MD5 do arquivo."""
    h = hashlib.md5()
    with open(caminho, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b''):
            h.update(bloco)
    return h.hexdigest()

# Input do usuário
pasta = input("Digite o caminho da pasta que deseja verificar: ").strip()

if not os.path.isdir(pasta):
    print("Caminho inválido ou pasta inexistente.")
    exit()

# Agora cada hash guarda uma lista completa de arquivos
hashes = {}

for raiz, _, arquivos in os.walk(pasta):
    for nome in arquivos:
        caminho = os.path.join(raiz, nome)

        # Ignora arquivos ocultos
        if arquivo_oculto(caminho):
            continue

        h = hash_arquivo(caminho)

        # Cria lista se for o primeiro arquivo desse hash
        if h not in hashes:
            hashes[h] = []

        hashes[h].append(caminho)

# Exibe grupos completos de duplicados
print("\nArquivos duplicados encontrados:")

encontrou = False
for h, caminhos in hashes.items():
    if len(caminhos) > 1:
        encontrou = True
        print("\n--- Grupo de duplicados ---")
        for c in caminhos:
            print(c)

if not encontrou:
    print("Nenhum arquivo duplicado encontrado.")
