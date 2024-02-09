from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("./data/french_words.csv")
words = df.to_dict()

rnd_index = random.randint(0, len(df) - 1)


def unknown_action():
    global rnd_index, words, t, w, window
    rnd_index = random.randint(0, len(df) - 1)
    canvas.delete(t)
    canvas.delete(w)
    t = canvas.create_text(403, 150, text="French", fill="black", font=("Arial", 34, "italic"))
    w = canvas.create_text(403, 270, text=f"{words['French'][rnd_index]}", fill="black", font=("Arial", 50, "bold"))
    canvas.itemconfig(canvas_background, image=front_img)
    window.after(3000, flip_card)


def flip_card():
    global t, w
    canvas.delete(t)
    canvas.delete(w)
    t = canvas.create_text(403, 150, text="English", fill="white", font=("Arial", 34, "italic"))
    w = canvas.create_text(403, 270, text=f"{words['English'][rnd_index]}", fill="white", font=("Arial", 50, "bold"))
    canvas.itemconfig(canvas_background, image=back_img)


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=17)
window.after(3000, flip_card)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=785, height=510, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(403, 270, image=front_img)
t = canvas.create_text(403, 150, text="French", font=("Arial", 34, "italic"))
w = canvas.create_text(403, 270, text=f"{words['French'][rnd_index]}", font=("Arial", 50, "bold"))

canvas.grid(column=1, row=1, columnspan=2)

rt_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

empty_label = Label()
empty_label.config(bg=BACKGROUND_COLOR)
empty_label.grid(column=1, row=2, columnspan=2)

rt_button = Button(image=rt_image, highlightthickness=0, command=unknown_action)
rt_button.config(pady=30, bg=BACKGROUND_COLOR)
rt_button.grid(column=2, row=3)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=unknown_action)
unknown_button.config(pady=30, bg=BACKGROUND_COLOR)
unknown_button.grid(column=1, row=3)

window.mainloop()
