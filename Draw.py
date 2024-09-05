
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk


def Draw(): 
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/eddyzheng/Documents/Python Projects/CycleTracker/assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("713x745")
    window.configure(bg = "#000000")

    canvas = Canvas(
        window,
        bg = "#000000",
        height = 745,
        width = 713,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        356.0,
        372.0,
        image=canvas.image_1
    )

    canvas.image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        361.0,
        45.0,
        image=canvas.image_2
    )

    canvas.image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        356.0,
        187.0,
        image=canvas.image_3
    )

    canvas.image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        361.0,
        552.0,
        image=canvas.image_4
    )

    canvas.image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        361.0,
        355.0,
        image=canvas.image_5
    )

    canvas.image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        112.0,
        407.0,
        image=canvas.image_6
    )

    canvas.image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        124.0,
        290.0,
        image=canvas.image_7
    )

    canvas.create_text(
        217.0,
        73.0,
        anchor="nw",
        text="Status: ",
        fill="#E6E0E9",
        font=("Roboto", 14 * -1)
    )

    canvas.image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        379.0,
        288.0,
        image=canvas.image_8
    )

    canvas.image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        361.0,
        652.0,
        image=canvas.image_9
    )

    canvas.image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        361.0,
        70.0,
        image=canvas.image_10
    )

    canvas.image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        356.0,
        155.0,
        image=canvas.image_11
    )


    canvas.image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        356.0,
        520.0,
        image=canvas.image_12
    )

    canvas.elixir = ImageTk.PhotoImage(Image.open(relative_to_assets("elixir.jpg")).resize((459, 24)))
    elixir = canvas.create_image(
        356.0,
        123.0,
        image=canvas.elixir
    )

    image_cards = [None, None, None, None, None, None, None, None]
    cards = [None, None, None, None, None, None, None, None]
    cardPositions = [220, 324.3, 428.6, 533]

    for i in range(0, 4):
        image_cards[i] = ImageTk.PhotoImage(Image.open(relative_to_assets("unknown.jpg")).resize((88, 109)))
        cards[i] = canvas.create_image(
            cardPositions[3-i],
            283.0,
            image=image_cards[i]
        )

    for i in range(0, 4):
        image_cards[i+4] = ImageTk.PhotoImage(Image.open(relative_to_assets("unknown.jpg")).resize((88, 109)))
        cards[i+4] = canvas.create_image(
            cardPositions[i],
            420.0,
            image=image_cards[i+4]
        )

    window.resizable(False, False)
    window.title("ClashTool")
    def update(cycle):
        for i in range(0, 8):
            image_cards[i] = ImageTk.PhotoImage(Image.open(relative_to_assets(cycle[i]+".jpg")).resize((88, 109)))
            canvas.itemconfigure(cards[i], image=image_cards[i])
            canvas.elixir = ImageTk.PhotoImage(Image.open(relative_to_assets("elixir.jpg")).resize((459, 24)))
            canvas.itemconfigure(elixir, image=canvas.elixir)

        window.update()
    
    return update
    
