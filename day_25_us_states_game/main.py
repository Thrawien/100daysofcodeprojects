import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()

#check if guess is among the 50 states
data = pandas.read_csv("50_states.csv")

#write the correct guesses onto the map

#use a loop to allow the user to keep guessing

#record the guesses in a list

#keep track of the score

turtle.mainloop()