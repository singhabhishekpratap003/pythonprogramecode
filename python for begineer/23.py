#Write a Python program to create a list and print its elements.

"""my_list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    my_list.append(list_item)
print(my_list)"""

#Write a program to find the length of a list without using len().

"""my_list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    my_list.append(list_item)
print(my_list)
cout = 0
for i in my_list:
    cout = cout + 1
print(cout)"""

#Write a program to find the largest element in a list.

"""my_list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    my_list.append(list_item)
print(my_list)
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
print(largest)"""

#Write a program to find the smallest element in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
smallest = list[0]
for i in list:
    if i < smallest:
        smallest = i
print(smallest)"""

#Write a program to calculate the sum of all elements in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
sum_of_list_elements = 0
for i in list:
    sum_of_list_elements = sum_of_list_elements+i
print(sum_of_list_elements)"""

#Write a program to calculate the average of elements in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
count = 0
sum = 0
for i in list:
    sum = sum + i
    count = count + 1
average = sum / count
print(average)
"""

#Write a program to count how many even numbers are in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
even_no_list = []
for i in list:
    if i%2==0:
        even_no_list.append(i)
print(even_no_list)
"""

#Write a program to count how many odd numbers are in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
odd_no_list = []
for i in list:
    if i%2!=0:
        odd_no_list.append(i)
print(odd_no_list)
"""

#Write a program to print all positive numbers in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
possitive_number_list = []
for i in list:
    if i > 0:
        possitive_number_list.append(i)
print(possitive_number_list)
"""

#Write a program to print all negative numbers in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
negative_number_list = []
for i in list:
    if i < 0:
        negative_number_list.append(i)
print(negative_number_list)
"""

#Write a program to find the second largest number in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
largest = list[0]
secend_largest = list[0]
for i in list:
    if i > largest:
        secend_largest = largest
        largest = i
    elif i < largest and i > secend_largest:
        secend_largest = i
print(secend_largest)
"""

#Write a program to remove duplicate elements from a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
rem_dup = []
for i in list:
    if i not in rem_dup:
        rem_dup.append(i)
print(rem_dup)
"""      
                
#Write a program to reverse a list without using reverse().

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
rev_list = []
for i in range(len(list)-1,-1,-1):
    rev_list.append(list[i])
print(rev_list)
"""

#Write a program to check whether an element exists in a list or not.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
num1 = int(input("enter a value for check value esxits in list = "))
if num1 in list:
    print("exits in list")
else:
    print("not exits in list")
"""

#Write a program to count the occurrences of an element in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
num1 = int(input("enter a value to check occurences of value = "))
count = 0
for i in list:
    if i == num1:
        count = count + 1
print(count)
"""

#Write a program to find the index of a given element in a list.

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
num1 = int(input("enter a value for check index = "))
count = 0
for i in range(len(list)):
    if list[i] == num1:
        count = i
print(count)
"""

#Write a program to sort a list in ascending order without using sort().

"""lst = [5,2,8,1,3]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
"""

#Write a program to sort a list in descending order.

"""lst = [5,2,8,1,3]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)"""


#Write a program to merge two lists into one list.

"""list = []
num = int(input("enter a value for range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
list1 = []
num1 = int(input("enter a value for range of list = "))
for i in range(num1):
    list_item1 = int(input("enter a list item value = "))
    list1.append(list_item1)
print(list1)
merge_list = list+list1
print(merge_list)
"""

#Write a program to find the common elements between two lists.

"""list = []
num = int(input("enter a value for range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
list1 = []
num1 = int(input("enter a value for range of list = "))
for i in range(num1):
    list_item1 = int(input("enter a list item value = "))
    list1.append(list_item1)
print(list1)
common_list = []
for i in list:
    if i in list1:
        common_list.append(i)
print(common_list)
"""

#Write a program to split a list into two halves.

"""list = []
num = int(input("enter a value for range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
list1 = []
num1 = int(input("enter a value for range of list = "))
for i in range(num1):
    list_item1 = int(input("enter a list item value = "))
    list1.append(list_item1)
print(list1)"""

#Write a program to rotate a list to the right by 1 position.

"""lst = [1,2,3,4,5]

temp = lst[-1]

for i in range(len(lst)-1,0,-1):
    lst[i] = lst[i-1]

lst[0] = temp

print(lst)"""

#Write a program to rotate a list to the left by 1 position.

"""lst = [1,2,3,4,5]

temp = lst[0]

for i in range(0,len(lst)-1):
    lst[i] = lst[i+1]

lst[-1] = temp

print(lst)"""

#Write a program to find the maximum difference between two elements in a list.
"""
lst = [2,3,10,6,4,8,1]

min_val = lst[0]
max_diff = 0

for i in range(1,len(lst)):
    
    if lst[i] - min_val > max_diff:
        max_diff = lst[i] - min_val
        
    if lst[i] < min_val:
        min_val = lst[i]

print(max_diff)"""


#Write a program to remove all even numbers from a list.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
remove_even = []
for i in list:
    if i%2!=0:
        remove_even.append(i)
print(remove_even)
"""

#Write a program to replace all negative numbers with 0 in a list.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
for i in range(len(list)):
    if list[i] < 0:
        list[i] = 0
print(list)
"""

#Write a program to find the product of all elements in a list.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
product_of_list = 1
for i in list:
    product_of_list = i * product_of_list
print(product_of_list)
"""

#Write a program to create a new list containing squares of elements of another list.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
new_list_of_square = []
for i in list:
    num = i*i
    new_list_of_square.append(num)
print(new_list_of_square)
"""

#Write a program to find pairs of elements whose sum equals a given number.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
target = int(input("enter a target value = "))
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] + list[j] == 7:
            print((list[i],list[j]) , end=" ")
"""

#Write a program to check if a list is palindrome or not.

"""list = []
num = int(input("emter a number for the range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
rev_list = list[::-1]
print(list)
print(rev_list)
if list == rev_list:
    print("polindrome")
else:
    print("not polindrome")"""
