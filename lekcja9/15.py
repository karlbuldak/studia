class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        import math
        if isinstance(other, Point):
            #pierw([x2-x1)**2+(y2-y1)**2]
            return(f'The distance is {math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)}')
        return('The distance is 0')
a=Point(1,1)
b=Point(1,1)
print(a==b)