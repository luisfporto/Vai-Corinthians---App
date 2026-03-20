import urllib.request
import json
import urllib.parse
import re

players = [
    ("Hugo Souza", "Hugo Souza (futebolista, 1999)"),
    ("Matheus Donelli", "Matheus Donelli"),
    ("Fagner", "Fagner (futebolista)"),
    ("Matheuzinho", "Matheuzinho (futebolista, 2000)"),
    ("Hugo", "Hugo (futebolista, 1997)"),
    ("Matheus Bidu", "Matheus Bidu"),
    ("André Ramalho", "André Ramalho"),
    ("Félix Torres", "Félix Torres (futebolista)"),
    ("Gustavo Henrique", "Gustavo Henrique (futebolista, 1993)"),
    ("Cacá", "Cacá (futebolista, 1999)"),
    ("Raniele", "Raniele"),
    ("José Martínez", "José Andrés Martínez"),
    ("Charles", "Charles Rigon Matos"),
    ("Alex Santana", "Alex Santana"),
    ("Breno Bidon", "Breno Bidon"),
    ("Rodrigo Garro", "Rodrigo Garro"),
    ("Igor Coronado", "Igor Coronado"),
    ("Yuri Alberto", "Yuri Alberto"),
    ("Memphis Depay", "Memphis Depay"),
    ("Ángel Romero", "Ángel Romero (futebolista)"),
    ("Talles Magno", "Talles Magno"),
    ("Pedro Henrique", "Pedro Henrique (futebolista, 1990)")
]

def get_wiki_image(title):
    try:
        url = "https://pt.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=" + urllib.parse.quote(title)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id in pages:
            if 'original' in pages[page_id]:
                return pages[page_id]['original']['source']
    except Exception:
        pass
    return None

photo_map = {}
for name, query in players:
    img = get_wiki_image(query)
    if not img: # fallback to english wiki
        try:
            url = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=" + urllib.parse.quote(query)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
            pages = data['query']['pages']
            for page_id in pages:
                if 'original' in pages[page_id]:
                    img = pages[page_id]['original']['source']
        except: pass
    if img:
        photo_map[name] = img
        
print(json.dumps(photo_map, indent=2))
