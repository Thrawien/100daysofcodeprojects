from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50, )

# load images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

known_button = PhotoImage(file="images/right.png")
unknown_button_img = PhotoImage(file="images/wrong.png")
french_button_img = PhotoImage(file="images/french_flag.png")
german_button_img = PhotoImage(file="images/german_flag.png")
spanish_button_img = PhotoImage(file="images/spanish_flag.png")
italian_button_img = PhotoImage(file="images/italian_flag.png")

# canvas creation
canvas = Canvas(width=900, height=550,background=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(450, 280, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=4)
# TODO align canvas text to center
welcome_text = canvas.create_text(450, 150, width=800,text="Welcome to the language flashcard game.\nChoose a language to begin.", font=("Ariel", 30, "italic"))
welcome_text2 = canvas.create_text(450, 300, width=700,text="You will have three seconds to identify the word before "
                                                            "the translation is revealed. If you know the word select "
                                                            "the tick.\nIf you don't then select the cross.",
                                   font=("Ariel", 22, "italic"))

# button creation

french_button = Button(image=french_button_img, highlightthickness=0)
french_button.grid(column=0, row=1, pady=10)

german_button = Button(image=german_button_img, highlightthickness=0)
german_button.grid(column=1, row=1, pady=10)

italian_button = Button(image=italian_button_img, highlightthickness=0)
italian_button.grid(column=2, row=1, pady=10)

spanish_button = Button(image=spanish_button_img, highlightthickness=0)
spanish_button.grid(column=3, row=1, pady=10)




window.mainloop()