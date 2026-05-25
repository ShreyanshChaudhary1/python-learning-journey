# Tuple - immutable, any data type contain kar sakta hai
tup1 = (3, 6, 1, 9, 0)

# list to tuple
t1 = tuple([1, 2, 3])

# string to tuple
t2 = tuple("Shr")

# single element tuple - comma zaruri hai
t3 = tuple("9,")  # bina comma int ban jaata

# tuple methods
frute = ('A', 'B', 'C', 'B', 'A', 'C', 'A')
print(frute.count('A'))   # count elements = 3
print(frute.index('B'))   # find index = 1
print(len(frute))         # length = 7
print(frute[1])           # index access = B
