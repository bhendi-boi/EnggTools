try:
    # external dependencies
    import math
    import numpy as np
    # Core classes
    from Point import Point

    # utils
    from utils import distanceBetweenPoints
    from typing import Tuple, Union
except:
    pass


class IllegalPoint(Exception):
    "Invalid Point"


class QuadraticEquation():
    def __init__(self, x2: float, y2: float, x: float, y: float, c: float) -> None:
        self.x2 = x2
        self.y2 = y2
        self.x = x
        self.y = y
        self.c = c





class Line():
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


class Circle():
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


class Triangle():
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        dists = [a.dist2point((b.xcoord, b.ycoord)), a.dist2point(
            (c.xcoord, c.ycoord)), b.dist2point((c.xcoord, c.ycoord))]
        dists.sort()
        assert dists[0]+dists[1] > dists[2], "Invalid Triangle"
        self.perimeter = dists[0]+dists[1]+dists[2]
        s = self.perimeter/2
        self.area = (s*(s-dists[2])*(s-dists[1])*(s-dists[0]))**0.5
        self.hasCircle = False

    def getSideEquations(self):
        e1 = Line.points2line(self.a, self.b)
        e2 = Line.points2line(self.b, self.c)
        e3 = Line.points2line(self.a, self.c)
        equations = (e2, e3, e1)  # In order of sides A B C
        return equations

    def getCircumcircle(self):
        if self.hasCircle == True:
            return self.circle
        else:
            self.hasCircle = True
            a = self.a
            b = self.b
            c = self.c
            ax, ay = a.xcoord, a.ycoord
            bx, by = b.xcoord, b.ycoord
            cx, cy = c.xcoord, c.ycoord

            arr = np.array([ax, ay, 1, bx, by, 1, cx, cy, 1])
            arr = arr.reshape(3, 3)
            sqr_coeff = np.linalg.det(arr)

            arr = np.array([ax**2+ay**2, ay, 1, bx**2+by **
                           2, by, 1, cx**2+cy**2, cy, 1])
            arr = arr.reshape(3, 3)
            lin_coeff_x = np.linalg.det(arr)
            lin_coeff_x *= -1

            arr = np.array([ax**2+ay**2, ax, 1, bx**2+by **
                           2, bx, 1, cx**2+cy**2, cx, 1])
            arr = arr.reshape(3, 3)
            lin_coeff_y = np.linalg.det(arr)

            arr = np.array([ax**2+ay**2, ax, ay, bx**2+by **
                           2, bx, by, cx**2+cy**2, cx, cy])
            arr = arr.reshape(3, 3)
            const_coeff = np.linalg.det(arr)
            const_coeff *= -1

            center = (-1*lin_coeff_x/(2*sqr_coeff), -
                      1*lin_coeff_y/(2*sqr_coeff))
            radius = ((lin_coeff_x/(2*sqr_coeff))**2+(lin_coeff_y /
                      (2*sqr_coeff))**2-(const_coeff/(sqr_coeff)))**0.5
            self.circle = Circle(radius, Point(center))
            return self.circle


def intersectionPointofTwoLines(l1: Line, l2: Line):
    a, b, c = l1.xcoeff, l1.ycoeff, l1.constant
    d, e, f = l2.xcoeff, l2.ycoeff, l2.constant
    assert b/a != e/d, "Lines are parallel, no intersection"
    k = b/e
    l = a/d
    x = (f*k-c)/(a-d*k)
    y = (l*f-c)/(b-l*e)
    poi = (x, y)
    return Point(poi)





class Quadrilateral():
    '''
    Points must be given in cyclic order
    '''

    def __init__(self, vertices: Tuple[Point]) -> None:
        self.v1 = vertices[0]
        self.v2 = vertices[1]
        self.v3 = vertices[2]
        self.v4 = vertices[3]

        self.l1 = Line.points2line(self.v1, self.v2)
        self.l2 = Line.points2line(self.v2, self.v3)
        self.l3 = Line.points2line(self.v3, self.v4)
        self.l4 = Line.points2line(self.v1, self.v4)

        self.lengths = (distanceBetweenPoints(self.v1, self.v2), distanceBetweenPoints(
            self.v2, self.v3), distanceBetweenPoints(
            self.v3, self.v4), distanceBetweenPoints(self.v1, self.v4)
        )
        self.perimeter = self.lengths[0] + \
            self.lengths[1]+self.lengths[2]+self.lengths[3]

    def isRectangle(self) -> bool:
        l1 = self.l1
        l2 = self.l2
        l3 = self.l3
        l4 = self.l4
        return l1.isPerpendicularTo(l2) and l1.isPerpendicularTo(l4) and l1.isParallelTo(l3) and self.lengths[0] == self.lengths[2] and self.lengths[1] == self.lengths[3]

    def isRhombus(self) -> bool:
        return self.lengths[0] == self.lengths[2] and self.lengths[1] == self.lengths[3] and self.lengths[1] == self.lengths[2]

    def isSquare(self) -> bool:
        return self.isRectangle() and self.isRhombus()
