filenamecontent=[]
with open('filename.txt') as f:
    for i in f:
        filenamecontent.append(i)
    with open('filenamecopy.txt', 'w') as r:
        for a in filenamecontent:
            r.write(a)