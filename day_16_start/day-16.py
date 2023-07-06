#example of whats happening
#import another_module
#print(another_module.another_variable)

#from turtle import Turtle, Screen
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("DarkOrchid")
#timmy.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)

#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)