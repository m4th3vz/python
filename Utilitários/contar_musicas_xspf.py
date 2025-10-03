import xml.etree.ElementTree as ET

# Pede o caminho do arquivo ao usuário
arquivo_xspf = input("Digite o caminho do arquivo .xspf: ")

try:
    # Fazendo o parse do arquivo XML
    tree = ET.parse(arquivo_xspf)
    root = tree.getroot()

    # Namespace do XSPF
    namespaces = {'xspf': 'http://xspf.org/ns/0/'}

    # Encontrando todas as tags <track>
    tracks = root.findall('xspf:trackList/xspf:track', namespaces)
    num_musicas = len(tracks)

    # Somando a duração de todas as músicas (em milissegundos)
    duracao_total_ms = sum(int(track.find('xspf:duration', namespaces).text or 0) for track in tracks)

    # Convertendo para horas, minutos e segundos
    duracao_total_s = duracao_total_ms // 1000
    horas = duracao_total_s // 3600
    minutos = (duracao_total_s % 3600) // 60
    segundos = duracao_total_s % 60

    print(f"Número de músicas na playlist: {num_musicas}")
    print(f"Duração total: {horas}h {minutos}m {segundos}s")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho.")
except ET.ParseError:
    print("Erro ao ler o arquivo. Verifique se é um arquivo .xspf válido.")
