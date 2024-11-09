import turtle
from turtle import Turtle

import pandas
from label import Label

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
state = data[states == "Illinois"]
print(state.x.values[0])

test = Turtle()
test.hideturtle()
test.penup()
# test.goto(state.x, state.y)
# test.write("Test", align="center", font= ("Courier", 24, "normal"))

screen.exitonclick()

# score_and_label = Label()
#
# game_is_on = True
# while game_is_on:
#     answer_state = screen.textinput(title=f"Guess Score: {len(score_and_label.guesses)}/50 ", prompt="What's the state?").lower()
#     if answer_state in score_and_label.guesses:
#         print("Already Guessed")
#     else:
#         for state in states:
#             if state.lower() == answer_state:
#                 score_and_label.guesses.append(answer_state)

