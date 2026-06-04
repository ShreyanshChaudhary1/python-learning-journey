# ============================================
# SHREYANSH CHAUDHARY - PYTHON PRACTICE SET 1
# PW Skills - Decode Python with DSA
# GitHub: ShreyanshChaudhary1
# ============================================


# ===== DATA TYPES =====

# Q1
a = input('Enter name: ')
b = int(input('Enter age: '))
c = input('Enter city: ')
print(a, end=' | ')
print(b, end=' | ')
print(c)

# Q2
print(a[0:3])

# Q3
x = 10
y = 10
print(id(x))
print(id(y))
# Same address aata hai kyunki Python small integers
# cache karta hai efficiency ke liye

# Q4
print(5e7)  # 5 crore

# Q5
print(type(5), '= int')
print(type(5.0), '= float')
print(type('5'), '= string')
print(type(True), '= bool')
print(type([5]), '= list')
print(type((5,)), '= tuple')
print(type(5+5j), '= complex')

# Q6
r = int(input('Number 1: '))
t = int(input('Number 2: '))
print('Add:', r + t)
print('Sub:', r - t)
print('Div:', r / t)
print('Floor div:', r // t)
print('Mul:', r * t)
print('Mod:', r % t)
print('Power:', r ** t)

# Q7
y = '100'
print(int(y) + 50)


# ===== STRINGS =====

# Q1
u = input('Write anything: ')
print(u[::-1])

# Q2
i = 'shreyansh'
print(i.count('a'))

# Q3
o = input('Input any sentence: ')
print(o.replace(' ', '\n'))

# Q4
p = input('Input string to check palindrome: ')
if p == p[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')

# Q5
q = input('Input name: ')
v = len(q)
print(f'Hello {q} your name has {v} characters')

# Q6
s = input('Sentence or word: ')
print(s.upper())
print(s.lower())
print(s.capitalize())

# Q7
d = input('Input a sentence: ')
print(d.replace(' ', ''))

# Q8
f = input('Input a sentence: ')
print(f.replace('a', '@'))


# ===== TUPLES =====

# Q1
g = ('lok', 'basti', 'pryag', 'pagwaea', 'katara')
print(g[1], g[4])

# Q2
h = ['s', 'd', 'f', 'g', 'l']
print(type(tuple(h)))

# Q3
j = (1, 5, 3, 5, 7, 5, 2, 5)
print(j.count(5))

# Q4
k = ('lok', 'basti', 'pryag', 'pagwaea', 'katara', 'del')
print(k.index('del'))

# Q5
l = (10, 20, 30)
z = l[0]
n = l[1]
c = l[2]
print(z + n + c)

# Q6 - FIXED
# Tuple already hai - bas print karo
bb = (2, 4, 6, 8, 10)
print(bb)

# Q7 - FIXED
# + se directly tuples merge hote hain
cc = (1, 2, 3)
dd = (4, 5, 6)
ee = cc + dd
print(ee)
print(type(ee))


# ===== DICTIONARY =====

# Q1
ff = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
print(ff)

# Q2 - FIXED
gg = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
gg.update({'github': 'ShreyanshChaudhary1'})
print(gg)

# Q3 - FIXED (values() add kiya)
hh = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
print(hh.keys())
print(hh.values())
print(hh.items())

# Q4
ii = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
ll = ii.pop('age')
print(ll)
del ii['city']
print(ii)

# Q5
jj = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
kk = {'class': 'B Tech', 'height': '182cm'}
jj.update(kk)
print(jj)

# Q6
kk = {'name': 'Shreyansh', 'age': '18', 'city': 'Basti', 'course': 'PW Skills'}
print('name' in kk)

# Q7
# zip() - do lists ko pair karta hai
# zip(["a","b"], [1,2]) = [("a",1), ("b",2)]
# dict() se dictionary ban jaati hai
keys = ["a", "b", "c"]
values = [1, 2, 3]
nn = dict(zip(keys, values))
print(nn)

# Q8
# Topper dhundna - highest marks wala
ll = {'mikku': 31, 'addi': 22, 'rag': 66, 'mee': 88}
max_marks = list(ll.values())
max_marks.sort()
highest = max_marks[-1]  # last = highest
print('Highest marks:', highest)
for key, value in ll.items():
    if value == highest:
        print('Topper:', key)
