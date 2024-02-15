d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 5, 'e': 6}

# update Method
d1.update(d2)
print(d1)

# unpack and merge operator
result = {**d1, **d2}
print(result)

# merge Operator
result = d1 | d2
print(result)

# update operator
d1 |= d2
print(d1)
