file=open('filename2.txt')
content=str(file.read())
filecopy=open('filenamecopy2.txt','w')
filecopy.write(content)
file.close()
filecopy.close()