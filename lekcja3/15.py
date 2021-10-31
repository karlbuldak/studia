import mymath

guess = mymath.read_number()
randomnum = mymath.generate_number()

if guess == randomnum:
    print("Wygrałeś!")
else:
    print("Przegrałeś!")