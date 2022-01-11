class C():
    def __init__(self, tekst):
        self.tekst=tekst
    def m1(self):
        slownik={}
        for i in self.tekst:
            if i not in slownik:
                slownik[i]=self.tekst.count(i)
        return(slownik)
    
    def m2(self, c1):
        slownik2={}
        for i in c1:
            slownik2[i]=self.tekst.count(i)
        return(slownik2)

print(C("my moon").m1())
print(C("my moon").m2("mn"))