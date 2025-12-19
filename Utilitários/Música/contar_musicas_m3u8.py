"""
Este script lê um arquivo de playlist no formato .m3u8,
extrai as músicas contidas nele e exibe:
- quantidade total de músicas
- duração total da playlist (hh:mm:ss)
"""

def ler_playlist_m3u8(caminho_arquivo):
    musicas = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()

        if linha.startswith('#EXTINF'):
            duracao, nome = linha.replace('#EXTINF:', '').split(',', 1)
            caminho = linhas[i + 1].strip()

            musicas.append({
                'nome': nome,
                'duracao_segundos': int(duracao),
                'arquivo': caminho
            })

            i += 2
        else:
            i += 1

    return musicas


def formatar_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f'{horas:02}:{minutos:02}:{segundos:02}'


# ===== Programa principal =====
caminho_playlist = input('Digite o caminho do arquivo .m3u8: ').strip()

try:
    playlist = ler_playlist_m3u8(caminho_playlist)

    total_musicas = len(playlist)
    duracao_total = sum(m['duracao_segundos'] for m in playlist)

    print(f'Total de músicas: {total_musicas}')
    print(f'Duração total: {formatar_tempo(duracao_total)}')

except FileNotFoundError:
    print('Erro: arquivo não encontrado. Verifique o caminho informado.')

except Exception as erro:
    print(f'Ocorreu um erro ao ler a playlist: {erro}')
