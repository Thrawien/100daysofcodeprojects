from turtle import Turtle

FONT = ("Arial", 20, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as data:
            # data.read() gives a str, need to convert to int for program to run
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()

    # def game_over(self):
        # self.goto(0,0)
        # self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
