from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from apikey import api_key
import functions
import sys
import requests
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def nickname():
    nick = entry_1.get()
    name = str(nick.replace(' ', '%20'))
    if nick == '':
        print('Nie podano zadnej nazwy')
    try:
        url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
        name_api_link = url1 +"?api_key="+api_key
        player_info = requests.get(name_api_link)
        resp1 = player_info.json()
        puuid = resp1['puuid']
        id = resp1['id']
    except:
        print('❌Taki gracz nie istnieje❌')
        sys.exit()
    print(f'=======\nObecna ranga\n=======')
    functions.rank(id=id)
    print(f'=======\nStatystyki z ostatniej gry\n=======')
    functions.champion(puuid=puuid)
    functions.kda(puuid=puuid)
    functions.CS(puuid=puuid)
    functions.gold(puuid=puuid)
    functions.visionscore(puuid=puuid)
    functions.damage(puuid=puuid)
    print(f'=======\nStatystyki twojej Maestri\n=======')   
    functions.maestria(id=id)




window = Tk()

window.geometry("1000x750")
window.configure(bg = "#FFFFFF")
window.iconbitmap(r"leaguetrash\icons\icon.ico")
window.title("League Of Legends Stats Tracker by kuba.#4158")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    375.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    386.0,
    image=image_image_2
)

canvas.create_text(
    290.0,
    258.0,
    anchor="nw",
    text="Swojego Przywoływacza",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    350.0,
    211.0,
    anchor="nw",
    text="Wprowadz nazwe",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    8.0,
    8.0,
    anchor="nw",
    text="Riot API rate limits\n20 requests every 1 seconds(s)\n100 requests every 2 minutes(s)",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    6.0,
    706.0,
    anchor="nw",
    text="v1.0",
    fill="#000000",
    font=("Inter", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    500.5,
    386.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=336.0,
    y=373.0,
    width=329.0,
    height=25.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=nickname
)
button_1.place(
    x=417.0,
    y=474.0,
    width=172.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
