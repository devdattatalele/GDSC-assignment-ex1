num = int(input("Enter a number: "))

strnum = str(num)

reversestr = strnum[::-1]

if strnum == reversestr:
    print((num)," is a palindrome number.")
else:
    print((num)," is not a palindrome number.")