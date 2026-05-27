# ===== CONDITIONS =====

# Truthy Value - non empty sequence ya non zero = True
# Falsy Value - empty sequence ya zero = False

# if, else, elif
y = int(input("Number: "))
if y > 15:
    print("Number is greater than 15")
elif y == 15:
    print("Number is = 15")
else:
    print("Number is smaller than 15")

# Nested conditions
x = 19
if x > 5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is less than 5")

# Ternary operator - short condition
num = 5
result = "Positive" if num >= 0 else "Negative"
print("Number is", result)

# Match and case - switch statement jaisa
# ek condition match hone pe automatically break
day_num = 5
match day_num:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Invalid day number")
