import urllib.request
import urllib.parse
import json

query = urllib.parse.quote("Matheus Donelli")
req = urllib.request.Request(f"https://transfermarkt-api.vercel.app/players/search/{query}", headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req).read().decode('utf-8')
    print(resp)
except Exception as e:
    print(f"Error: {e}")
