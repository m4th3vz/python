# main.py

import json
import time
import os

from api import buscar_artista, buscar_lancamentos
from service import filtrar_albuns, ja_ouvido


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "bandas_e_albuns.json")
OUTPUT_FILE = FILE_PATH
OUTPUT_TXT = os.path.join(BASE_DIR, "nao_ouvidos.txt")


def carregar_dados(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"bandas": {}}


def salvar_json(path, dados):
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    os.replace(temp_path, path)


# carregar dados
dados = carregar_dados(FILE_PATH)

bandas = list(dados.get("bandas", {}).keys())
albuns_ouvidos = dados.get("bandas", {})

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
    nome = album.get("title")
    data = album.get("first-release-date", "desconhecido")

    if not ja_ouvido(nome, albuns_ouvidos.get(banda, [])):
        print(f"🔊 {banda} lançou: {nome} — {data}")

        nao_ouvidos.append(f"{banda}: {nome} — {data}")
        albuns_ouvidos[banda] = [nome]

    else:
        print(f"✔️ {banda}: {nome} já ouvido")


# salvar JSON com segurança
salvar_json(OUTPUT_FILE, dados)

# salvar TXT apenas se houver novos
if nao_ouvidos:
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(nao_ouvidos))

    print("\n📄 arquivo salvo")
else:
    print("\n✅ tudo atualizado")