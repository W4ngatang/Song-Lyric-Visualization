from bs4 import BeautifulSoup
from bs4 import Tag
from urllib2 import urlopen
from time import sleep

BASE_URL = "http://www.billboard.com/charts/hot-100?page="

def get_songs(page_number):
    html = urlopen(BASE_URL + page_number).read()
    soup = BeautifulSoup(html, "lxml")
    songs = soup.findAll('h1')
    print songs
    for i in range(len(songs)):
        print songs[i]
        return songs[i]

if __name__ == '__main__':
    data = [] # a list to store the songs

    for i in range(10):
        song = get_songs(str(i))
        data.append(song)
        sleep(1)
    
    print data
