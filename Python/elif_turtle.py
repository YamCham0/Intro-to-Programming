import random
mood = random.choice(["happy","sad", "anxious", "party"])


import turtle
riley = turtle.Turtle()
riley.width(5)
riley.speed(0)

if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == "anxious":
    riley.color("gray")
elif mood == "party":
    riley.color("cyan")
    

for side in range(5):
    riley.forward(100)
    riley.right(144)