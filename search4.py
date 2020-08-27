#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = "ここにAPIキー"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q, # 検索したい文字列
    part="id,snippet",
    order='viewCount', # 視聴回数が多い順
    maxResults=options.max_results # 表示する検索結果数
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print("Videos:\n", "\n".join(videos), "\n")
  print("Channels:\n", "\n".join(channels), "\n")
  print("Playlists:\n", "\n".join(playlists), "\n")


if __name__ == "__main__":
  # 検索ワード
  argparser.add_argument("--q", help="Search term", default="東海オンエア")
  # 検索上限
  argparser.add_argument("--max-results", help="Max results", default=20)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))


def getVideoTitle(ch, term_start, term_end, next):
  # チャンネルの指定期間内の動画一覧を取得
  request = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?channelId=" + ch + "&part=id,snippet" + term_start + term_end + "&maxResults=50&key=***your api key***" + next)
  response = request.read()  # 文字列が返ってくる
  data = json.loads(response) #文字列をjson化

  id_list = []
  title_list = []
  for d in data["items"]:
    if "videoId" in d["id"]:
      id_list.append(d["id"]["videoId"])
      title_list.append(d["snippet"]["title"])

  videoid = "&id=" + ','.join(id_list)
  titles = []
  if len(id_list) > 0:
    # 取得した動画の再生数を取得し判定後，タイトルリストに追加
    request = urllib.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics" + videoid + "&fields=items(statistics)&key=***your api key***")
    response = request.read()
    count = 0
    for item in json.loads(response)["items"]:
      if int(item["statistics"]["viewCount"]) > 1000000:  # 任意の再生数を指定
        titles.append(title_list[count])
      count += 1

  if "nextPageToken" in data["items"]:
    npt = data["nextPageToken"]
  else:
    npt = ""

  return [npt, titles]