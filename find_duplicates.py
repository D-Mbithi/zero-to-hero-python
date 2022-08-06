my_list = ['a', 'b', 'b', 'c', 'd', 'e', 'f', 'f']

duplicates = []

for char in my_list:
    if my_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)


print(duplicates)
