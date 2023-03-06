from typing import Tuple
from math import sqrt
from .utils import distanceBetweenPoints3D

class Point3D:
    def __init__(self, coordinates: Tuple[float]) -> None:
        # (x, y, z) input
        assert len(coordinates) == 3, "Invalid input for a 3D point"
        self.xcoord = coordinates[0]
        self.ycoord = coordinates[1] 
        self.zcoord = coordinates[2] 

    def dist2origin(self)->float:
        # √x^2 + y^2 + z^2
        return sqrt(self.xcoord**2 + self.ycoord**2+ self.zcoord**2)
    
    def dist2point(self,point2: "Point3D")->float:
        return distanceBetweenPoints3D(self,point2)
