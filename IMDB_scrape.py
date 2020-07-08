#Create a CSV file with the rank, name, length, genre(s), and rating.

import requests
from bs4 import BeautifulSoup
import csv
import re

name = ""
rank = ""
length = ""
genre = ""
rating = ""

URL = "https://www.imdb.com/search/title/?genres=animation&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=fd0c0dd4-de47-4168-baa8-239e02fd9ee7&pf_rd_r=JG00WHB6TRAK7T2ZTCHE&pf_rd_s=center-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr4_i_1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

fields = ['name', 'rank', 'length', 'genre', 'rating']


filename = "IMDB_CSV.csv"
csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(fields)


movies = soup.find_all(class_="lister-item-content")
#ranking = soup.find_all(class_="lister-item-index unbold text-primary")
#titles = soup.find_all("a", href="/title/tt0417299/?ref_=adv_li_tt")
# <span class="lister-item-index unbold text-primary">1.</span>
#<a href="/title/tt0417299/?ref_=adv_li_tt">Avatar: The Last Airbender</a>

# rank, name, length, genre(s), and rating

for movie in movies:
    name = movie.h3.a.text
    rank = movie.find(class_="lister-item-index unbold text-primary")
    #name = movie.find(class_="lister-item-index unbold text-primary")
    length = movie.find(class_="runtime")
    if length is None:
        length = ""
    else:
        length = length.text
    genre = movie.find(class_="genre")
    genre = re.sub("[^a-zA-Z- ]+", "", genre.text.rstrip())
    rating = movie.find(class_="certificate")
    if rating is None:
        rating = ""
    else:
        rating = rating.text
    row = [rank.text, name, length, genre, rating]
    #for things in things_to_find:
    print(row)
    csv_writer.writerow(row)
