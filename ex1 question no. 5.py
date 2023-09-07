input = input("Enter a list of numbers: ")#.split(',')

if input:
    if input[0] == input[-1]:
        print("True")
    else:
        print("False")
