pin = float(0.0805)

i = 3

while i > 0:
    pininput = float(input("Wprowadź PIN: "))/10000
    if pininput == pin:
        print("Płatność zrealizowana")
        break
    i -= 1
    if i == 2:
        print(f"Wprowadzony kod PIN niepoprawny. Zostało {i} próby.")
    if i == 1:
        print(f"Wprowadzony kod PIN niepoprawny. Zostało {i} próba.")
    if i == 0:
        print("Przepraszamy, twoja karta została zablokowana.")
    