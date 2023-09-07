input = input("Enter the filename of the text file: ")
emptylist = {}

with open(input, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            cleaned_word = word.strip('.,!?").').lower()
            emptylist[cleaned_word] = emptylist.get(cleaned_word, 0) + 1

for word, count in sorted(emptylist.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
