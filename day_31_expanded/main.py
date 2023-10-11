from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# load images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

known_button = PhotoImage(file="images/right.png")
unknown_button_img = PhotoImage(file="images/wrong.png")
french_button_img = PhotoImage(file="images/french_flag.png")
german_button_img = PhotoImage(file="images/german_flag.png")
spanish_button_img = PhotoImage(file="images/spanish_flag.png")
italian_button_img = PhotoImage(file="images/italian_flag.png")




window.mainloop()