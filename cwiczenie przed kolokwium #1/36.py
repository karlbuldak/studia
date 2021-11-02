import random

n = random.randint(0,101)

guess = int(input('Zgadnij jaka to liczba!: '))

while guess != n:
    if guess > n:
        print('Spróbuj wpisać mniejszą liczbe...')
        guess = int(input('Zgadnij jaka to liczba!: '))
    if guess < n:
        print('Spróbuj wpisać większą liczbe...')
        guess = int(input('Zgadnij jaka to liczba!: '))
else:
    print('')
    print('Zgadłeś!!!')