import requests
import shutil
from random import randrange
import os

API_KEY="<API KEY HERE>"
BASE_URL="https://api.pexels.com"
per_page=90
queries=("ocean", "nature")
orientation="landscape"
size="large"

def download_file(url):
    url_array = url.split('.')
    extension = url_array[len(url_array)-1]
    local_filename = url_array[-1]

    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    os.rename(local_filename, f"new_wallpaper.{extension}")
    abs_path = os.path.abspath(f"new_wallpaper.{extension}")

    os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri {abs_path}")
    return local_filename

def fetch_random_wallpaper():
    index = randrange(per_page)

    response = requests.get(f"{BASE_URL}/v1/search?query={queries[1]}&per_page={per_page}&size={size}&orientation={orientation}",
    headers={
        "Authorization": API_KEY
    })

    if response.status_code == 200:
        response_json = response.json()
        photo_url = response_json["photos"][index]["src"]["original"]
        download_file(photo_url)
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

fetch_random_wallpaper()