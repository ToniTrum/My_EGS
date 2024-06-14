import requests
import sqlite3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36'
}

con = sqlite3.connect("../Data_bases/GamesList.db")
cur = con.cursor()
result = cur.execute("SELECT GameID, Link from GamesInfo").fetchall()
con.close()

for game in result:
    game_id, url = game

    response = requests.get(url, headers=headers)
    while not response.ok:
        response = requests.get(url, headers=headers)

    with open(f'HTML_pages/{game_id}.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(game_id, url)
