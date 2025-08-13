import os

# Pasta onde procurar
pasta = "."
# Texto que queremos buscar
texto_procurado = "import"

# Percorrer todos os arquivos da pasta e subpastas
for raiz, _, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, arquivo)
        
        # Ler somente arquivos de texto
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                for numero_linha, linha in enumerate(f, start=1):
                    if texto_procurado in linha:
                        print(f"[{caminho_arquivo}] Linha {numero_linha}: {linha.strip()}")
        except (UnicodeDecodeError, PermissionError):
            # Ignora arquivos binários ou protegidos
            continue
