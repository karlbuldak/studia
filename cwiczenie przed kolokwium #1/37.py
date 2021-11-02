n = int(input('Jak duża ma być piramida? '))
a = n-1
for i in range(n+1):
    print(i*'*')
while a != 0:
    print(a*'*')
    a -= 1
    