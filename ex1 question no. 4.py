
inputword = input("Enter a word: ")
chars_to_be_remove = int(input("Enter the number of characters to remove: "))

if chars_to_be_remove >= len(inputword):
    print("n must be less than the length of the string.")

newword = ""
for i in range(chars_to_be_remove, len(inputword)):
     newword = newword + inputword[i]

print("New string.:", newword)
