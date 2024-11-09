from turtle import Turtle

class Label(Turtle):

    def __init__(self):
        super().__init__()
        self.guesses = []
        self.penup()
        self.hideturtle()
        # self.goto(self.add_label(answer_dict=))

    # def add_label(self, answer_dict):
    #     self.write("")
    #
    #     return (0,0)