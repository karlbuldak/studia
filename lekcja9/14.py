class area():
    @staticmethod
    def triangle(base, height):
        return(base*height/2)
    @staticmethod
    def rectangle(sidea, sideb):
        return(sidea*sideb)
    @staticmethod
    def circle(radius):
        import math
        return(math.pi*radius**2)
    
print(area.circle(3))
print(area.rectangle(4,7))
print(area.triangle(6,2))