wiek = float(input("Wprowadź wiek psa: "))

if wiek <= 2:
    wiek = wiek*10.5
else:
    wiek = 21+(wiek-2)*4
    
print(f"Wiek psa w przeliczeniu na ludzkie lata: {wiek}")