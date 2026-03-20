import json
import re

with open(r'app\src\main\java\com\a15032\vaicorinthiansapp\MainActivity.kt', 'r', encoding='utf-8') as f:
    text = f.read()

tm_photos = {
    "Hugo Souza": "https://img.a.transfermarkt.technology/portrait/medium/574901-1758160198.jpg?lm=1",
    "Matheus Donelli": "https://img.a.transfermarkt.technology/portrait/medium/708723-1725326064.jpg?lm=1",
    "André Ramalho": "https://img.a.transfermarkt.technology/portrait/medium/175792-1721347430.jpg?lm=1",
    "Gustavo Henrique": "https://img.a.transfermarkt.technology/portrait/medium/208681-1725326922.jpg?lm=1",
    "Matheus Bidu": "https://img.a.transfermarkt.technology/portrait/medium/670021-1660574686.jpg?lm=1",
    "Hugo": "https://img.a.transfermarkt.technology/portrait/medium/730708-1700062381.jpg?lm=1",
    "Matheuzinho": "https://img.a.transfermarkt.technology/portrait/medium/594226-1725325967.jpg?lm=1",
    "Raniele": "https://img.a.transfermarkt.technology/portrait/medium/546530-1680488285.jpg?lm=1",
    "Charles": "https://img.a.transfermarkt.technology/portrait/medium/486078-1771002454.jpg?lm=1",
    "Breno Bidon": "https://img.a.transfermarkt.technology/portrait/medium/1029227-1725327135.jpg?lm=1",
    "Alex Santana": "https://img.a.transfermarkt.technology/portrait/medium/219835-1622913468.png?lm=1",
    "Rodrigo Garro": "https://img.a.transfermarkt.technology/portrait/medium/565009-1725327608.jpg?lm=1",
    "Memphis Depay": "https://img.a.transfermarkt.technology/portrait/medium/167850-1668167349.jpg?lm=1",
    "Yuri Alberto": "https://img.a.transfermarkt.technology/portrait/medium/489893-1744075236.jpg?lm=1"
}

def replace_photo(match):
    name = match.group(1)
    rest = match.group(2)
    old_url = match.group(3)
    if name in tm_photos:
        return f'Player("{name}"{rest}, "{tm_photos[name]}")'
    return match.group(0)

# The regex matches Player("name", age, ... , "https://...")
new_text = re.sub(r'Player\("([^"]+)"(.*?), "(https?://[^"]+)"\)', replace_photo, text)

with open(r'app\src\main\java\com\a15032\vaicorinthiansapp\MainActivity.kt', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Transfermarkt Photos applied.")
