import requests
import json
import urllib
from bs4 import BeautifulSoup

response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=JP&key= ここにAPIキー ', 'r')
#print(response.status_code)
#print(response.text)

date = json.load(response)
print(date)