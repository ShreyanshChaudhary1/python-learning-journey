# and, or, not - multiple conditions ek saath
x = input('your name: ')
a = len(x)

# and = dono true hone chahiye
if a < 3 and a > 10:
    print('name 3 to 50 chars hona chahiye')
else:
    print(f'thanks {x}')