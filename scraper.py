from bs4 import BeautifulSoup
import requests
import json

page = requests.get("https://www.finder.com/ca/netflix-movies")

soup = BeautifulSoup(page.content, 'html.parser')

moviesList =  soup.find("tbody",{"class": "luna-table__body"})

mov_list = list({})

for mov in moviesList.contents:
    mov_traits = list(())
    traits = mov.children
    name = mov.find('b').contents[0]
    for t in traits:
        mov_traits.append(t.contents[0])
    year_of_release = mov_traits[1]
    runtime = mov_traits[2]
    genres = mov_traits[3]
    mov_list.append({
        'name': name,
        'year_of_release': year_of_release,
        'runtime': runtime,
        'genres': genres})

with open('data.json', 'w') as outfile:
    json.dump(mov_list, outfile)
