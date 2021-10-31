x = int(input("Wprowadź x: "))
y = int(input("Wprowadź y: "))

if x > 0 and y > 0:
   cwiartka = 1
if x > 0 and y < 0:
    cwiartka = 4
if x < 0 and y < 0:
   cwiartka = 3
if x < 0 and y > 0:
    cwiartka = 2
if x == 0 and y == 0:
    print("Punkt to początek układu współrzędnych")
else:
    print(f"Punkt [{x}, {y}] jest w {cwiartka} ćwiartce układu współrzędnych")

