from decouple import config
import requests
import base64
import json
import re

# 🧾 Substitua pelas suas chaves do Spotify Developer
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

# 📂 Carrega bandas e álbuns ouvidos do arquivo JSON
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

def get_token():
    auth = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth.encode()).decode()
    headers = {"Authorization": f"Basic {b64_auth}"}
    data = {"grant_type": "client_credentials"}
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return r.json().get("access_token")

def buscar_artista_id(nome, token):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": nome, "type": "artist", "limit": 1}
    r = requests.get(url, headers=headers, params=params)
    items = r.json().get("artists", {}).get("items", [])
    return items[0]["id"] if items else None

def pegar_lancamento_mais_recente(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "include_groups": "album",  # apenas álbuns/EPs
        "limit": 50,
        "market": "BR"
    }
    r = requests.get(url, headers=headers, params=params)
    albums = r.json().get("items", [])

    vistos = set()
    unicos = []
    for album in albums:
        nome = album["name"]
        if nome not in vistos:
            vistos.add(nome)
            unicos.append(album)

    unicos.sort(key=lambda x: x["release_date"], reverse=True)
    return unicos[0] if unicos else None

# 🔁 Executa
token = get_token()
print("🎧 Lançamentos recentes:\n")
nao_ouvidos = []

for banda in bandas:
    artist_id = buscar_artista_id(banda, token)
    if artist_id:
        album = pegar_lancamento_mais_recente(artist_id, token)
        if album:
            nome_album = album["name"]
            data = album["release_date"]
            tipo = album["album_type"]

            nome_norm = normalizar(nome_album)
            ouvidos_norm = [normalizar(a) for a in albuns_ouvidos_dict.get(banda, [])]

            if nome_norm not in ouvidos_norm:
                print(f"🔊 {banda} lançou: {nome_album} ({tipo}) — {data} [Você ainda não ouviu!]")
                nao_ouvidos.append(f"{banda}: {nome_album} ({tipo}) — {data}")
            else:
                print(f"✔️ {banda}: {nome_album} ({tipo}) — {data} [Você já ouviu]")
        else:
            print(f"⚠️ Nenhum lançamento encontrado para {banda}")
    else:
        print(f"❌ Artista não encontrado: {banda}")

# 💾 Salva em arquivo os lançamentos não ouvidos
if nao_ouvidos:
    with open("nao_ouvidos.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(nao_ouvidos))
    print("\n📄 Arquivo 'nao_ouvidos.txt' salvo com os lançamentos que você ainda não ouviu.")
else:
    print("\n✅ Nenhum lançamento novo não ouvido encontrado!")
