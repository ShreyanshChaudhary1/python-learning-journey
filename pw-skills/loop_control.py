# ===== LOOP CONTROL =====

# break - loop se bahar niklo
for num in range(1, 13):
    if num % 4 == 0:
        break           # 4 print nahi hoga
    print(num)          # 1, 2, 3

# continue - current iteration skip karo
# agle iteration pe jao
for i in range(11):
    if i % 2 != 0:
        continue        # odd skip
    print(i)            # 0,2,4,6,8,10

# Nested loop with break
for i in range(4):
    for j in range(1, 13):
        if j % 4 == 0:
            break
        print(j)

# Nested loop with continue
for i in range(4):
    for j in range(1, 13):
        if j % 2 != 0:
            continue    # odd skip
        print(j)        # even numbers only
