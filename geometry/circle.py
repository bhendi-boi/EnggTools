import math
from .point import Point
from .utils import distanceBetweenPoints
# from .twodim import QuadraticEquation

class QuadraticEquation:
    def __init__(self, x2: float, y2: float, x: float, y: float, c: float) -> None:
        self.x2 = x2
        self.y2 = y2
        self.x = x
        self.y = y
        self.c = c

        
class Circle:
    def __init__(self, radius: float, center: Point) -> None:
        self.radius = radius
        self.center = center
        self.area = math.pi*radius*radius
        self.diameter = self.radius*2

    def onPoint(self, point: Point) -> bool:
        return self.radius == distanceBetweenPoints(self.center, point)

    def containsPoint(self, point: Point) -> bool:
        return self.radius >= distanceBetweenPoints(self.center, point)

    def getEquation(self) -> QuadraticEquation:
        equation = QuadraticEquation(1, 1, -2*self.center.xcoord, -2*self.center.ycoord,
                                     self.center.xcoord**2+self.center.ycoord**2-self.radius**2)
        return equation


