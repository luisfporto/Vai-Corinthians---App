import urllib.request
import re
import urllib.parse
try:
    req = urllib.request.Request("https://img.a.transfermarkt.technology/portrait/big/68802.jpg", headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print("Code:", resp.getcode())
except Exception as e:
    print("Big without timestamp:", e)

# Test if we can find TM link from wiki
title = urllib.parse.quote("Fagner (futebolista)")
url = f"https://pt.wikipedia.org/w/api.php?action=parse&page={title}&prop=externallinks&format=json"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read().decode('utf-8')
    links = json.loads(data)['parse']['externallinks']
    for link in links:
        if 'transfermarkt' in link:
            match = re.search(r'jogador/(\d+)', link) or re.search(r'profil/spieler/(\d+)', link)
            if match:
                print("Found ID:", match.group(1))
except Exception as e:
    print("Wiki Parse Error:", e)
