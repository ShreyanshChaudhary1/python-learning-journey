# Bitwise - numbers ko binary mein convert karke compare karta hai

num1 = 5   # binary = 101
num2 = 3   # binary = 011

# AND & - dono 1 hone pe 1
print(num1 & num2)   # 001 = 1

# OR | - ek bhi 1 hone pe 1
print(num1 | num2)   # 111 = 7

# XOR ^ - different hone pe 1
print(num1 ^ num2)   # 110 = 6

# Left shift << - value double hoti hai
num = 5              # 101
print(num << 1)      # 1010 = 10 (double)

# Right shift >> - value half hoti hai
num1 = 14            # 1110
print(num1 >> 1)     # 0111 = 7 (half)
