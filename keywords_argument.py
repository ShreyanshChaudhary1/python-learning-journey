# keyword argument = naam se value do
# order matter nahi karta position argument ma 

def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet(last_name="Chaudhary", first_name="Shreyansh")  # naam se specify karo
print("Finish")

# agar dono missing ho to error
# position argument na ho to keyword use karo