file=open('data.txt','w')
file.write('Karol\nBułdak\nUEK\nInformatyka Stosowana')
file.close()
file=open('data.txt','r')
for i in file:
    print(i,end='')
file.close