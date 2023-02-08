try:
    import math
except:
    pass


class IllegalPoint(Exception):
    "Invalid Point"


class Point():
    def __init__(self, coordinate: tuple) -> None:
        # (x,y) input
        if (len(coordinate) != 2):
            raise IllegalPoint
        self.xcoord = coordinate[0]
        self.ycoord = coordinate[1]

    def dist2origin(self) -> float:
        dist = (self.xcoord**2 + self.ycoord**2)**0.5
        return dist

    def dist2point(self, point: tuple) -> float:
        if len(point) != 2:
            raise IllegalPoint
        try:
            point[0] = float(point[0])
            point[1] = float(point[1])
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

def points2line(point1:Point,point2:Point) -> Line:
    x1,y1 = (point1.xcoord,point1.ycoord)
    x2,y2 = (point2.xcoord,point2.ycoord)
    
    if x1==x2:
        slope = 'inf'
    else:
        slope = (y2-y1)/(x2-x1)
    
    if slope == 'inf':
        ycoeff=0
        xcoeff=1
        constant=(-1)*x1
    else:
        xcoeff = y1-y2
        ycoeff = x2-x1
        constant = (x1-x2)*y1+x1*(y2-y1)
    return Line((xcoeff,ycoeff,constant))
    
