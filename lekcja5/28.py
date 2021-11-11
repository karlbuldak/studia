array=[1,4,5,567,54,345,90,793]
arraystr=[]
for i in array:
    i=str(i)
    arraystr.append(i)

print('-----------------------------------------')
print('|','|'.join(arraystr),'|')
print('-----------------------------------------')
