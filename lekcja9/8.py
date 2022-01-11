class phone():
    def __init__(self, battery, number, model):
        self.battery=battery
        self.number=number
        self.model=model
        
    def checkbattery(self):
        print(f'Your battery percentage is {self.battery}%')
    
    def plug(self):
        if self.battery!=100:
            print(f'Your battery percentage is {self.battery}%, starting to charge...')
            while self.battery!=100:
                self.battery+=1
                print(f'Charging, battery percentage is {self.battery}%')
            print('Battery full, unplug!')            
        
        else:
            print('Battery full, unplug!')
            
iphone=phone(99, 123, 'X')
iphone.plug()