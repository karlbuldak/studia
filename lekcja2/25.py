a = int(input("a: "))
b = int(input("b: "))

print("*"*a)
while (b-2) > 0:
    print("*" + " "*(a-2) + "*")
    b -= 1
    
print("*"*a)