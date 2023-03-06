import numpy
from .point import Point
from .line import Line
from .circle import Circle


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        dists = [a.dist2point(Point((b.xcoord, b.ycoord))), a.dist2point(
            Point((c.xcoord, c.ycoord))), b.dist2point(Point((c.xcoord, c.ycoord)))]
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
