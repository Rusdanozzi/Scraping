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
    return soup.find('div',class_="photo__wrap").find("img")["src"]

def getSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

if __name__ == "__main__":
    url = "https://nasional.kompas.com/read/2023/01/11/12091371/yusril-penerbitan-perppu-cipta-kerja-oleh-jokowi-jauh-memenuhi-alasan"
    soup = getSoup(url)
    imgURL = getImageUrl(soup)
    downloadImage(imgURL)