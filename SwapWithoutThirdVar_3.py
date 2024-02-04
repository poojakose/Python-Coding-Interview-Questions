x = 10
y = 20

print("Before Swap :", x, y)

x = x ^ y # 10 ^ 20 = 30
y = x ^ y # 30 ^ 20 = 10
x = x ^ y # 30 ^ 10 = 20

print("After Swap :", x, y)