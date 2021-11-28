kolory=['red','blue','yellow','orange']
with open('kolory.txt','w') as file:
    for i in kolory:
        file.write(i)
        file.write('\n')


