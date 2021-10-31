wzrost = float(input("Wprowadź wzrost w CM: "))

masa = float(input("Wprowadź masę w KG: "))

bmi = masa/((wzrost/100)**2)

print(f"Twoje BMI to: {round(bmi, 2)}")