import turtle



jack = turtle.Turtle()
jack.speed(4)
jack.width(3)
jack.color("red")
jack.penup()
jack.back(90)
jack.pendown()

def draw_polygon(length, sides, color):
    jack.color(color)
    for side in range(8):
        jack.forward(length)
        jack.right(sides)
        
draw_polygon(100, 90, "yellow")
draw_polygon(200, 72, "blue")
draw_polygon(300, 120, "green")
draw_polygon(200, 60, "red")
draw_polygon(100, 45, "purple")