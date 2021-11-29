import re
plik=open('30linijek.txt')
for line in plik:
    a=re.findall(r'\b[a-zA-Z]{6,}\b', line)
    for i in a:
        print(i)
plik.close()
        