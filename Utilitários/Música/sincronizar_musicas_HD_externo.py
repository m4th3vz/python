"""
Script para sincronizar automaticamente a biblioteca de músicas do PC
com um HD externo de forma incremental.

O script copia apenas arquivos que ainda não existem no destino,
preservando toda a estrutura de subpastas (artistas, álbuns, anos, etc.).
"""

import os
import shutil

# --------------------------------------------------
# PASTAS RAIZ PARA SINCRONIZAÇÃO
# --------------------------------------------------
pastas_para_sincronizar = [
    (r"C:\Users\user\Music", r"E:\Músicas"),
]
# --------------------------------------------------

for origem, destino in pastas_para_sincronizar:

    print(f"\nSincronizando:\n{origem}\n→ {destino}")

    if not os.path.isdir(origem):
        print("❌ Pasta de origem não encontrada.")
        continue

    os.makedirs(destino, exist_ok=True)

    copiados = 0

    for raiz, _, arquivos in os.walk(origem):
        for nome in arquivos:
            caminho_origem = os.path.join(raiz, nome)

            caminho_relativo = os.path.relpath(caminho_origem, origem)
            caminho_destino = os.path.join(destino, caminho_relativo)

            os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

            # 🔹 Reconhecimento apenas por nome
            if not os.path.exists(caminho_destino):
                shutil.copy2(caminho_origem, caminho_destino)
                copiados += 1
                print(f"Novo: {caminho_destino}")

    if copiados == 0:
        print("✔ Nenhuma alteração encontrada.")
    else:
        print(f"✔ {copiados} arquivo(s) copiado(s).")

print("\nSincronização finalizada.")
