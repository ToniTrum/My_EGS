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
    print(response.ok)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
pagination = soup.find("ul", class_="css-dr37qy").find_all("li", class_="css-12lid1g")
max_pagination = int(pagination[-2].text)

con = sqlite3.connect("../Data_bases/GamesList.db")
cur = con.cursor()

gameID = 1
for page in range(max_pagination):
    url = f"https://store.epicgames.com/ru/browse?sortBy=relevancy&sortDir=DESC&category=Game&count=40&start={page *40}"
    game_list = None
    while not game_list:
        response = requests.get(url=url, headers=headers)
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

        response = requests.get(url=game_link, headers=headers)
        while not response.ok:
            response = requests.get(url=game_link, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        try:
            price = soup.find("div", class_="css-169q7x3").find("span", class_="css-119zqif").text
        except AttributeError:
            try:
                price = soup.find("div", class_="css-169q7x3").find("span", class_="css-l4hmav").text
            except AttributeError:
                try:
                    table = soup.find("div", class_="css-1gmuxco").find("div", class_="css-j7qwjs").find_all("div", class_="css-15fg505")[-2]
                    row = table.find_all("div", class_="css-10mlqmn")[-2]
                    price = "Будет доступно " + row.find("span", class_="css-119zqif").text
                except IndexError:
                    try:
                        table = soup.find("div", class_="css-1gmuxco").find("div", class_="css-j7qwjs").find_all("div", class_="css-15fg505")[-1]
                        row = table.find_all("div", class_="css-10mlqmn")[-2]
                        price = "Будет доступно " + row.find("span", class_="css-119zqif").text
                    except AttributeError:
                        price = "Скоро"
                except AttributeError:
                    price = "Скоро"

        try:
            genre_list = soup.find("div", class_="css-saiooq").find("div", class_="css-1kg0r30").find_all("span", class_="css-119zqif")
        except AttributeError:
            genre_list = soup.find("div", class_="css-3r3brs").find("div", class_="css-11fxqgy").find_all("span", class_="css-l4hmav")
        genres = [i.text for i in genre_list]

        print(page + 1, gameID, title, price, image, game_link)
        print(genres)
        result_for_game_info = cur.execute("""INSERT INTO Games(GameID, Title, Price, Image, Link)
                                              VALUES(?, ?, ?, ?, ?) """,
                                           (gameID, title, price, image, game_link)).fetchall()
        for genre in genres:
            genreID = cur.execute(f"""SELECT GenreID from Genres
                                      WHERE GenreName = '{genre}'""").fetchone()
            if genreID:
                result_for_genre = cur.execute("""INSERT INTO GenresForGame(GameID, GenreID)
                                                  VALUES(?, ?) """,
                                               (gameID, genreID[0])).fetchall()
        con.commit()
        gameID += 1
        c += 1

con.close()
