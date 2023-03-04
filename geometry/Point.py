try:
    from typing import Tuple
    from utils import distanceBetweenPoints
except:
    pass

class Point():
    def __init__(self, coordinate: Tuple[float]) -> None:
        # (x,y) input
        assert len(coordinate) == 2, "Invalid input for a 2D point"
        self.xcoord = coordinate[0]
        self.ycoord = coordinate[1]

    def dist2origin(self) -> float:
        dist = (self.xcoord**2 + self.ycoord**2)**0.5
        return dist

    def dist2point(self, point2) -> float:
        return distanceBetweenPoints(self, point2)