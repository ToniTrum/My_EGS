import sqlite3
import urllib.request
from PIL import Image


con = sqlite3.connect("../Data_bases/GamesList.db")
cur = con.cursor()
result = cur.execute("""SELECT GameID, Title, Image from GamesInfo""").fetchall()

for game in result:
    game_id, name, img_url = game
    if img_url != "None" and img_url:
        name = name.replace(" ", "_").replace(":", "").replace("'", "").replace("´", "")
        name = name.replace('"', "").replace(",", "").replace(".", "").replace("?", "")
        name = name.replace("!", "").replace("/", "_").replace("\\", "_").replace("\t", "")
        name = name.replace("\n", "").replace("\r", "")
        save_path = f"Images/{name}.avif"
        urllib.request.urlretrieve(img_url, "../" + save_path)

        image_avif = Image.open("../" + save_path)
        png_image = save_path.replace(".avif", ".png")
        image_avif.save("../" + png_image, "PNG")
    else:
        png_image = "Images/NoImage.png"

    result = cur.execute("""UPDATE GamesInfo
                            SET Image = ?
                            WHERE GameID = ?""", (png_image, game_id)).fetchall()

    print(game_id, name, png_image)
    con.commit()

con.close()
