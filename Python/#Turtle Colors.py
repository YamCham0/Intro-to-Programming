906030




  margin-top: auto;
  margin-right: auto;
  margin-left: auto;
  border: 8px double black;
  width: 325px;
  height: 300px;












import turtle



jack = turtle.Turtle()
jack.speed(0)
jack.width(3)
jack.color("red")
jack.penup()
jack.back(90)
jack.pendown()

def draw_polygon(length, sides, color):
    jack.color(color)
    for side in range(4):
        jack.forward(length)
        jack.right(sides)
        
draw_polygon(100, 90, "yellow")
draw_polygon(200, 72, "blue")
draw_polygon(300, 120, "green")