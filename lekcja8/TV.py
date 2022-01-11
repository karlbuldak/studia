class TV():
    
    def __init__(self):
        self.ison=False
        self.channel_no=1
        self.channels_list=[]
        self.volume=0
        
    def turn_on(self):
        self.ison=True
        
    def turn_off(self):
        self.ison=False
    
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
        
    def show_status(self):
        if self.ison == True:
            if len(self.channels_list) < self.channel_no:
                print('TV is ON, channel', self.channel_no, 'volume is', self.volume)
            else:            
                print('TV is ON, channel', self.channel_no, self.channels_list[(self.channel_no)-1], 'volume is', self.volume)
        else:
            print('TV is OFF')
    
    def set_channels(self, channels_list):
        self.channels_list=(channels_list)
    
    def show_channels(self):
        if len(self.channels_list)==0:
            print('TV channels list is empty')
        else:
            print('TV channels list: ')
            for i in self.channels_list:
                print(i, end=', ')
            print()
    
    def volume_increase(self):
        if self.volume==10:
            print("TV already at maximum volume")
        else:
            print('Increased volume by one')
            self.volume+=1
        
    def volume_decrease(self):
        if self.volume==0:
            print("TV already at minimum volume")
        else:
            print('Decreased volume by one')
            self.volume-=1
            
        
            
            
TV1=TV()
TV1.turn_on()
TV1.show_status()
TV1.volume_decrease()
TV1.show_status()
TV1.turn_on()
TV1.show_status()
TV1.show_channels()
TV1.set_channels(['TVP1', 'TVP2', 'TVN', 'Polsat', 'Filmbox', 'Discovery', 'ESPN'])
TV1.show_channels()
TV1.show_status()
TV1.set_channel(2)
TV1.show_status()
TV1.set_channel(8)
TV1.show_status()
TV1.set_channel(7)
TV1.show_status()
TV1.turn_off()

#wszysko dziala :D



        
    