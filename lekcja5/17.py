a=[4,36,12,28,9,44,5] 
b=[5,1,36]
for i in range(len(a)):
    for j in range(len(b)):
        if (a[i] == b[j]):
            break
    if (j == len(b) - 1):
        print(a[i], end = " ")
