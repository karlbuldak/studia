array=[5,4,3,2,6,5]
arraystr=[]

for i in array:
    i=str(i)
    arraystr.append(i)
    
arraystr=','.join(arraystr)

print(arraystr)