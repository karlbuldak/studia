import re
with open('beautybeast.txt') as file:
    for i in file:
        list=re.findall(r'\b[a-zA-Z]{12,}\b',i)
        for j in list:
            j=j.upper()
            print(j,end=' ')

    