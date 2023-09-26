from tkinter import *

FONT = "Arial", 21, "bold"


def button_clicked():
    miles = float(miles_input.get())
    kilometer = round(miles * 1.609)
    answer_label.config(text=f"{kilometer}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(column=0, row=1)
equals_label.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

answer_label = Label(text="0", font=FONT)
answer_label.grid(column=1, row=1)
answer_label.config(padx=20, pady=20)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=20, pady=20)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()
