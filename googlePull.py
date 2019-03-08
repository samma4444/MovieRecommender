from bs4 import BeautifulSoup
import requests
import json

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

imported_data = list({})

with open("data.json", "r") as read_file:
    for obj in json.load(read_file):
        imported_data.append(obj)

query = imported_data[0]["name"]
service_url = 'https://www.google.com/search?q=' + query

page = requests.get(service_url, timeout=5, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

div = soup.find(class_="zVvuGd MRfBrb")
div = div.find_all("a")
names = list({})

for t in div:
    l = list(t["title"])
    temp = list({})
    for i in range(0,len(l) - 7):
        temp.append(l[i])
    names.append("".join(temp).lower())

print(names)

recs = list({})

for obj in imported_data:
    if obj["name"] in names:
        recs.append(obj)
j = query + ".json"

print(j)

with open(j, 'w') as outfile:
    json.dump(recs, outfile)
