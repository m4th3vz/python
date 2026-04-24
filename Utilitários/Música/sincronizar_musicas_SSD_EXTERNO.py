"""
Este script copia automaticamente arquivos de uma pasta de origem
para um destino (como um HD externo), preservando toda a estrutura
de diretórios (artistas, álbuns, etc.).

Características:
- Copia apenas arquivos que ainda não existem no destino
- Ignora arquivos e pastas ocultas do sistema (Windows)
- Mantém a organização original da biblioteca
- Evita sobrescrever arquivos já existentes
- Possui verificação de segurança para prevenir cópias acidentais

Observação:
A comparação é feita apenas pela existência do arquivo no destino.
Arquivos modificados com o mesmo nome não serão atualizados.
"""

import os
import shutil
import ctypes

# --------------------------------------------------
# FUNÇÃO PARA DETECTAR ARQUIVOS/PASTAS OCULTOS (WINDOWS)
# --------------------------------------------------
def arquivo_oculto(caminho):
    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_SYSTEM = 0x04

    try:
        atributos = ctypes.windll.kernel32.GetFileAttributesW(caminho)
        if atributos == -1:
            return False
        return bool(atributos & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
    except Exception:
        return False

# --------------------------------------------------
# PASTAS RAIZ PARA SINCRONIZAÇÃO
# --------------------------------------------------
pastas_para_sincronizar = [
    (r"C:\Users\user\Music", r"F:\Músicas"),
]
# --------------------------------------------------

for origem, destino in pastas_para_sincronizar:

    print(f"\nSincronizando:\n{origem}\n→ {destino}")

    if not os.path.isdir(origem):
        print("❌ Pasta de origem não encontrada.")
        continue

    # 🔴 VERIFICAÇÃO DE SEGURANÇA
    if not os.path.exists(destino):
        print(f"\n⚠️ A pasta de destino '{destino}' NÃO existe!")

        resposta = input("Deseja criar e continuar mesmo assim? (s/n): ").strip().lower()

        if resposta != "s":
            print("❌ Operação cancelada pelo usuário.")
            continue
        else:
            os.makedirs(destino, exist_ok=True)
            print("✔ Pasta criada, continuando...")

    copiados = 0

    for raiz, dirs, arquivos in os.walk(origem):

        # 🔹 Remove pastas ocultas
        dirs[:] = [
            d for d in dirs
            if not arquivo_oculto(os.path.join(raiz, d))
        ]

        for nome in arquivos:
            caminho_origem = os.path.join(raiz, nome)

            # 🔹 Ignora arquivos ocultos
            if arquivo_oculto(caminho_origem):
                continue

            caminho_relativo = os.path.relpath(caminho_origem, origem)
            caminho_destino = os.path.join(destino, caminho_relativo)

            os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

            if not os.path.exists(caminho_destino):
                shutil.copy2(caminho_origem, caminho_destino)
                copiados += 1
                print(f"Novo: {caminho_destino}")

    if copiados == 0:
        print("✔ Nenhuma alteração encontrada.")
    else:
        print(f"✔ {copiados} arquivo(s) copiado(s).")

print("\nSincronização finalizada.")