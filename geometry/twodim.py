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
        
    

