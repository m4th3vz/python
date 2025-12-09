# Usado para enviar requisições HTTP, facilitando o consumo de APIs e a interação com servidores web.
import requests

usuario = input("Digite o nome de usuário do GitHub: ")
url = f"https://api.github.com/users/{usuario}"

resposta = requests.get(url)
dados = resposta.json()

print("Nome:", dados["name"])
print("Bio:", dados["bio"])
print("Repositórios públicos:", dados["public_repos"])
