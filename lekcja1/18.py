cm = int(input("Podaj wzrost w cm: "))

ft = cm / 30.48

ft_1 = int(ft)

inches = (ft-ft_1)*10

print(f"I am {cm} cm tall, i.e. {ft_1} feet and {round(inches, 1)} in")