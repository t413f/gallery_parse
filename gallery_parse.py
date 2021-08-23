from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#url site: Gallerix.ru
url = "https://gallerix.ru/album/200-Russian/"

#server bypass
ua = UserAgent()

#copy webpage
response = requests.get(url, headers={'User-Agent': ua.chrome})
html = response.content
soup = BeautifulSoup(html, "lxml")

#start parse
print(soup.head.title.text[:46])

#create database with name and picture
all_urls = []

for obj in soup.findAll(attrs={'class': 'pic'}):
    for urls in obj:
        if urls.find(attrs={'class': 'a_dv1'}):
            all_urls.append(urls.attrs['href'])


href_img = []
name_img = []

for url in all_urls:
    response = requests.get("https://gallerix.ru" + url, headers={'User-Agent': ua.chrome})
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    href_img.append(soup.find(attrs={'id': 'xpic'}).attrs['src'])
    name_img.append(soup.find(attrs={'id': 'axpic'}).attrs['title'][:soup.find(attrs={'id': 'axpic'}).attrs['title'].find(".")])



