#Create a list of numbers and print all elements using a loop.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
for i in list:
    print(i)"""
#Find the sum of all elements in a list.

"""num = int(input("enter a value for range of list = "))
list = []
sum = 0
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
for i in list:
    sum = sum+i
print(sum)"""

#Find the largest number in a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)

largest = list[0]

for i in list:
    if i > largest:
        largest = i

print(largest)
print(max(list))  """

#Find the smallest number in a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)

smallest = list[0]

for i in list:
    if i < smallest:
        smallest = i

print(smallest)
print(min(list))"""

#Count the total even numbers in a list.
"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
check_list = []

for i in list:
    if i%2==0:
        check_list.append(i)
print(check_list)"""

#Count the total odd numbers in a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
check_list = []

for i in list:
    if i%2!=0:
        check_list.append(i)
print(check_list)
"""

#Print all positive numbers from a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
check_positive = []

for i in list:
    if i > 0:
        check_positive.append(i)
print(check_positive)"""

#Print all negative numbers from a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
check_negative = []

for i in list:
    if i < 0:
        check_negative.append(i)
print(check_negative)"""

#Find the average of numbers in a list.

"""num = int(input("enter a value for range of list = "))
list = []
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
sum_of_list = 0

for i in range(len(list)):
    sum_of_list= sum_of_list+i
print(sum_of_list)
list_of_lenght = len(list)

find_average_of_list = sum_of_list / list_of_lenght

print(find_average_of_list)
"""

#Print numbers greater than 10 from a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a value of list_item value = "))
    list.append(list_item)
print(list)
new_list = []
for i in list:
    if i > 10:
        new_list.append(i)
print(new_list)"""
