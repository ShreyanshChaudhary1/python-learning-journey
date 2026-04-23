# parameters = variable storage
# jab call karo tab value  ra ga (argument)

def greet(name):
    print(f'Hi {name}!')
    print('Welcome aboard')

print("Start")
greet("Shreyansh")   # Shreyansh = argument
print("Finish")
greet("Chaudhary")

# 2 ya zyada parameters bhi ho sakte hai
def greet2(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet2("Shreyansh", "Chaudhary")  # error if 2 values nahi diye
print("Finish")