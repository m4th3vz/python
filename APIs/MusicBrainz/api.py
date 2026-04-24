import requests

HEADERS = {
    "User-Agent": "app-musica/1.0 (matheus-dev)"
}

def buscar_artista(nome):
    url = "https://musicbrainz.org/ws/2/artist/"
    params = {
        "query": nome,
        "fmt": "json",
        "limit": 1
    }

    r = requests.get(url, params=params, headers=HEADERS)
    data = r.json()

    artistas = data.get("artists", [])
    return artistas[0]["id"] if artistas else None


def buscar_lancamentos(artist_id):
    url = "https://musicbrainz.org/ws/2/release-group"
    params = {
        "artist": artist_id,
        "fmt": "json",
        "limit": 100
    }

    r = requests.get(url, params=params, headers=HEADERS)
    return r.json().get("release-groups", [])