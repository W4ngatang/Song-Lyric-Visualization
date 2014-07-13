from bs4 import BeautifulSoup
from bs4 import Tag
from urllib2 import urlopen
from time import sleep

BASE_URL = "http://www.billboard.com/charts/hot-100?page="

def get_songs(page_number):
    html = urlopen(BASE_URL + page_number).read()
    soup = BeautifulSoup(html, "lxml")
    songs = soup.findAll('h1')
    list_section = []
    for i in range(1,11): # kind of cheating, need to figure out how to filter out anchor tags (links on bottom of page)
        songz = songs[i].encode_contents().strip()
        list_section.append(songz)
    return list_section

if __name__ == '__main__':
    data = [] # a list to store the songs

    for i in range(10):
        songs = get_songs(str(i))
        data += songs
        sleep(1)
    
    print data
