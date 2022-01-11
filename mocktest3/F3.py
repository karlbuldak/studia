class C():
    def __init__(self, array):
        self.array=array
        
    def m(self):
        check=[]
        for i in self.array:
            i=i.upper()
            if i not in check:
                check.append(i)
        return(len(self.array)!=len(check))
            