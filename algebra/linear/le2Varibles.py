from typing import Tuple


class LinearEquation2Varaibles:
    # ax + by + c = 0
    def __init__(self, a:float, b:float, c:float)-> None:
        self.a = a
        self.b = b
        self.c = c

    def solve(self, eq2:"LinearEquation2Varaibles")-> Tuple[float]:
        pass
