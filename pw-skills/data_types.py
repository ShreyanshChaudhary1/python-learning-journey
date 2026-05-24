# PW Skills - Decode Python with DSA
# Topic: Data Types and print() basics

# id() - variable ka memory address deta hai
x = 10
print(id(x))

# print() - sep and end parameters
a, b, c = 1, 2, 3
print(a, b, c, sep=",")     # comma se separate
print("H", end=" ")          # same line pe print
print("W", end=" ")
print("!")                   # H W !

# Data Types
# Numerical
num1 = 5        # int
num2 = 2.5      # float
num3 = 4 + 5j   # complex number

# Scientific notation
num = 3e6       # 3 x 10^6 = 3000000.0
print(num)

# Built-in math functions
print(abs(-5))      # always positive = 5
print(pow(2, 3))    # 2^3 = 8
print(round(4.75))  # round off = 5
