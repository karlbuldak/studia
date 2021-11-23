import random
liczby=[]
for i in range(50):
    liczby.append(random.randint(100,1000))
file=open('randint.txt','w')
for i in liczby:
    file.write(f'{i}\n')
file.close()