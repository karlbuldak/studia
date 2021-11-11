l=[1,3,4,7,8,29]
parzyste=0
nieparzyste=0
for i in l:
    if i%2==0:
        parzyste+=1
    if i%2!=0:
        nieparzyste+=1
        
print(f"Parzystych: {parzyste}, nieparzystych: {nieparzyste}")