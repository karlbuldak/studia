array=[15, 38, 7, 23, 14]
spr=int(input('Input number that you want to check for: '))
a=3

#sketchy solution

for i in array:
    if spr==i:
        a=1
    if a==1:
        break
    if spr!=i:
        a=0

if a==1:
    print(f'Number {spr} does appear in the array.')
if a==0:
    print(f'Number {spr} does not appear in the array.')