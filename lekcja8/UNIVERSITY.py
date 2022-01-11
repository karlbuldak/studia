class University():

    # object constructor (__init__ method)
    def __init__(self, university, fullname):
        # object states/attributes (fields)
        self.name = university
        self.fullname = fullname

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
    
    def set_name(self, name):
        self.name = name
    
    def set_fullname(self, fullname):
        self.fullname = fullname
        
    def print_fullname(self):
        print(self.fullname)
        
u1=University('UEK','Uniwersytet Ekonomiczny w Krakowie')
u1.print_name()
u1.print_fullname()
u1.set_name('PK')
u1.set_fullname('Politechnika Krakowska')
u1.print_name()
u1.print_fullname()