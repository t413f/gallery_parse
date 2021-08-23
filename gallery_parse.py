from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#Url site: Gallerix
url = "https://gallerix.ru/album/200-Russian/"

ua = UserAgent()

print(ua.chrome)

response = requests.get(url, headers={'User-Agent':ua.chrome})

