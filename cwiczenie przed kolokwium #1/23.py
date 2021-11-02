i=5
licznik5=0
while i != 0:
    n=int(input('Wprowadź dowolną liczbę od 1 do 10: '))
    if n < 1 or n > 10:
        print('Liczba musi być z zakresu od 1 do 10!')
        i += 1
    if n == 5:
        licznik5 += 1
    i -= 1
print(f'Użytkownik wybrał {licznik5} razy liczbę 5.')
    
          