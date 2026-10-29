#Create a list of 5 numbers and print the list.
"""list = []
num = int(input("enter a value of range for list = "))

for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)"""

#Create a list of 5 student names and print each name using a loop.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = input("entyer a list item value = ")
    list.append(list_item)
    
print(list)

for i in list:
    print(i)"""

#Print the first element of a list.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
print(list[0])"""

#Print the last element of a list.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
print(list[-1])"""

#Find the length of a list.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
print(len(list))"""

#Add a new element to a list using append().

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
new_item = list.append(45)
print(list)"""
#Insert an element at position 2 in a list.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
new_item = list.insert(2,45)
print(list)"""

#Remove an element from a list using remove().

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
new_item = list.remove(45)
print(list)
"""
#Remove the last element from a list.

"""list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)
new_item = list.pop()
print(list)
"""

#Check if a number exists in a list.

list = []
num = int(input("enter avalue of range of list = "))
for i in range(num):
    list_item = int(input("entyer a list item value = "))
    list.append(list_item)
    
print(list)

num = 45
if num in list:
    print("this value exits in list")
else:
    print("not exixts in list")