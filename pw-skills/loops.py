# ===== LOOPS =====

# While loop - jab tak condition true hai
num = 10
while num > 0:
    print("Hello")
    num -= 1        # 10 times print hoga

# For loop - list iterate karna
frutes = ["apple", "banana", "cherry", "date"]
for i in frutes:
    print(i)        # har fruit print hoga

# For loop - string iterate karna
name = "Shreyansh"
for ch in name:
    print(ch, end=" ")   # S h r e y a n s h

# Range function
for i in range(5):          # 0 to 4
    print(i)

for i in range(2, 7):       # 2 to 6
    print(i)

for i in range(2, 10, 2):   # 2,4,6,8 - step 2
    print(i)

# Reverse range
for i in range(10, 0, -1):  # 10 to 1
    print(i)

for i in range(12, 0, -3):  # 12,9,6,3
    print(i)
