# JSONPlaceholder - Posts fictícios
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
res = requests.get(url).json()

print("\nTítulo do post:", res["title"])
print("Conteúdo:", res["body"])