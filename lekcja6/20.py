liczby=[]
for i in range(1,51):
    liczby.append(i)
print(liczby)
file=open('liczby.txt','w')
for i in liczby:
    i=str(i)
    file.write(f'{i}\n')
file.close()