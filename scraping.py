import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

result = requests.get("https://lolchess.gg/statistics/items")

src = result.content
soup = BeautifulSoup(src, "html.parser")


def transform():
    tr = soup.find_all("tr")
    for item in tr:
        champion_td = item.find_all("td", class_="champion")
        for i in champion_td:
            champion_name = i.find("span").text
            champion_img = i.find("img")["src"]
            champion_list = {"champion": champion_name, "src": champion_img}
            champions.append(champion_list)

        items_td = item.find_all("td", class_="items")
        for i in items_td:
            main_item_img = i.find("div", class_="desc").img["src"]
            ratio = i.find("div", class_="combination").find(
                "span", class_="ratio").text
            main_items_name = i.find("div", class_="combination").find(
                "span", class_="name").text
            items_list = {"item": {"name": main_items_name,
                                   "ratio": ratio, "src": main_item_img}}
            main_items.append(items_list)

    return


champions = []
main_items = []
combined_arr = []

transform()

for slice_arr in (main_items[i:i+5] for i in range(0, len(main_items), 5)):
    combined_arr.append(slice_arr)

zip_result = list(zip_longest(champions, combined_arr))

final_list=[]

champions_file=open("champions.txt","w")
champions_file.write(f"{zip_result}")
champions_file.close()