import json
import requests

response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=JP&key= ここにAPIキー &fields=items(id,snippet(title),statistics)')
print(response.text)

str = {
    response.text
}

str_test = {
    "東京":{
        "population": 1300,
        "capital": "東京"
    },
    "北海道":{
        "population": 538,
        "capital": "札幌市"
    },
    "沖縄":{
        "population": 143,
        "capital": "那覇市"
    }
}

with open('test.json', 'w') as f:
    json.dump(str, f, ensure_ascii=False, indent=4)