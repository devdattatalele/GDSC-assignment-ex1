input = input("Enter a list of numbers: ").split(',')

for numinput in input:
    divisiblenum = int(numinput)
    if divisiblenum % 5 == 0:
        print(divisiblenum)