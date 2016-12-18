from bs4 import BeautifulSoup

import requests, json, re

songurl = []
lyricdata = []

artistlink = "https://web.archive.org/web/20160501083109/http://www.azlyrics.com/r/rollingstones.html" #examnple: https:/www.azlyrics.com/r/rollingstones.html

linkend = "rollingstones" #example: rollingstones

artistname = "The Rolling Stones" # example: The Rolling Stones

header = { 'User-Agent':'school project'}

page = requests.get(artistlink, headers=header)
page_html = page.text
soup = BeautifulSoup(page_html, "html.parser")
songlist= soup.find_all("a", attrs={"href": re.compile("lyrics/"+linkend)})

for song in songlist:
    songurl.append("https://web.archive.org"+song['href'])

for url in songurl:
    lyricpage = requests.get(url, headers=header)
    lyricpage_html = lyricpage.text
    lyricsoup = BeautifulSoup(lyricpage_html, "html.parser")
    lyricbody = lyricsoup.find("br")
    lyricdict = {artistname :lyricbody.text}
    lyricdata.append(lyricdict)

with open('rollingstone.json', 'w') as file:
    file.write(json.dumps(lyricdata,indent=4))


