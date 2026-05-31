# ===== PRACTICE PROBLEMS =====

# Q1: Sum of even numbers 1 to 20
sum = 0
for num in range(1, 21):
    if num % 2 == 0:
        sum += num
print("Sum of even numbers:", sum)   # 110

# Q2: Count vowels in a sentence
s = input("Enter a word to find vowels: ")
count = 0
for i in s:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print("No of vowels:", count)

# Q3: Fibonacci series
n = int(input("Enter n: "))
print(1, end=", ")
if n == 1:
    pass
else:
    print(1, end=", ")
    if n == 2:
        pass
    else:
        prev = 1
        prev1 = 1
        for num in range(3, n + 1):
            print(prev + prev1, end=", ")
            prev, prev1 = prev + prev1, prev

# Q4: Star pattern
# *
# * *
# * * *
# * * * *
for i in range(4):
    for j in range(i + 1):
        print("*", end=" ")
    print()
