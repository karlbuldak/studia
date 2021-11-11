array=[1,2,3,4,5,6,7]
uporzadkowana=[]
for i in array:
    if i%2==0:
        uporzadkowana.append(i)
for i in array:
    if i%2==1:
        uporzadkowana.append(i)
        
print(uporzadkowana)
        