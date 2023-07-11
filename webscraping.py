from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

data = requests.get(start_url)
soup = BeautifulSoup(data.text, "html.parser")

star_data_list = []
name = []
distance = []
mass = []
radius = []

heading = ["Star Name", "Distance", "Mass", "Radius"]
for tr_tags in soup.find("table").find("tbody").find_all("tr"):
    td_tags = tr_tags.find_all("td")
    row = []
    for i in td_tags:
        i = i.text.strip()
        row.append(i)

    star_data_list.append(row)
    
#print(star_data_list)

for i in range(1, len(star_data_list)):
    name.append(star_data_list[i][1])
    distance.append(star_data_list[i][3])
    mass.append(star_data_list[i][5]),
    radius.append(star_data_list[i][6])

# print(name)
# print(distance)
# print(mass)
# print(radius)

print("Writing file")
time.sleep(2)

star_data = {"Star Name": name, "Distance": distance, "Mass": mass, "Radius": radius}
df = pd.DataFrame(star_data)
df.to_csv("star_data.csv", index=True, index_label="id")