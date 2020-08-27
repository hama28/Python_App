import requests
import json
import sqlite3

response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=JP&key= ここにAPIキー &fields=items(snippet(title))')
honbun = response.text
#honbun = json.loads(response.text)

savepath = 'test.json'
with open(savepath, 'w') as f:
    json.dump(honbun, f, ensure_ascii=False)

with open(savepath, 'r') as f:
    date = json.load(f)
    print(date)
