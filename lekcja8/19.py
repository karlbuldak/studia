class statistics():
    def __init__(self, array):
        self.array=array
        
    def add(self, array1):
        self.array.append(array1)
        
    def display(self):
        for i in self.array:
            print(i, end=' ')
            
    def greatest(self):
        print(max(self.array))
        
    def smallest(self):
        print(min(self.array))
        
    def mean(self):
        print(sum(self.array)/len(self.array))
    
    def median(self):
        self.array=sorted(self.array)
        if len(self.array)%2==1:
            print(self.array[len(self.array)//2])
        else:
            print((self.array[len(self.array)//2]+self.array[len(self.array)//2-1])/2)
    
    
a=statistics([12, 37, 6, 9, 17])
a.median()
a.add(3)
a.median()
