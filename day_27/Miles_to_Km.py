from tkinter import *
FONT = "Arial", 24, "bold"

def button_clicked():
    query = int(miles_input.get())
    answer = str(query * 1.6)
    answer_label.config(text=answer)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

equals_label = Label(text="is equal to", font=(FONT))
equals_label.grid(column=0, row= 1)

miles_label = Label(text="Miles", font=(FONT))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=(FONT))
km_label.grid(column=2, row=1)

answer_label = Label(text="0", font=(FONT))
answer_label.grid(column=1, row=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)




window.mainloop()