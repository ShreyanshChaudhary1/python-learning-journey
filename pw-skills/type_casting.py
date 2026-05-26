# Type Casting - ek type se doosre mein convert karo

# Implicit - Python khud convert karta hai
x = 5       # int
y = 6.5     # float
result = x + y
print(result)        # 11.5 float - auto convert

# Explicit - hum manually convert karte hain
y = '10'             # string
print(type(y))       # str
ind = int(y)         # string to int
print(ind)           # 10
print(type(ind))     # int

# Frozen Set - immutable set
# dictionary mein key banana ke liye use hota hai
f = frozenset([1, 2, 3])
print(f)             # frozenset({1, 2, 3})

f2 = frozenset({1, 2, 3})
print(f2)

# frozenset as dictionary key
dict = {f2: "VS"}
print(dict)          # {frozenset({1, 2, 3}): 'VS'}
