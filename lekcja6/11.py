film_titles=['film1','film2','film3','film4','film5']
file=open('filmtitles.txt','w')
for i in film_titles:
    file.write(i+'\n')
file.close()
file=open('filmtitles.txt','r')
for i in file:
    print(i,end='')

    
    