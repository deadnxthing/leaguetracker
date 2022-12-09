from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from apikey import api_key
import functions
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def nickname():
    #print("Nick: %s" %(entry_1.get()))
    nick = entry_1.get()
    if nick == '':
        print('nie podano zadnej nazwy')
    name = str(nick.replace(' ', '%20'))
    try:
        functions.puuid(name=name)
    except:
        print('❌Taki gracz nie istnieje❌')
        sys.exit()
    print(f'=======\nObecna ranga\n=======')
    functions.rank(name=name)
    print(f'=======\nStatystyki z ostatniej gry\n=======')
    functions.champion(name=name)
    functions.kda(name=name)
    functions.CS(name=name)
    functions.gold(name=name)
    functions.visionscore(name=name)
    functions.damage(name=name)
    print(f'=======\nStatystyki twojej Maestri\n=======')   
    functions.maestria(name=name)


window = Tk()

window.geometry("1000x750")
window.configure(bg = "#FFFFFF")


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
