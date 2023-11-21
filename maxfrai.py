#pip install requests beautifulsoup4

import requests
import pandas as pd
from bs4 import BeautifulSoup
urlMain = "https://my.mail.ru/music/search/макс%20фрай/pages/6"  # ссылка

#//moosic.my.mail.ru/file/2089a7b9146d91efefd8021e4e8f87d6.mp3
requests.get(urlMain)
MainPages = requests.get(urlMain)
#print(MainPages)
# parser-lxml = Change html to Python friendly format
MainSoup = BeautifulSoup(MainPages.text, "lxml")  # код сайта готовый к обработки
soup = BeautifulSoup(MainPages.text, 'html.parser')
#print(MainSoup)

MainFilteredParsRes = MainSoup.find_all("div", class_="song-item song songs-table")  # отфильтрованный код компаний
#print(MainFilteredParsRes)
print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")



for elem in MainFilteredParsRes:
    ScriptRes = elem.find("script", class_="data-song")
    ScriptText = ScriptRes.text
    print(ScriptText)
    #выдергивание элементов
    UrlIndex = ScriptText.find("//moosic.my.mail.ru")  #ссылка
    UrlEndIndex = ScriptText.find(".mp3")
    TitleIndex = ScriptText.find("urlId\": \"")
    TitleEndIndex = ScriptText.find("name")

    SongLink = ("https:"+ScriptText[UrlIndex:UrlEndIndex+4])
    print (SongLink)
    SongName = (ScriptText[TitleIndex+9:TitleEndIndex -7])
    print(SongName)
    r = requests.get(SongLink)
    with open(SongName+'.mp3', 'wb') as f: f.write(r.content)