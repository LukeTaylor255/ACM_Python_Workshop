class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*3.14
    def circumference(self):
        return self.radius*3.14*2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return self.width*2 + self.height*2


class Square(Rectangle):
    def __init__(self, edge_length):
        self.width = edge_length
        self.height = edge_length