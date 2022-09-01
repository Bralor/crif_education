import requests
from bs4 import BeautifulSoup


odpoved_serveru = requests.get("https://www.idnes.cz/")
rozdelene_html = BeautifulSoup(odpoved_serveru.content, features="html.parser")
vsechny_elementy_a = rozdelene_html.find_all("a", {"class": "art-link"})
    
clanky = {
    a_tag["href"]: a_tag.get_text()
    for a_tag in vsechny_elementy_a
}

for index, clanek in enumerate(clanky.items(), 1):
    print(f"{index:>2}. {clanek[1].strip()}")

