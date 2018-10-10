from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの取得
key = "f9495dcf2c01a80e55b6c9b50e538186"
secret = "7d60c8357cf7fe1d"

wait_time = 1

#保存フォルダの指名
animalname = sys.argv[1]
savedir = "./" + animalname

flickrapi = FlickrAPI(key, secret, format='parsed-json')
result = flickrapi.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence',
)

photos = result['photos']
#返り値を取得する
pprint(photos)

for i, photo in enumerate(photos['photo']):
    #url_q = photo['url_q'] #url_qがない場合があるので例外処理に変える
    try:
        url_q = photo["url_q"]
    except:
        continue
    filepath = savedir + "/" + photo['id'] + ".jpg"
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
