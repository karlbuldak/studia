class C():
    def __init__(self, slownik):
        self.system=slownik['system']
        self.value=slownik['value']
        
    def m(self):
        a=0
        b=0
        suma=0
        for i in self.value:
            if i<self.system:
                a+=1
        if a==len(self.value):
            for j in self.value:
                j=int(j)
                b=(j*int(self.system)**(a-1))
                a-=1
                suma+=b
            return(suma)
        else:
            return(-1)
                
                
                
#print(C({"system":"8", "value":"70281"}))