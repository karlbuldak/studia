file= open('30linijek.txt')

for i in range(0,5):
    print(file.readline())
for i in file:
    enter=str(input('Enter by wyswietlic kolejne 5 linijek'))
    if enter=='':
        print(i)
        for a in range(0,4):
            print(file.readline())
file.close()
