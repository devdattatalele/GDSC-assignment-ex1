num1 = 0
num2 = 0
for l in range(0,10):
    Sum = num1 + num2
    print("New number", num1)
    print("Previous number", num2)
    print("Sum:", Sum)

    num2 = num1
    num1 = num1 + 1