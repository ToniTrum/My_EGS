import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://store.epicgames.com/ru/browse?sortBy=relevancy&sortDir=DESC&category=Game&count=40&start=0"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36'
}

response = requests.get(url, headers=headers)

while not response.ok:
    response = requests.get(url, headers=headers)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
pagination = soup.find("ul", class_="css-dr37qy").find_all("li", class_="css-12lid1g")
max_pagination = int(pagination[-2].text)

for page in range(max_pagination):
    game_list = None
    while not game_list:
        url = f"https://store.epicgames.com/ru/browse?sortBy=relevancy&sortDir=DESC&category=Game&count=40&start={page * 40}"
        response = requests.get(
            url=url,
            headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        game_list = soup.find_all("li", class_="css-lrwy1y")
    c = 1
    for game in game_list:
        if game == game_list[0] and c > 1:
            break
        game = game.find("a", class_="css-g3jcms")
        game_link = "https://store.epicgames.com" + game.get("href")
        try:
            image = game.find("div", class_="css-uwwqev").find("img", class_="css-b664ty").get("data-image")
        except AttributeError:
            image = None
        title = game.find("span", class_="css-119zqif").text

        try:
            price = game.find('span', class_="css-d3i3lr").text
        except AttributeError:
            try:
                price = game.find("div", class_="css-u4p24i").find("span", class_="css-119zqif").text
            except AttributeError:
                response = requests.get(url=game_link, headers=headers)
                while not response.ok:
                    response = requests.get(url=game_link, headers=headers)
                    soup = BeautifulSoup(response.text, 'lxml')
                try:
                    price = soup.find("div", class_="css-169q7x3").find("span", class_="css-119zqif").text
                except AttributeError:
                    try:
                        table = soup.find("div", class_="css-j7qwjs").find("div", class_="css-1ofqig9").find_all("div", class_="css-10mlqmn")
                        for row in table:
                            if row.find("span", class_="css-d3i3lr").text == "Доступность":
                                price = row.find("span", class_="css-119zqif").text
                                break
                    except AttributeError:
                        price = "Скоро"

        con = sqlite3.connect("../Data_bases/GamesList.db")
        cur = con.cursor()
        print(page + 1, c, title, price, image, game_link)
        result = cur.execute("""INSERT INTO game_info(Title, Price, Image, Link)
                                VALUES(?, ?, ?, ?) """, (title, price, image, game_link)).fetchall()
        con.commit()
        con.close()

        c += 1
