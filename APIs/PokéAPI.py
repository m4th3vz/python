# PokéAPI - Informações sobre um Pokémon
import requests

pokemon = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
res = requests.get(url).json()

print("\nNome:", res["name"].title())
print("Altura:", res["height"])
print("Peso:", res["weight"])
tipos = [tipo['type']['name'] for tipo in res['types']]
print("Tipos:", ", ".join(tipos))