# service.py

import re
from datetime import datetime


def normalizar(nome):
    if not nome:
        return ""

    nome = nome.lower()
    nome = re.sub(r"\(.*?\)", "", nome)

    ignoradas = [
        "deluxe", "remaster", "remastered", "live",
        "edition", "bonus", "remix"
    ]

    for palavra in ignoradas:
        nome = re.sub(rf"\b{palavra}\b", "", nome)

    return re.sub(r"\s+", " ", nome).strip()


def parse_data(data):
    if not data:
        return datetime.min

    try:
        return datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        return datetime.min


def filtrar_albuns(releases):
    if not releases:
        return []

    albuns = [
        r for r in releases
        if r.get("primary-type") == "Album"
        and r.get("first-release-date")
    ]

    vistos = set()
    unicos = []

    for r in albuns:
        titulo = r.get("title")
        if not titulo:
            continue

        if titulo not in vistos:
            vistos.add(titulo)
            unicos.append(r)

    unicos.sort(
        key=lambda x: parse_data(x.get("first-release-date")),
        reverse=True
    )

    return unicos


def ja_ouvido(nome_album, lista_ouvidos):
    if not nome_album:
        return False

    nome_norm = normalizar(nome_album)

    return any(
        normalizar(a) == nome_norm
        for a in lista_ouvidos if a
    )