import requests
import json
import re
import time

# Carrega o JSON
with open("bandas_e_albuns.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

bandas = list(dados["bandas"].keys())
albuns_ouvidos_dict = dados["bandas"]

def normalizar(nome):
    nome = nome.lower()
    nome = re.sub(r"\(.*?\)", "", nome)

    palavras_ignoradas = [
        "deluxe", "extended", "special", "edition", "remaster", "expanded",
        "live", "demo", "version", "anniversary", "bonus", "reissue",
        "instrumental", "session", "sessions", "remastered", "remix", "remixed",
        "ao vivo", "acoustic"
    ]

    for palavra in palavras_ignoradas:
        nome = re.sub(rf"\b{palavra}\b", "", nome)

    nome = re.sub(r"\s+", " ", nome).strip()
    return nome


# 🔍 Buscar artista
def buscar_artista_mb(nome):
    url = "https://musicbrainz.org/ws/2/artist/"
    params = {
        "query": nome,
        "fmt": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "app-musica/1.0 (matheus-dev)"
    }

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    artistas = data.get("artists", [])
    return artistas[0]["id"] if artistas else None


# 🎧 Pegar lançamento mais recente
def pegar_lancamento_mais_recente_mb(artist_id):
    url = "https://musicbrainz.org/ws/2/release-group"
    params = {
        "artist": artist_id,
        "fmt": "json",
        "limit": 100
    }

    headers = {
        "User-Agent": "app-musica/1.0 (matheus-dev)"
    }

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    releases = data.get("release-groups", [])

    # filtrar só álbuns (ignorar singles, etc.)
    releases = [r for r in releases if r.get("primary-type") == "Album"]

    # manter só os que têm data
    releases = [r for r in releases if "first-release-date" in r]

    # remover duplicados pelo nome
    vistos = set()
    unicos = []

    for rls in releases:
        nome = rls["title"]
        if nome not in vistos:
            vistos.add(nome)
            unicos.append(rls)

    # ordenar por data
    unicos.sort(key=lambda x: x["first-release-date"], reverse=True)

    return unicos[0] if unicos else None


print("🎧 Lançamentos recentes:\n")

nao_ouvidos = []

for banda in bandas:
    artist_id = buscar_artista_mb(banda)

    if artist_id:
        # ⏳ evitar bloqueio da API (MusicBrainz pede isso)
        time.sleep(1)

        album = pegar_lancamento_mais_recente_mb(artist_id)

        if album:
            nome_album = album["title"]
            data = album.get("first-release-date", "????")
            tipo = album.get("primary-type", "Album")

            nome_norm = normalizar(nome_album)
            ouvidos_norm = [normalizar(a) for a in albuns_ouvidos_dict.get(banda, [])]

            if nome_norm not in ouvidos_norm:
                print(f"🔊 {banda} lançou: {nome_album} ({tipo}) — {data} [Você ainda não ouviu!]")
                nao_ouvidos.append(f"{banda}: {nome_album} ({tipo}) — {data}")

                # 💾 Atualiza o JSON
                albuns_ouvidos_dict[banda] = [nome_album]

                with open("bandas_e_albuns.json", "w", encoding="utf-8") as f:
                    json.dump(dados, f, indent=2, ensure_ascii=False)

            else:
                print(f"✔️ {banda}: {nome_album} ({tipo}) — {data} [Você já ouviu]")

        else:
            print(f"⚠️ Nenhum lançamento encontrado para {banda}")
    else:
        print(f"❌ Artista não encontrado: {banda}")


# 📄 Salvar TXT
if nao_ouvidos:
    with open("nao_ouvidos.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(nao_ouvidos))
    print("\n📄 Arquivo 'nao_ouvidos.txt' salvo.")
else:
    print("\n✅ Nenhum lançamento novo não ouvido encontrado!")