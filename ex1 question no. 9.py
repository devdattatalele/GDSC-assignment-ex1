list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
resultlist = []

for num in list1:
    if num % 2 != 0:
        resultlist.append(num)

for num in list2:
    if num % 2 == 0:
        resultlist.append(num)

print("Result List:", resultlist)