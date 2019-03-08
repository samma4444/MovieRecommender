from bs4 import BeautifulSoup
import requests
import json

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

service_url = "https://www.finder.com/ca/netflix-movies"

page = requests.get(service_url, timeout=5, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

moviesList =  soup.find("tbody",{"class": "luna-table__body"})

mov_list = list({})

for mov in moviesList.contents:
    mov_traits = list(())
    traits = mov.children
    name = list(mov.find('b').contents[0])
    for i in range(len(name)):
        if (name[i] == '#') :
            name[i] = ''
    name = "".join(name).lower()
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
