import urllib.request
import json

req = urllib.request.Request("https://api.sofascore.app/api/v1/team/1957/players", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    resp = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(resp)
    photo_map = {}
    for p in data['players']:
        player = p['player']
        name = player['name']
        pid = player['id']
        photo_map[name] = f"https://api.sofascore.app/api/v1/player/{pid}/image"
    print(json.dumps(photo_map, indent=2))
except Exception as e:
    print(e)
