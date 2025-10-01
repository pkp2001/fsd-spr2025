from abc import ABC, abstractmethod
class Polygon(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def area(self):
        pass

class Square(Polygon):
    def __init__(self, side):
        super().__init__('Square')
        self.side = float(side)

    def area(self):
        return self.side * self.side

    def __str__(self):
        return '%-8s area = %-6.2f' % (self.type, self.area())

class Triangle(Polygon):
    def __init__(self, height, base):
        super().__init__('Triangle')
        self.height = float(height)
        self.base = float(base)

    def area(self):
        return 0.5 * self.height * self.base

    def __str__(self):
        return '%-8s area = %-6.2f' % (self.type, self.area())

class Shapes:
    def __init__(self):
        self.shapes = []

    def load_shapes(self):
        self.shapes.append(Square(5))
        self.shapes.append(Square(10))
        self.shapes.append(Triangle(5, 3))
        self.shapes.append(Triangle(5, 5))

    def show(self):
        for shape in self.shapes:
            print(shape)

if __name__ == '__main__':
    shapes = Shapes()
    shapes.load_shapes()
    shapes.show()