def distanceBetweenPoints(point1, point2) -> float:
    x1 = point1.xcoord
    y1 = point1.ycoord
    x2 = point2.xcoord
    y2 = point2.ycoord
    dist: float
    dist = ((x1 - x2)**2 + (y1-y2)**2)**0.5
    return dist


def intersectionPointofTwoLines(l1, l2):
    a, b, c = l1.xcoeff, l1.ycoeff, l1.constant
    d, e, f = l2.xcoeff, l2.ycoeff, l2.constant
    assert b/a != e/d, "Lines are parallel, no intersection"
    k = b/e
    l = a/d
    x = (f*k-c)/(a-d*k)
    y = (l*f-c)/(b-l*e)
    poi = (x, y)
    from geometry import Point
    return Point(poi)
