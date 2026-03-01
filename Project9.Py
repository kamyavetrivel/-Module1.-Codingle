
class Polygon:

    def area(self):
        print("Area method should be implemented in child class")



class Rectangle(Polygon):

    def __init__(self, length, width):
        self.length = length
        self.width = width

   



class Square(Polygon):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side



class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    



r = Rectangle(10, 5)
s = Square(4)
t = Triangle(6, 8)


for shape in (r, s, t):
    print("Area is:", shape.area())
