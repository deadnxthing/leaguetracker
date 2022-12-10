from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel
from apikey import api_key
from time import sleep
import functions
import sys
import requests
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def error_window(nick):
    window3= Toplevel(window)
    window3.geometry("700x500")
    window3.configure(bg = "#FFFFFF")
    window3.iconbitmap(r"leaguetracker\assets\frame0\icon.ico")
    window3.title(f'Błąd')

    canvas = Canvas(
        window3,
        bg = "#FFFFFF",
        height = 700,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_100 = PhotoImage(
        file=relative_to_assets("image_100.png"))
    image_100 = canvas.create_image(
        600.0,
        350.0,
        image=image_image_100
    )

    canvas.create_text(
        138.0,
        164.0,
        anchor="nw",
        text=f"Taki gracz jak {nick} nie istnieje!\nUpewnij się co do poprawności wpisanej nazwy",
        fill="#ff0000",
        font=("Inter", 20 * -1)
    ) 


    window3.resizable(False, False)
    window3.mainloop()




def nickname():
    nick = entry_1.get()
    name = str(nick.replace(' ', '%20'))
    try:
        url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
        name_api_link =(url1+"?api_key="+api_key)
        player_info = requests.get(name_api_link)
        resp1 = player_info.json()
        puuid = resp1['puuid']
        id = resp1['id']
        resp=functions.lastmatchinfo(puuid=puuid)
        last_match=functions.last_match(resp=resp[0],user_index=resp[1])
        resp2=functions.rankinfo(id=id)
        rank=functions.rank(rank=resp2)
        maestria=functions.maestria(id=id)

        open_new_window(
            nick=nick,
            kda=last_match[0],
            champion=last_match[1],
            visionscore=last_match[2],
            goldearned=last_match[3],
            goldpermin=last_match[4],
            dmgtochmp=last_match[5],
            trdmgtochamp=last_match[6],
            healing=last_match[8],
            tkndmg=last_match[7],
            cs=last_match[9],
            division=str.capitalize(rank[0]),
            tier=rank[1],
            lp=rank[2],
            wr=rank[3],
            maestriachmpname=maestria[0],
            maestriachmpid=maestria[1],
            level=maestria[2],
            punkty=maestria[3],
            )
    except:
        print(
            '❌Taki gracz nie istnieje❌'
            )
        error_window(nick=nick)



def open_new_window(nick,kda,champion,visionscore,goldearned,goldpermin,dmgtochmp,trdmgtochamp,healing,tkndmg,cs,division,tier,lp,wr,maestriachmpname,maestriachmpid,level,punkty):
    window2= Toplevel(window)
    window2.geometry("1200x700")
    window2.configure(bg = "#FFFFFF")
    window2.iconbitmap(r"leaguetracker\assets\frame0\icon.ico")
    window2.title(f'Statystyki Przywoływacza {nick}')

    canvas = Canvas(
        window2,
        bg = "#FFFFFF",
        height = 700,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_100 = PhotoImage(
        file=relative_to_assets("image_100.png"))
    image_100 = canvas.create_image(
        600.0,
        350.0,
        image=image_image_100
    )

    image_image_200 = PhotoImage(
        file=relative_to_assets("image_200.png"))
    image_200 = canvas.create_image(
        338.0,
        491.0,
        image=image_image_200
    )

    canvas.create_text(
        238.0,
        264.0,
        anchor="nw",
        text="Ostatni Mecz",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    canvas.create_text(
        975.0,
        160.0,
        anchor="nw",
        text="Maestria",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    canvas.create_rectangle(
        966.0,
        246.0,
        1116.0,
        396.0,
        fill="#404040",
        outline="")

    image_image_300 = PhotoImage(
        file=relative_to_assets(f"{str.lower(division)}.png"))   #ranga
    image_300 = canvas.create_image(
        698.0,
        392.0,
        image=image_image_300
    )

    image_image_400 = PhotoImage(
        file=relative_to_assets("image_400.png"))
    image_400 = canvas.create_image(
        1046.0,
        430.0,
        image=image_image_400
    )

    image_image_500 = PhotoImage(
        file=relative_to_assets(f"{maestriachmpid}.png"))   #obrazek czempiona
    image_500 = canvas.create_image(
        1041.0,
        321.0,
        image=image_image_500
    )

    image_image_600 = PhotoImage(
        file=relative_to_assets("image_600.png"))
    image_600 = canvas.create_image(
        1025.0,
        237.0,
        image=image_image_600
    )

    image_image_700 = PhotoImage(
        file=relative_to_assets("image_700.png"))
    image_700 = canvas.create_image(
        1045.0,
        571.0,
        image=image_image_700
    )

    canvas.create_text(
        648.0,
        264.0,
        anchor="nw",
        text="Ranga",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    image_image_800 = PhotoImage(
        file=relative_to_assets("image_800.png"))
    image_800 = canvas.create_image(
        703.0,
        512.0,
        image=image_image_800
    )

    image_image_900 = PhotoImage(
        file=relative_to_assets("image_900.png"))
    image_900 = canvas.create_image(
        703.0,
        589.0,
        image=image_image_900
    )

    canvas.create_text(
        422.0,
        45.0,
        anchor="nw",
        text="Statystyki Przywoływacza",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    image_image_1000 = PhotoImage(
        file=relative_to_assets("image_1000.png"))
    image_1000 = canvas.create_image(
        600.0,
        123.0,
        image=image_image_1000
    )
    #Nazwa przywolywacza

    canvas.create_text(
        500.0,
        108.0,
        anchor="nw",
        text=nick,
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    #Ostatni mecz
    canvas.create_text(
        220.0,
        320.0,
        anchor="nw",
        text=(f'Czempion: {champion}\nKDA {kda}\nCS {cs}\nPunkty wizji: {visionscore}\nZdobyte Złoto: {goldearned}\nZłoto na minutę: {goldpermin}'),
        fill="#000000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        220.0,
        470.0,
        anchor="nw",
        text=(f'Zadane Obrażenia: \n{dmgtochmp}\nNieuchronne obrażenia: \n{trdmgtochamp}\nOtrzymane Obrażenia: \n{tkndmg}\nLeczenie: \n{healing}'),
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    #ranga

    canvas.create_text(
        630.0,
        500.0,
        anchor="nw",
        text=(f'{division} {tier} {lp}'),
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    canvas.create_text(
        592.0,
        575.0,
        anchor="nw",
        text=(f'{wr}'),
        fill="#000000",
        font=("Inter", 18 * -1)
    )
    #maestria
    canvas.create_text(
        1000.0,
        415.0,
        anchor="nw",
        text=(f'{maestriachmpname}'),
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    canvas.create_text(
        950.0,
        485.0,
        anchor="nw",
        text=(f'Poziom Maestri:\n            {level}'),
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    canvas.create_text(
        950.0,
        580.0,
        anchor="nw",
        text=(f'Ilośc Punktów:\n      {punkty}'),
        fill="#000000",
        font=("Inter", 28 * -1)
    )
    
    window2.resizable(False, False)
    window2.mainloop()


window = Tk()

window.geometry("1000x750")
window.configure(bg = "#FFFFFF")
window.iconbitmap(r"leaguetracker\assets\frame0\icon.ico")
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
