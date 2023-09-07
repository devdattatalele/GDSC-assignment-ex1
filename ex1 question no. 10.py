input = int(input("Enter a number: "))

num = str(input)

reversedstr = num[::-1]

for digit in reversedstr:
    print(digit, end=' ')
