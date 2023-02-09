try:
    import math
    import numpy as np
except:
    pass


class IllegalPoint(Exception):
    "Invalid Point"


class Point():
    def __init__(self, coordinate: tuple) -> None:
        # (x,y) input
        assert len(coordinate) ==2,"Invalid input for a 2D point"
        self.xcoord = coordinate[0]
        self.ycoord = coordinate[1]

    def dist2origin(self) -> float:
        dist = (self.xcoord**2 + self.ycoord**2)**0.5
        return dist

    def dist2point(self, point: tuple) -> float:
        assert len(point)==2,"Invalid input for 2D point"
        try:
            float(point[0])
            float(point[1])
        except:
            raise IllegalPoint
        x1 = self.xcoord
        y1 = self.ycoord
        x2 = point[0]
        y2 = point[1]
        dist: float
        dist = ((x1 - x2)**2 + (y1-y2)**2)**0.5
        return dist


class Line():
    def __init__(self, equation: tuple) -> None:
        # Stored in (a,b,c) tuple, of equation ax+by+c=0
        # Parse
        self.xcoeff = equation[0]
        self.ycoeff = equation[1]
        self.constant = equation[2]

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


class Circle():
    def __init__(self, radius: float, center: Point) -> None:
        self.radius = radius
        self.center = center
        self.area = math.pi*radius*radius
        self.diameter = self.radius*2

# enduku ra
class Triangle():
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        dists = [a.dist2point((b.xcoord,b.ycoord)),a.dist2point((c.xcoord,c.ycoord)),b.dist2point((c.xcoord,c.ycoord))]
        dists.sort()
        assert dists[0]+dists[1] > dists[2],"Invalid Triangle"
        self.perimeter = dists[0]+dists[1]+dists[2]
        s = self.perimeter/2
        self.area = (s*(s-dists[2])*(s-dists[1])*(s-dists[0]))**0.5
        self.hasCircle = False

    def getSideEquations(self):
        e1 = Line.points2line(self.a, self.b)
        e2 = Line.points2line(self.b, self.c)
        e3 = Line.points2line(self.a, self.c)
        equations = (e2, e3, e1) #In order of sides A B C
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
            arr = arr.reshape(3,3)
            sqr_coeff = np.linalg.det(arr)

            
            arr = np.array([ax**2+ay**2, ay, 1, bx**2+by**2, by, 1, cx**2+cy**2, cy, 1])
            arr = arr.reshape(3,3)
            lin_coeff_x = np.linalg.det(arr)
            lin_coeff_x*=-1

            
            arr = np.array([ax**2+ay**2, ax, 1, bx**2+by**2, bx, 1,cx**2+cy**2, cx, 1])
            arr = arr.reshape(3,3)
            lin_coeff_y = np.linalg.det(arr)

            
            arr = np.array([ax**2+ay**2, ax, ay, bx**2+by**2, bx, by, cx**2+cy**2, cx, cy])
            arr = arr.reshape(3,3)
            const_coeff= np.linalg.det(arr)
            const_coeff*=-1

            center = (-1*lin_coeff_x/(2*sqr_coeff),-1*lin_coeff_y/(2*sqr_coeff))
            radius = ((lin_coeff_x/(2*sqr_coeff))**2+(lin_coeff_y/(2*sqr_coeff))**2-(const_coeff/(sqr_coeff)))**0.5
            self.circle = Circle(radius,Point(center))
            return self.circle