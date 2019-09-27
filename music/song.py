import sys, requests, os, eyed3
from bs4 import BeautifulSoup

link_list = open("links.txt", "r")

for url in link_list.read().splitlines():
    print(url)
    param_name = "v"

    try:
        video_index = [i.split("=")[-1] for i in url.split("?", 1)[-1].split("&") if i.startswith(param_name + "=")][0]
    except:
        print("No 'v' parameter in the link provided!")
        exit(1)

    cookie = {'__cfduid': 'ddcc04ae7cb0524f32f2d64977609b8a91551979418'}
    request_url = 'https://usualdownloader.com/yt/' + str(video_index) + '?dl=mp3_192&fade-in=&fade-out='

    get_response = requests.get(request_url, cookies=cookie, stream=True)
    file_name = str(video_index) + ".mp3"

    with open("downloaded/" + file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=192):
            if chunk:
                f.write(chunk)

    audio = eyed3.load("downloaded/" + file_name)
    os.rename(str("downloaded/" + file_name), str("downloaded/" + audio.tag.title) + ".mp3")


