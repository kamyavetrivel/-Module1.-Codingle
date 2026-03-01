
class Polygon:
    def area(self):
        pass   



class Rectangle(Polygon):
    def __init__(self, length, width):
        self.__length = length      

        self.__width = width

    def area(self):
        return self.__length * self.__width



class Square(Polygon):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side



class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height




r = Rectangle(10, 5)
s = Square(4)
t = Triangle(6, 8)


for shape in (r, s, t):
    print("Area is:", shape.area())
