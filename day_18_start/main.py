from turtle import Screen
import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
tim.speed(10)
tim.pensize(1)
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

#Draw a square
#for turtle in range(4):
    #tim.forward(100)
    #tim.right(90)

#Draw a dashed line
#for turtle in range(10):
    #tim.forward(10)
    #tim.penup()
    #tim.forward(5)
    #tim.pendown()


#def draw_shape(num_sides):
    #angle = 360 / num_sides
    #for turtle in range(num_sides):
       # tim.forward(100)
        #tim.right(angle)

#for shape_side_n in range(3, 11):
   # tim.color(random_colour)
    #draw_shape(shape_side_n)

#random walk
#directions = [0, 90, 180, 270]
#for turtle in range(200):
    #tim.forward(30)
    #tim.setheading(random.choice(directions))
    #tim.color(random_colour())

#draw a circle spirograph

def draw_spirograph(size_of_gap):
    for turtle in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_colour())
draw_spirograph(5)









screen = Screen()
screen.exitonclick()