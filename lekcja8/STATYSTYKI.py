class Statistics():
    
    def __init__(self):
        self.set=[]
        
    def add(self):
        zbior=input('Wprowadź  zbiór liczb: ')
        self.set=zbior
        
    def display(self):
        for i in self.set:
            print(i, end=', ')
        print()
            
    def add(self):
        liczba=int(input("Wprowadź liczbę: "))
        self.set.append(liczba)
        
    def max(self):
        print(max(self.set))
        
    def min(self):
        print(min(self.set))
        
    def mean(self):
        print(sum(self.set)/len(self.set))
        
    def median(self):
        i=int(len(self.set))
        a=int(i/2)
        if len(self.set)%2==1:
            print(self.set[a])
            
        if len(self.set)%2==0:
            print((self.set[a]-1)+(self.set[a])/2)
            
# Display of calculated / determined statistical
# quantities (minimum, maximum, arithmetic mean, median)

jeden=Statistics()
jeden.add()
jeden.add()
jeden.add()
jeden.add()
jeden.add()
jeden.add()
jeden.display()
jeden.mean()
jeden.median()