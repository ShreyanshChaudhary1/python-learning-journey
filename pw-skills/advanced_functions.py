# ===== PASS BY VALUE vs PASS BY REFERENCE =====

# Pass by Value - immutable data types pe apply hota hai
# Numbers, Strings, Tuples - copy bhejta hai
num = 5
def modify(num):
    num += 1
    print(num)   # 6 - local copy change hui

modify(num)
print("Original num", num)   # 5 - original same rahega

# Pass by Reference - mutable data types pe apply hota hai
# List, Dictionary, Set - original change ho jaata hai
list = [1, 2, 4]
def list1(li):
    li.append(5)   # original list mein add ho jaata hai
    print(li)

print("Before calling f", list)    # [1, 2, 4]
list1(list)                        # [1, 2, 4, 5]
print("After calling f", list)     # [1, 2, 4, 5] - original change!

# ===== LAMBDA FUNCTION =====
# Anonymous function - koi naam nahi
# Sirf ek expression allowed hai body mein
# Syntax: lambda parameter : expression

# Single parameter
func = lambda x: x + 10
print(func(5))   # 15

# Multiple parameters
add = lambda a, b: a + b
print(add(5, 6))   # 11

# Lambda returning lambda - nested
def myfunc():
    # naya function return karo
    return lambda msg: print(msg)

myfunc()("Hello word")   # Hello word
# 2 bracket
