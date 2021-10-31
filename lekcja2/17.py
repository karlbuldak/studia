x = int(input("Wprowadź x: "))
y = int(input("Wprowadź y: "))

if x > 0 and y > 0:
    print("Punkt znajduje się w I ćwiartce")
if x > 0 and y < 0:
    print("Punkt znajduje się w VI ćwiartce")
if x < 0 and y < 0:
    print("Punkt znajduje się w III ćwiartce")
if x < 0 and y > 0:
    print("Punkt znajduje się w II ćwiartce")
if x == 0 and y == 0:
    print("Punkt to początek układu współrzędnych")
