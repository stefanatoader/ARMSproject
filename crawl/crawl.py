import requests
from bs4 import BeautifulSoup

URLS = ["https://www.thetoptens.com/metal-songs",
        "https://www.thetoptens.com/best-alternative-songs",
        "https://www.thetoptens.com/rap-songs",
        "https://www.thetoptens.com/best-pop-songs",
        "https://www.thetoptens.com/greatest-punk-songs"]


def scrape_billboard(data):
    x = []
    i = 0
    soup = BeautifulSoup(data, 'lxml')
    for div in soup.find_all("div", {"class": "chart-row__main-display"}):
        key = div.find_all("h2", {"class": "chart-row__song"})[0].get_text()
        value = ""
        if len(div.find_all("a", {"class": "chart-row__artist"})) > 0:
            value = div.find_all("a", {"class": "chart-row__artist"})[0].get_text()
        elif len(div.find_all("span", {"class": "chart-row__artist"})):
            value = div.find_all("span", {"class": "chart-row__artist"})[0].get_text()
        key.replace("\\n", "")
        value = value.strip('\n')
        x.insert(i, {key: value})
        i += 1
    print(x, file=open("billboard.txt", "a"))


def scrape_songs(urls):
    for url in urls:
        print(url)
        soup = BeautifulSoup(requests.get(url).content, 'lxml')
        file_name = "results/" + url.split('/')[-1] + ".txt"
        for element in soup.find_all("div", {"class": "i"}):
            print(element.find("b").get_text(), file=open(file_name, "a"))


scrape_songs(URLS)

# urlToCrawl = 'https://www.billboard.com/charts/hot-100'
# response = urllib.request.urlopen(URLS[0]).read()
# print(response.decode("utf-8"))
# scrape_billboard(response.decode("utf-8"))
