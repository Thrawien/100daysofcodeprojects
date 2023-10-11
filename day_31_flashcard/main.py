from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)

def is_known():
    to_learn.remove(current_card)
    data =pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcard Game")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=900, height=550,background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(450, 280, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(450, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(450, 300, text="Word", font=("Ariel", 60, "bold"))

# buttons
known_button = PhotoImage(file="images/right.png")
unknown_button_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=known_button, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()