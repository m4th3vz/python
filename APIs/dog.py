# Dog API - Imagem aleatória de cachorro
import requests

url = "https://dog.ceo/api/breeds/image/random"
res = requests.get(url).json()

print("\nImagem de cachorro:", res["message"])