from bs4 import BeautifulSoup
import requests
import os
from fake_useragent import UserAgent

#url site
urlsite = str(os.environ["URLSITES"])

#server bypass
ua = UserAgent()

#copy webpage
response = requests.get(urlsite, headers={'User-Agent': ua.chrome})
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

for urlsite in all_urls:
    response = requests.get(str(os.environ["MAINSITE"]) + urlsite, headers={'User-Agent': ua.chrome})
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    href_img.append(soup.find(attrs={'id': 'xpic'}).attrs['src'])
    name_img.append(soup.find(attrs={'id': 'axpic'}).attrs['title'][:soup.find(attrs={'id': 'axpic'}).attrs['title'].find(".")])


#download all pic
for id, urls in enumerate(href_img):
    resource = requests.get(urls, headers={'User-Agent': ua.chrome})
    out = open("D:/gallery/images/" + str(name_img[id]) + ".jpg", "wb")
    out.write(resource.content)
    out.close()

