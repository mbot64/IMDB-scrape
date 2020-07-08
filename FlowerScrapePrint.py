import requests
from bs4 import BeautifulSoup

URL = "https://www.teleflora.com/floral-facts/glossary-of-flowers?promotion=JULYWELCOME5"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

flowers = soup.find_all("a", class_="flower-meaning-anchor")


for flower in flowers:
    print(flower.text)
#
# import selenium
# from selenium import webdriver
# import time
#
#
# URL = "https://www.imdb.com/search/title/?genres=animation&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=fd0c0dd4-de47-4168-baa8-239e02fd9ee7&pf_rd_r=JG00WHB6TRAK7T2ZTCHE&pf_rd_s=center-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr4_i_1"
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
# movies = soup.find_all("a", href="lister-item-year tex-muted unbold")
#
#
# for movie in movies:
#     print(movie.text)
