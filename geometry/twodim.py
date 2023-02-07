class Point():
    def __init__(self, coordinate:str):
        # (x,y) input
        while (coordinate.find(' ') != -1):
            pos = coordinate.find(' ')
            coordinate = list(coordinate)
            coordinate.pop(pos)
            coordinate = ''.join(coordinate)
        poscomma = coordinate.find(',')
        self.xcoord = float(coordinate[1:poscomma])
        self.ycoord = float(coordinate[poscomma+1,:])

    def dist2origin(self):
        dist = (self.xcoord**2 + self.ycoord**2)**0.5
        return dist
        

class Line():
    def __init__(self,equation:str) :
        #Stored in (a,b,c) tuple, of equation ax+by+c=0
        #Parse
        while(equation.find(' ') != -1):
            pos = equation.find(' ')
            equation = list(equation)
            equation.pop(pos)
            equation = ''.join(equation)

        posx = equation.find('x')
        posy = equation.find('y')
        posequal = equation.find('=')
        
        self.xcoeff = float(equation[0:posx])
        self.ycoeff = float(equation[posx+1:posy])
        self.constant = float(equation[posy+1:posequal])
        
    

