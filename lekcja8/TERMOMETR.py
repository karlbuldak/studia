import random

class termometr():
    def __init__(self):
        self.wlaczony=False
        self.temperatura=0
        
    def wlacz(self):
        self.wlaczony=True
        print('Wlaczyles termometr')
        
    def wylacz(self):
        self.wlaczony=False
        print('Wylaczyles termometr')
        
    def zmierz(self):
        if self.wlaczony==True:
            self.temperatura=round(random.uniform(34,42), 1)
            if self.temperatura>=41:
                print(f"Temperatura: {self.temperatura} C, (fever)")
            else:
                print(f"Temperatura: {self.temperatura} C")
        if self.wlaczony==False:
            print('Termometr wyłączony')
            
            
termometr=termometr()
termometr.zmierz()
termometr.wlacz()
termometr.zmierz()
termometr.wylacz()