try:
    import Point
except:
    pass

def distanceBetweenPoints(point1: Point, point2: Point) -> float:
    x1 = point1.xcoord
    y1 = point1.ycoord
    x2 = point2.xcoord
    y2 = point2.ycoord
    dist: float
    dist = ((x1 - x2)**2 + (y1-y2)**2)**0.5
    return dist
