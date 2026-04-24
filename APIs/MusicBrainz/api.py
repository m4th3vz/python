# api.py

import requests

HEADERS = {
    "User-Agent": "app-musica/1.0 (matheus-dev)"
}

BASE_URL = "https://musicbrainz.org/ws/2"


def buscar_artista(nome):
    url = f"{BASE_URL}/artist/"
    params = {
        "query": nome,
        "fmt": "json",
        "limit": 1
    }

    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=10)
        r.raise_for_status()
        data = r.json()
    except (requests.RequestException, ValueError):
        return None

    artistas = data.get("artists", [])
    return artistas[0]["id"] if artistas else None


def buscar_lancamentos(artist_id):
    url = f"{BASE_URL}/release-group"
    params = {
        "artist": artist_id,
        "fmt": "json",
        "limit": 100
    }

    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=10)
        r.raise_for_status()
        data = r.json()
    except (requests.RequestException, ValueError):
        return []

    return data.get("release-groups", [])