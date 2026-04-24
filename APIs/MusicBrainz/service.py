import re
from datetime import datetime

def normalizar(nome):
    nome = nome.lower()
    nome = re.sub(r"\(.*?\)", "", nome)

    ignoradas = [
        "deluxe", "remaster", "live", "edition", "bonus", "remix"
    ]

    for palavra in ignoradas:
        nome = re.sub(rf"\b{palavra}\b", "", nome)

    return re.sub(r"\s+", " ", nome).strip()


def parse_data(data):
    try:
        return datetime.strptime(data, "%Y-%m-%d")
    except:
        return datetime.min


def filtrar_albuns(releases):
    albuns = [
        r for r in releases
        if r.get("primary-type") == "Album"
        and "first-release-date" in r
    ]

    vistos = set()
    unicos = []

    for r in albuns:
        if r["title"] not in vistos:
            vistos.add(r["title"])
            unicos.append(r)

    unicos.sort(
        key=lambda x: parse_data(x["first-release-date"]),
        reverse=True
    )

    return unicos


def ja_ouvido(nome_album, lista_ouvidos):
    nome_norm = normalizar(nome_album)
    return any(normalizar(a) == nome_norm for a in lista_ouvidos)