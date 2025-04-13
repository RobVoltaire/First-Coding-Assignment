class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
 
center_point = Point(150, 100)
circle = Circle(center_point, 75)

import math

def point_in_circle(circle, point):
    distance = math.sqrt((point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2)
    return distance <= circle.radius
    
class Rectangle:
    def __init__(self, bottom_left, width, height):
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def corners(self):
        """Returns a list of all four corners of the rectangle."""
        return [
            self.bottom_left,
            Point(self.bottom_left.x + self.width, self.bottom_left.y),
            Point(self.bottom_left.x, self.bottom_left.y + self.height),
            Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height)
        ]
        
def rect_in_circle(circle, rectangle):
    # Check if all corners are within the circle
    return all(point_in_circle(circle, corner) for corner in rectangle.corners())

def rect_circle_overlap(circle, rectangle):
    # Check if any corner is within the circle
    return any(point_in_circle(circle, corner) for corner in rectangle.corners())


