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

z = 0;

for obj in imported_data:

    query = obj["name"]

    s_q = query + " movie"
    service_url = 'https://www.google.com/search?q=' + s_q

    page = requests.get(service_url, timeout=5, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find(class_="zVvuGd MRfBrb")
    if (div == None):
        continue
    div = div.findAll("a")
    names = list({})

    for t in div:
        l = list(t["title"])
        temp = list({})
        for i in range(0,len(l) - 7):
            temp.append(l[i])
        names.append("".join(temp).lower())

    recs = list({})
    recs.append(obj)

    new = list({})
    new.append(obj)

    if (z % 2 == 0):
        for ob in imported_data:
            if ob["name"] in names:
                recs.append(ob)

        j = "RecommendedMoviesPairs/Testing/" + str(int(z/2)) + ".json"
    else:
        for ob in imported_data:
            if ob["name"] in names:
                recs.append(ob)
                j = "RecommendedMoviesPairs/Training/" + str(int(z/2)) + ".json"
                break;

    if recs == new:
        continue

    z = z + 1

    with open(j, 'w') as outfile:
        json.dump(recs, outfile)
