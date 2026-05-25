# Dictionary - key:value pairs
# unordered, mutable, keys unique hone chahiye

student = {'name': 'Shreyansh', 'age': '18', 'city': 'Prayagraj'}

# access
print(student['age'])      # 18 - value by key
print(student['city'])     # Prayagraj

# all keys
print(student.keys())      # ['name', 'age', 'city']

# all values
print(student.values())    # ['Shreyansh', '18', 'Prayagraj']

# all items
print(student.items())     # list of all key:value pairs

# add element
student['country'] = 'India'
print(student)

# update - dusri dict merge karo
ddict = {'country': 'India'}
student.update(ddict)

# remove element
a = student.popitem()      # last item remove karo
print(student.popitem())

del student['name']        # specific key delete

student.clear()            # empty dict
