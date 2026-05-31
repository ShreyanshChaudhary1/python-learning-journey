# ===== FUNCTIONS =====

# Basic function
def first_func():
    print("Hello student")   # body

first_func()   # call karo

# Parameters aur return
def add(a, b):
    sum = a + b
    return sum   # value wapas bhejo

print(add(10, 20))   # 30

# ===== SCOPE =====

# Global variable - function ke bahar
x = 101

def funk():
    x = 106      # local scope - sirf function ke andar
    print(x)     # 106

funk()
print(x)         # 101 - global wala

# ===== TYPES OF ARGUMENTS =====

# Default argument
def greet(name, message="Good funk"):
    print(name, message)

greet("Vishal", "Hello")   # Vishal Hello
greet("Vishal")            # Vishal Good funk - default use hoga

# Keyword argument - naam se value do
def greet2(name, age, message):
    print(message, name, "your age", age)

greet2(name="Vishal", age=99, message="Hello")   # order matter nahi

# Positional argument - order matter karta hai
def add2(x, y):
    print("x", x)
    print("y", y)
    print(x + y)

add2(5, 6)   # x=5, y=6

# *args - multiple values le sakta hai - tuple mein store hota hai
def sum_all(*args):
    print(type(args))   # tuple
    print(args)
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all(1, 2, 3, 9, 5))   # 20

# *args with fixed params - fixed pehle, baaki args mein
def fn(a, b, *args):
    print(a)        # 5
    print(b)        # 6
    print(args)     # (7, 8, 9) tuple
    print(*args)    # 7 8 9 unpacked

fn(5, 6, 7, 8, 9)

# **kwargs - keyword arguments - dict mein store hota hai
def display_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, "->", value)

display_info(name="Shreyansh", age=18, city="Bangl")

# Mix of all - a, b fixed, *args tuple, **kwargs dict
def func(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(5, 6, 7, 8, 9, name="Shreyansh", age=18)

# Return type hint - sirf suggestion hai, enforce nahi karta
def add3(a: int, b: int) -> int:
    return a + b

print(add3(5, 7))      # 12
print(add3(5.5, 7.6))  # 13.1 - float bhi chalega

# Function nesting - function ke andar function
def outer():
    print("Hello from the outer")
    def inner():
        print("Hello from the inner")
    return inner   # inner function return karo

fn = outer()    # Hello from the outer
fn()            # Hello from the inner
outer()()       # dono ek saath
