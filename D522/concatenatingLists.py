# Concatenating Lists
# Lists can be concatenated using the + operator or the extend() method

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2

print(concatenated_list)

# Using the extend method, this actually modifies the original list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)  # List1 is now holding everything

print(list1)


