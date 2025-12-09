# Open Library - Buscar livro
import requests

livro = "orgulho e preconceito"
url = f"https://openlibrary.org/search.json?title={livro}"
res = requests.get(url).json()

print("\nLivro encontrado:", res["docs"][0]["title"])
print("Autor:", res["docs"][0].get("author_name", ["Desconhecido"])[0])