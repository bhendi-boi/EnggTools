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
    def __init__(self,equation:tuple) -> None:
        #Stored in (a,b,c) tuple, of equation ax+by+c=0
        #Parse     
        self.xcoeff = equation[0]
        self.ycoeff = equation[1]
        self.constant = equation[2]
        
        
    def cointainsPoint(self, point:Point)->bool:
        xcoord = point.xcoord
        ycoord = point.ycoord
        if int(self.xcoeff* xcoord + self.ycoeff*ycoord + self.constant):
            return False
        return True
        
    

