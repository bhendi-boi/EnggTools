
import math
from .point import Point
from .utils import intersectionPointofTwoLines
from utils import lineParser
from typing import Union, Tuple


class Line:
    def __init__(self, equation: Tuple[float]) -> None:
        # Stored in (a,b,c) tuple, of equation ax+by+c=0
        # Parse
        self.xcoeff = equation[0]
        self.ycoeff = equation[1]
        self.constant = equation[2]
        if self.ycoeff == 0:
            self.slope = 'inf'
        else:
            self.slope = -self.xcoeff/self.ycoeff

    @classmethod
    def initFromString(self,lineEq: str)->"Line":
        coordinates = lineParser(lineEq)
        return Line(coordinates)

    @classmethod
    def points2line(cls, point1: Point, point2: Point):
        x1, y1 = (point1.xcoord, point1.ycoord)
        x2, y2 = (point2.xcoord, point2.ycoord)

        if x1 == x2:
            slope = 'inf'
        else:
            slope = (y2-y1)/(x2-x1)

        if slope == 'inf':
            ycoeff = 0
            xcoeff = 1
            constant = (-1)*x1
        else:
            xcoeff = y1-y2
            ycoeff = x2-x1
            constant = (x1-x2)*y1+x1*(y2-y1)
        return Line((xcoeff, ycoeff, constant))

    def containsPoint(self, point: Point) -> bool:
        xcoord = point.xcoord
        ycoord = point.ycoord
        if int(self.xcoeff * xcoord + self.ycoeff*ycoord + self.constant):
            return False
        return True

    def onSameSide(self, p1: Point, p2: Point) -> bool:
        e1 = self.xcoeff*p1.xcoord + self.ycoeff*p1.ycoord+self.constant
        e2 = self.xcoeff*p2.xcoord + self.ycoeff*p2.ycoord+self.constant
        sign1 = math.copysign(1, e1)
        sign2 = math.copysign(1, e2)
        if sign1 == sign2:
            return True
        else:
            return False

    def passesThroughOrigin(self) -> bool:
        return self.constant == 0

    def isParallelTo(self, line2: "Line") -> bool:
        return self.slope == line2.slope

    def isPerpendicularTo(self, line2: "Line") -> bool:
        if (self.slope == 0 and line2.slope == 'inf') or (self.slope == 'inf' and line2.slope == 0):
            return True
        return self.slope * line2.slope == -1

    def isIntersectingWith(self, line2: "Line") -> bool:
        # unless both lines are parallel any pair of 2D Lines will always intersect
        return self.slope != line2.slope

    def intersectsAt(self, line2: "Line") -> Union[Point, bool]:
        if self.isIntersectingWith(line2):
            return intersectionPointofTwoLines(self, line2)
        return False
