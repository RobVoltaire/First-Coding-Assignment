import turtle

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

def draw_rect(t, rect):
    """Draw a rectangle using a Turtle object."""
    t.penup()
    t.goto(rect.x, rect.y)  # Move to starting position
    t.pendown()
    
    for _ in range(2):
        t.forward(rect.width)
        t.right(90)
        t.forward(rect.height)
        t.right(90)

def draw_circle(t, circ):
    """Draw a circle using a Turtle object."""
    t.penup()
    t.goto(circ.x, circ.y - circ.radius)  # Move to bottom of circle
    t.pendown()
    t.circle(circ.radius)

# Example usage
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a rectangle
rect = Rectangle(-50, 50, 100, 60)
draw_rect(t, rect)

# Draw a circle
circ = Circle(100, 100, 40)
draw_circle(t, circ)

turtle.done()
