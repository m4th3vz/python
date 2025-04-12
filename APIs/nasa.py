# NASA - Astronomy Picture of the Day
import requests

api_key = "DEMO_KEY"  # Chave gratuita da NASA
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
res = requests.get(url).json()

print("Título:", res["title"])
print("Data:", res["date"])
print("Explicação:", res["explanation"])
print("URL da imagem:", res["url"])