liczby=[]

file=open('liczbyipotegi.txt','w')

for i in range(1,11):
    liczby.append(i)
for a in liczby:
    file.write(f'{a} , {a**2} , {a**3} \n')
file.close()
    



    