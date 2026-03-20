import urllib.request
import urllib.parse
import json

query = urllib.parse.quote("Matheus Donelli")
req = urllib.request.Request(f"https://www.transfermarkt.com.br/schnellsuche/ergebnis/schnellsuche?query={query}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
try:
    resp = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(resp)
    print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Error: {e}")
