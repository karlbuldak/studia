import stack

liczba=int(input('Wprowadź liczbę: '))

while liczba>0:
    if liczba%2==0:
        stack.push(0)
    if liczba%2==1:
        stack.push(1)
    liczba=liczba//2
stack.display()


