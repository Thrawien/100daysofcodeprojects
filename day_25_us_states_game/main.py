import turtle, pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another State's name?").title()

    #check if guess is among the 50 states
    data = pandas.read_csv("50_states.csv")
    state_list = data["state"].to_list()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        # write the correct guesses onto the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # pull out the row where the state is equal to the answer state
        state_data = data[data.state == answer_state]
        #tap into the data attributes using the names of the columns, in this case x and y
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)