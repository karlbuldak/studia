wartosc = int(input("Wprowadź wartość: "))
i = 0
suma = 0
if wartosc == 0:
    print("Wprowadź wcześniej chociaż jedną wartość różną od zera.")
while wartosc != 0:
    suma += wartosc
    wartosc = int(input("Wprowadź wartość: "))
    i += 1
    if wartosc == 0:
        print(f"WYNIK: Ile liczb: {i}, Suma: {suma}, Średnia artmetyczna: {suma/i}.")
        
    
    