array=[2,3,2,5,8,1,9,8]
output=[]
for i in array:
    if i not in output:
        output.append(i)
print(output)