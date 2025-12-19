"""
Detecta músicas duplicadas usando nome do arquivo + duração real.
Rápido e eficiente para bibliotecas grandes.
"""

import os
from mutagen import File

EXTENSOES_AUDIO = ('.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac')


def obter_duracao(caminho):
    try:
        audio = File(caminho)
        if audio and audio.info:
            return int(audio.info.length)
    except:
        pass
    return None


def detectar_duplicatas(pasta):
    musicas = {}

    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith(EXTENSOES_AUDIO):
                caminho = os.path.join(raiz, arquivo)
                duracao = obter_duracao(caminho)

                if duracao is None:
                    continue

                chave = (arquivo.lower(), duracao)

                musicas.setdefault(chave, []).append(caminho)

    return {k: v for k, v in musicas.items() if len(v) > 1}


# ===== Programa principal =====
pasta_musicas = input('Digite o caminho da pasta de músicas: ').strip()

duplicatas = detectar_duplicatas(pasta_musicas)

if not duplicatas:
    print('Nenhuma música duplicada encontrada.')
else:
    print('Músicas duplicadas encontradas:\n')
    for (_, duracao), arquivos in duplicatas.items():
        print(f'Duração: {duracao}s')
        for a in arquivos:
            print(f'  - {a}')
        print()
