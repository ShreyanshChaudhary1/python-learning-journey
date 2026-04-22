p# mini project - weight convert karo kg <-> lbs
weight = float(input("Enter weight: "))
unit = input("kg or lbs?: ")

if unit == "kg":
    result = weight * 2.205   # kg to lbs formula
    print(f"{weight}kg = {result:.2f}lbs")
else:
    result = weight / 2.205   # lbs to kg
    print(f"{weight}lbs = {result:.2f}kg")
# .2f = 2 decimal places
