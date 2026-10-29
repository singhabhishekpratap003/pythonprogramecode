#Reverse a list using loop.

"""list = []
num = int(input("emter a value of range of list = "))

for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
rev_list = []
for i in range(len(list)-1,-1,-1):
    rev_list.append(i)
print(rev_list)
print(type(list))"""
  
#Print the square of each element in a list.

"""list = []
num = int(input("emter a value of range of list = "))

for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)

square_list = []
for i in list:
    square_list.append(i**2)

print(square_list)"""

#Create a new list containing double of each element.

"""list = []
num = int(input("emter a value of range of list = "))

for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)

new_list = []

for i in list:
    new_list.append(i*2)
print(new_list)"""

#Count how many times a specific element appears in a list.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
num2 = int(input("enter a value for check the uccurences = "))
new_list = []
count = 0
for i in list:
    if i==num2:
        new_list.append(i)
        count = count+1
print(new_list)
print("total number of element that appear in list = ",count)"""

#Find the second largest number in a list.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
max_in_list = max(list)
secend_largest_element = 0
for i in list:
    if i != max_in_list and i > secend_largest_element:
        secend_largest_element = i
print(secend_largest_element)"""

#Remove duplicate elements from a list.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
"""

#Merge two lists into one list.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
list1 = []
num1 = int(input("emter a value of range of list = "))
for i in range(num1):
    list_item1 = int(input("enter a list item value = "))
    list1.append(list_item1)
merge_list = []
for i in list:
    merge_list.append(i)
for i in list1:
    merge_list.append(i)
print(merge_list)"""

#Find common elements between two lists.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
list1 = []
num1 = int(input("emter a value of range of list = "))
for i in range(num1):
    list_item1 = int(input("enter a list item value = "))
    list1.append(list_item1)
common_list = []
for i in list:
    if i in list1:
        common_list.append(i)
print(common_list)
"""

#Check whether a list is palindrome or not.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
new_list = []
for i in range(len(list)-1,-1,-1):
    new_list.append(list[i])
print(new_list)
if list == new_list:
    print("this list is pollindromne")
else:
    print("not pollindrome")"""

#Sort a list in ascending order.

"""list = []
num = int(input("emter a value of range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print("Sorted list:", list)
"""
