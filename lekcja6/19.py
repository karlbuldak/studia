file=open('MeatAndFish.txt')
shoppinglist=[]
for i in file:
    shoppinglist.append(i)
file2=open('GrainsAndBread.txt')
for i in file2:
    shoppinglist.append(i)
file3=open('shoppinglist.txt','w')
for i in shoppinglist:
    file3.write(i)
file.close()
file2.close()
file3.close()
    