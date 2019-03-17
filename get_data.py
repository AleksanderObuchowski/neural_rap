from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib
from tqdm import tqdm 

alphabet = "TUVWXYZ"
lyrics_file = "rap_lyrics.txt"


url = "http://www.tekstyhh.pl/index.php/Abradab/Chobcy.html"
url2 = "http://www.tekstyhh.pl/index.php/Table/A/" 


def get_lyrics(url):
    with open(lyrics_file,"a") as file:
        page =urllib.request.urlopen(url)

        #page = requests.get("http://www.tekstyhh.pl/index.php/Abradab/Chobcy.html")
        soup = BeautifulSoup(page,'html.parser')
        text =soup.select(".contentpaneopen")[1].select("tr")[0].select("td")[1].get_text()

        file.write(text.replace("(adsbygoogle = window.adsbygoogle || []).push({});",""))

for l in alphabet:
    print("Checkign letter: ", l)
    page = urllib.request.urlopen("http://www.tekstyhh.pl/index.php/Table/"+l+"/")
    soup = BeautifulSoup(page,'html.parser')
    links = soup.select(".category")
    for link in links:
        try:
            print("Checking artist:",link["href"])

            artist_url = links[0]["href"]

            artist_page = urllib.request.urlopen(artist_url)

            artist_soup = BeautifulSoup(artist_page,"html.parser")

            song_links_1 = artist_soup.select(".sectiontableentry1")
            for s_link in tqdm(song_links_1):
                get_lyrics(s_link.select("a")[0]['href']) 

            song_links_2 = artist_soup.select(".sectiontableentry2")
            for s_link in tqdm(song_links_2):
                get_lyrics(s_link.select("a")[0]['href'])  
        except:
            pass


