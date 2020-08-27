from apiclient.discovery import build
import sqlite3
from contextlib import closing

dbname = 'database.db'

YOUTUBE_API_KEY = ここにAPIキー

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    chart='mostPopular',
    maxResult=10,
    regionCode=JP,
    fileds=items(id,snippet(title),statistics)
    ).execute()
