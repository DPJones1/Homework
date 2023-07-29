import abc
class Shape(object):
    __metaclass__ = abc.ABCMeta\

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = 
    def calc_perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calc_perimeter(self):
        return 2 * self.a + self.b

class Square(Rectangle):
    def __init__(self, a,):
        super().__init__(a, a)


triangle = Triangle(4, 5, 6)
rectangle = Rectangle(4, 2)
square = Square(5)

print("Perimeter of triangle:", triangle.calc_perimeter())
print("Perimeter of rectangle:", rectangle.calc_perimeter())
print("Perimeter of square:", square.calc_perimeter())


