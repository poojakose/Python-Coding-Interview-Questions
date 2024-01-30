# Swap two variables using Multiplication and Division Operator
x = 10
y = 30

print("Before Swap :", x, y)

x = x * y # 10 * 30 = 300
y = x / y # 300 / 30 = 10
x = x / y # 300 / 10 = 30

#print("After Swap :", x, y)

print("After Swap int :", int(x), int(y))
