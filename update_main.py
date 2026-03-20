import json
import re

with open(r'app\src\main\java\com\a15032\vaicorinthiansapp\MainActivity.kt', 'r', encoding='utf-8') as f:
    text = f.read()

photos = {
  "Matheus Donelli": "https://upload.wikimedia.org/wikipedia/commons/c/cc/S%C3%A9rie_A1_Bragantino_1x0_Corinthians_%2852633088383%29_-_Matheus_Donelli.jpg",
  "Fagner": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Paulist%C3%A3o_A1_-_S%C3%A3o_Bernardo_2x0_Corinthians_%2852681299548%29.jpg",
  "Matheus Bidu": "https://upload.wikimedia.org/wikipedia/commons/3/34/Matheus_Bidu_2025.jpg",
  "André Ramalho": "https://upload.wikimedia.org/wikipedia/commons/c/cb/FC_Admira_Wacker_M%C3%B6dling_vs._FC_Red_Bull_Salzburg_2018-04-15_%28058%29.jpg",
  "Raniele": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Raniele_2026.jpg",
  "Charles": "https://upload.wikimedia.org/wikipedia/commons/1/12/CharlesInter2017.jpg",
  "Breno Bidon": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Breno-de-souza-bidon-no-corinthians_y_corinthians_%28cropped%29.jpg",
  "Rodrigo Garro": "https://upload.wikimedia.org/wikipedia/commons/6/67/Rodrigo_Garro_2025.jpg",
  "Igor Coronado": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Coronado_in_the_Al-Ittihad_club_match.jpg",
  "Yuri Alberto": "https://upload.wikimedia.org/wikipedia/commons/8/89/Brasileir%C3%A3o_2022_Corinthians_2x0_Cuiab%C3%A1_%2852661306474%29_%28cropped%29.jpg",
  "Memphis Depay": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Memphis_Depay_2019.jpg",
  "Ángel Romero": "https://upload.wikimedia.org/wikipedia/commons/1/12/%C3%81ngel_Romero_-_Sulamericana_CUP_2023_Semifinal_-_Corinthians_x_Fortaleza-CE_%2853554974439%29_%28cropped%29.jpg",
  "Talles Magno": "https://upload.wikimedia.org/wikipedia/commons/6/61/CINvNYC_2022-06-29_-_Maxime_Chanot%2C_Tayvon_Gray%2C_Talles_Magno%2C_Gabriel_Pereira%2C_Maxi_Moralez_%2852187858080%29_%28Magno_crop%29.jpg",
  "Pedro Henrique": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Pedro_Henrique_A_Kayserispor_2020.jpg",
  "Hugo Souza": "https://upload.wikimedia.org/wikipedia/commons/0/07/Hugo_Souza_%28cropped%29.jpg",
  "Hugo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Hugo%2C_o_novo_refor%C3%A7o_do_Goi%C3%A1s._%28cropped%29.jpg/640px-Hugo%2C_o_novo_refor%C3%A7o_do_Goi%C3%A1s._%28cropped%29.jpg",
  "Félix Torres": "https://upload.wikimedia.org/wikipedia/commons/8/89/Felix_Torres_em_a%C3%A7%C3%A3o_pela_sele%C3%A7%C3%A3o_equatoriana_em_2021.png",
  "Gustavo Henrique": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Gustavo_Henrique_Vernandes_-_Flamengo_%2851494576856%29.jpg/640px-Gustavo_Henrique_Vernandes_-_Flamengo_%2851494576856%29.jpg",
  "Cacá": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Caca_em_a%C3%A7%C3%A3o_pelo_Cruzeiro_em_2020.jpg/640px-Caca_em_a%C3%A7%C3%A3o_pelo_Cruzeiro_em_2020.jpg",
  "José Martínez": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Jose_Martinez_Philly.jpg/640px-Jose_Martinez_Philly.jpg",
  "Alex Santana": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Alex_Santana_em_a%C3%A7%C3%A3o_pelo_Botafogo.jpg/640px-Alex_Santana_em_a%C3%A7%C3%A3o_pelo_Botafogo.jpg",
  "Matheuzinho": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Matheuzinho_Corinthians_%28cropped%29.jpg/640px-Matheuzinho_Corinthians_%28cropped%29.jpg"
}

def replace_fn(match):
    name = match.group(1)
    rest = match.group(2)
    old_url = match.group(3)
    if name in photos:
        return f'Player("{name}"{rest}, "{photos[name]}")'
    return match.group(0)

new_text = re.sub(r'Player\("([^"]+)"(.*?), "(https://ui-avatars.com[^"]+)"\)', replace_fn, text)

with open(r'app\src\main\java\com\a15032\vaicorinthiansapp\MainActivity.kt', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replacement complete.")
