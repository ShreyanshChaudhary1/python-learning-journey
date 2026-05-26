# ===== OPERATORS IN PYTHON =====

# 1. Arithmetic - result always float ya int
num1 = 10
num2 = 20
print(num1 + num2)   # 30
print(num1 - num2)   # -10
print(num1 * num2)   # 200
print(num1 / num2)   # 0.5 float
print(num1 // num2)  # 0 floor div
print(num1 % num2)   # 10 remainder
print(num1 ** 2)     # 100 power

# 2. Comparison - result T/F
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 < num2)   # True
print(num1 > num2)   # False

# 3. Assignment operators
x = 5
x += 5   # x = x + 5 = 10
x -= 5   # x = x - 5 = 5
x *= 5   # x = x * 5 = 25
x /= 5   # x = x / 5 = 5.0
x //= 5  # floor div
x %= 5   # remainder
x **= 5  # power

# 4. Logical operators
# and - dono true hone chahiye
# or  - ek bhi true ho toh true
# not - ulta kar do
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# XOR - ^ - different hone pe True
print(True ^ False)   # True
print(True ^ True)    # False

# 5. Infinity and NaN
pos_inf = float("inf")   # +infinity
neg_inf = float("-inf")  # -infinity
nan = float("nan")       # NaN - not a number
print(pos_inf)           # inf
print(neg_inf)           # -inf
# nan is always != to any number
