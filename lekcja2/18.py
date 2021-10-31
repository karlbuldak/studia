kwota = int(input("Kwota w PLN: "))
reszta = kwota % 5
ile5 = int((kwota-reszta)/5)
ile1 = reszta % 2
pozostale = kwota-(ile1+ile5*5)
ile2 = int(pozostale / 2)

print(f"5 PLN: {ile5}")
print(f"2 PLN: {ile2}")
print(f"1 PLN: {ile1}")