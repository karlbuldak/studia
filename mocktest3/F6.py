class C():
    def __init__(self, array):
        self.array=array
        
    def m(self):
        a=0
        for i in range(len(self.array)):
            try:
                if self.array[i]==self.array[i+2]:
                    a+=1
            except:
                pass
        return(a)
            

        
# print(C([True,False,True,True,False,True,False,True,False]).m())
            
        
    