filename=str(input('Wprowadź nazwe pliku: '))
i=0
with open(filename) as f:
    for line in f:
        i+=1
        
print(f'Nazwa pliku: {f.name}')
print(f'Liczba linijek: {i}')