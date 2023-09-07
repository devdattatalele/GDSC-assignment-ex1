input = input("Enter a string: ")

input_string = input.replace(" ", "").lower()

if input_string == input_string[::-1]:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
