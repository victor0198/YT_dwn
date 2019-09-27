import sys, requests, os, eyed3
from bs4 import BeautifulSoup


cookie = {'__cfduid': 'ddcc04ae7cb0524f32f2d64977609b8a91551979418'}
youtube_dwn = 'https://usualdownloader.com/yt/'
lnk = sys.argv[1]

print(lnk)

html_doc = requests.get(lnk)

soup = BeautifulSoup(html_doc.text, 'html.parser')

playlist = soup.find(id="playlist-autoscroll-list")
list_songs = playlist.find_all("li", attrs={"class":"yt-uix-scroller-scroll-unit"})

for song in list_songs:
    try:
        index = song.find("span", attrs={"class":"index"}).string.replace(" ","").replace("\n","")
    except:
        continue


    print("Index: ", index)

    partial_url = song.find("a", attrs={"class":"playlist-video"})

    video_index = [i.split("=")[-1] for i in partial_url['href'].split("?", 1)[-1].split("&") if i.startswith("v" + "=")][0]











    request_url = youtube_dwn + str(video_index) + '?dl=mp3_192&fade-in=&fade-out='
    print(video_index)
    print(request_url)

    get_response = requests.get(request_url, cookies=cookie, stream=True)
    file_name = str(video_index) + ".mp3"

    with open("D:\Downloaded music/R2/" + file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)

    audio = eyed3.load("D:\Downloaded music/R2/" + file_name)
    try:
        os.rename(str("D:\Downloaded music/R2/" + file_name), str("D:\Downloaded music/R2/" + audio.tag.title) + ".mp3")
        print(audio.tag.title)
    except:
        print("No 'tag' attribute")

