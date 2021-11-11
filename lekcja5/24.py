array=[3,4,23,34,54,65]
a=0
liczba=int(input('Wprowadź liczbę: '))
for i in array:
    if i>liczba:
        a+=1
        
print(a)