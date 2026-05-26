# Identity Operator - is / is not
# Check karta hai same memory location pe hai ya nahi

x = 5
y = 5
print(x is y)        # True - same memory

a1 = [1, 2, 3]
a2 = [1, 2, 3]
print(a1 is a2)      # False - list alag memory mein store hoti hai
print(a1 is not a2)  # True

# Membership Operator - in / not in
# Check karta hai value list mein hai ya nahi
list = [1, 2, 3, 4]
print(4 in list)      # True
print(5 in list)      # False
print(4 not in list)  # False
print(5 not in list)  # True

# Float precision issue - binary mein
# 0.3 binary mein exactly represent nahi hota - repeating hai
print(1 - 4 * 0.25)        # 0.0 - sahi
print(0.9 - 3 * 0.3)       # 1.110...e-16 - should be 0 but floating point error
