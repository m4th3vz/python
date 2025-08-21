"""
Script para coletar seguidores e seguidos de um usuário no GitHub usando web scraping.
Exibe os usuários que você segue, mas que não te seguem de volta.
"""

import requests
from bs4 import BeautifulSoup

GITHUB_USERNAME = "m4th3vz"  # Seu nome de usuário do GitHub
BASE_URL = f"https://github.com/{GITHUB_USERNAME}"


def get_users(tab):
    """Função para coletar todos os usuários de uma aba (followers ou following)."""
    users = set()
    page = 1

    while True:
        url = f"{BASE_URL}?page={page}&tab={tab}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erro ao acessar {url}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        user_elements = soup.select("span.Link--secondary")

        if not user_elements:  # Se não houver mais usuários, sai do loop
            break

        for user in user_elements:
            username = user.text.strip()
            users.add(f"https://github.com/{username}")

        page += 1  # Passa para a próxima página

    return users


# Coletando seguidores e seguidos
seguidores = get_users("followers")
seguidos = get_users("following")

# Descobrindo quem você segue e não te segue de volta
nao_seguem_de_volta = seguidos - seguidores

# Exibindo o resultado
print("\nUsuários que você segue, mas que não te seguem de volta:")
for user_link in sorted(nao_seguem_de_volta):
    print(user_link)
