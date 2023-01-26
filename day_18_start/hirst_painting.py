#import colorgram
from turtle import Screen
import turtle as turtle_module
import random


#rgb_colors = []
#colors = colorgram.extract("index.jpg", 20)
#print(colors)
#for color in colors:
   # r = color.rgb.r
    #g = color.rgb.g
   # b = color.rgb.b
   # new_color = (r, g, b)
   # rgb_colors.append(new_color)

#print(rgb_colors)

colour_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164)]
tim = turtle_module.Turtle()
tim.speed(10)
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = Screen()
screen.exitonclick()