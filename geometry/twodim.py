try:
    # external dependencies
    import math
    import numpy as np
    # Core classes
    from .point import Point
    from .line import Line
    # utils
    from utils import distanceBetweenPoints

    
except:
    pass


class IllegalPoint(Exception):
    "Invalid Point"
















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
