from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=550, height=400)
user_bet = screen.textinput(title="Place your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
initial_pos = -80
racing_turtles = []
is_race_on = False

# Draw finish line
ref_turtle = Turtle()
ref_turtle.penup()
ref_turtle.goto(x=250, y=-150)
ref_turtle.setheading(90)
ref_turtle.pendown()
ref_turtle.forward(270)
ref_turtle.hideturtle()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-180, y=initial_pos)
    initial_pos += 30
    racing_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racing_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost! The winner is the {winning_color} turtle.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
