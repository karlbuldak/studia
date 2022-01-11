class student():
    university='UEK Kraków'
    id=100000
    
    def __init__(self, name, surname, major):
        self.name=name
        self.surname=surname
        self.major=major
        student.id+=1
        
    def __str__(self):
        return(f'{self.name} {self.surname}, ({student.id}), {self.major}, {student.university}')
    
print(student('Anna','Maj','informatyka'))

print(student('Marek','Gaj','informatyka'))

print(student('Franek','Faj','informatyka'))        