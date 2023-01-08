from tkinter import *
from PIL import ImageTk, Image
import string
import random

root = Tk()
root.title("Я люблю BRAWL STARS")
root.geometry("1200x675")

def clicked():
    exit = ""
    for j in range(3):
        n = 5
        letters = 0
        integers = 0
        for i in range(n):
            if letters < 3 and integers < 2:
                a = random.randint(1,2)
                if a == 1:
                    exit += random.sample(string.ascii_letters, 1)[0]
                    letters += 1
                else:
                    exit+=str(random.randint(0,9))
                    integers += 1
            elif letters < 3:
                exit += random.sample(string.ascii_letters, 1)[0]
            else:
                exit+=str(random.randint(0,9))
        if j == 2:
            break
        exit+='-'
    canvas1.itemconfig(label1_canvas, text=exit.upper())


bg = ImageTk.PhotoImage(Image.open("2D4F4F53-D36C-4213-BB42-CAC30A9DD06D.jpeg"))
canvas1 = Canvas(root, width=1200, height=675)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

btn = Button(root, text="Генерировать ключ", command=clicked)

button1_canvas = canvas1.create_window(950, 550, anchor="nw", window=btn)
label1_canvas = canvas1.create_text(1000, 500, text="Генерация ключа", fill="white",
                                    font=('Arial 25 bold'))

root.mainloop()