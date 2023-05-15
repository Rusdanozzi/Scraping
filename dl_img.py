from bs4 import BeautifulSoup
import requests
from os.path import basename


def downloadImage(imgURL):
    img_name = basename (imgURL)
    with open("images/" + img_name,'wb') as f:
        image = requests.get(imgURL)
        f.write(image.content)
        print("writing",img_name)

def getImageUrl(soup):
    return soup.find('figure',class_="image-overlay").find("img")["src"]

def getSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

if __name__ == "__main__":
    url = "https://www.antaranews.com/berita/3374832/airlangga-tegaskan-surya-paloh-alumni-golkar?utm_source=antaranews&utm_medium=desktop&utm_campaign=terkini"
    soup = getSoup(url)
    imgURL = getImageUrl(soup)
    downloadImage(imgURL)