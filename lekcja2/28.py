a = 0
b = 1

c = 2

print(f"{a} {b}", end=" ")

while c < 50:
    print(f"{a+b}", end=" ")
    c += 1
    if c % 2 == 0:
        b = (a+b)
    if c % 2 == 1:
        a = (a+b)
    
    
    