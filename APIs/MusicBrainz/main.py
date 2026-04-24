import json
import time
import os

from api import buscar_artista, buscar_lancamentos
from service import filtrar_albuns, ja_ouvido

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "bandas_e_albuns.json")

# carregar dados
with open(FILE_PATH, "r", encoding="utf-8") as f:
    dados = json.load(f)

bandas = list(dados["bandas"].keys())
albuns_ouvidos = dados["bandas"]

nao_ouvidos = []

print("🎧 Lançamentos recentes:\n")

for banda in bandas:
    artist_id = buscar_artista(banda)

    if not artist_id:
        print(f"❌ {banda} não encontrado")
        continue

    time.sleep(1)

    releases = buscar_lancamentos(artist_id)
    albuns = filtrar_albuns(releases)

    if not albuns:
        print(f"⚠️ Nenhum álbum para {banda}")
        continue

    album = albuns[0]
    nome = album["title"]
    data = album["first-release-date"]

    if not ja_ouvido(nome, albuns_ouvidos.get(banda, [])):
        print(f"🔊 {banda} lançou: {nome} — {data}")

        nao_ouvidos.append(f"{banda}: {nome} — {data}")
        albuns_ouvidos[banda] = [nome]

    else:
        print(f"✔️ {banda}: {nome} já ouvido")


# salvar tudo no final
with open("bandas_e_albuns.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

if nao_ouvidos:
    with open("nao_ouvidos.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(nao_ouvidos))

    print("\n📄 arquivo salvo")
else:
    print("\n✅ tudo atualizado")