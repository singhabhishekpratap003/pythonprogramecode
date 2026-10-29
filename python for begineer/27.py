# Create a set and print it

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)"""


# Add an element to a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
num1 = int(input("enter a range of add set element = "))
while num1 > 0:
    element_add = int(input("enter a add element for set = "))
    set_.add(element_add)
    num1=num1-1
print(set_)
"""

# Add multiple elements using update()

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
list = []
num1 = int(input("enter a range or add miltiple elements = "))
while num1 > 0:
    element_add = int(input("enter a value for the add element = "))
    list.append(element_add)
    num1-=1
print(list)
set_.update(set(list))
print(set_)
"""

# Remove an element using remove()

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
num1 = int(input("enter a value for the remove from set = "))
set_.remove(num1)
print(set_)
"""

# Remove an element using discard()

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
num1 = int(input("enter ba value for remove element from the set using discard = "))
set_.discard(num1)
print(set_)"""


# Remove a random element using pop()

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
print(set_.pop())
"""

# Clear all elements from a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set_.clear()
print(set_)
"""

# Find the length of a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
count = 0
for i in set_:
    count = count+1
print(count)
print(len(set_))
"""

# Check if element exists in a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
num1 = int(input("enter a value for check exixts in set or not = "))
for i in set_:
    if num1 == i:
        print("exists in set")
     
if num1 in set_:
    print("yes")
else:
    print("not")
"""

# Print all elements using loop

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
for i in set_:
    print(i)
"""

# Create two sets and print them

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
"""

# Find union of two sets

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
result1 = set_.union(set1_)
print(result1)
result2 = set1_ | set_
print(result2)
"""

# Find intersection of two sets

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
result = set()
for i in set1_:
    for j in set_:
        if i == j:
            result.add(i)
print(result)
print(set_.intersection(set1_))
"""

# Find difference of two sets

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
result = set()
for i in set_:
    if i not in set1_:
            result.add(i)
print(result)
result1 = set_.difference(set1_)
print(result1)
"""

# Find symmetric difference

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
result = set()
for i in set_:
    if i not in set1_:
            result.add(i)
for j in set1_:
    if j not in set_:
            result.add(j)
print(result)
result1 = set_.symmetric_difference(set1_)
print(result1)
"""

# Check if one set is subset of another

"""set_ = set()
num = int(input("enter a range of set = "))
for i in range(num):
    set_item = int(input("enter avalue for set = "))
    set_.add(set_item)
set1 = set()
num1 = int(input("enter a range of set2 = "))
while num1 > 0:
    set_item1 = int(input(" enter a value of set2 = "))
    set1.add(set_item1)
    num1-=1
if set_[i] in set1: print("set is subset")
else: print("set is not subset")
print(set_.issubset(set1))
"""

# Check if one set is superset of another

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
flag = True
for i in set1_:
    if i not in set_:
        flag = False
        break
print(flag)
print(set_.issuperset(set1_))
"""

# Count total even numbers in a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
count = 0
for i in set_:
    if i%2==0:
        count = count+1
print(count)
"""

# Count total odd numbers in a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
count = 0
for i in set_:
    if i%2!=0:
        count = count+1
print(count)
"""

# Find maximum element in a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
maximum = 0
for i in set_:
    if i > maximum:
        maximum = i
print(maximum)
"""

# Find minimum element in a set

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
minimum = list(set_)[0]
for i in set_:
    if i < minimum:
        minimum = i
print(minimum)
print(min(set_))
"""

# Find sum of all elements

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
sum = 0
for i in set_:
    sum = sum + i
print(sum)
"""

# Find average of elements

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
sum = 0
count = 0
for i in set_:
    sum = sum + i
    count = count+1
avera = sum / count
print(avera)
"""

# Remove duplicate elements from list using set()

"""list = []
num = int(input("enter a range of list ="))
while num > 0:
    list_item = int(input("enter a value for the list =  "))
    list.append(list_item)
    num-=1
print(list)
set_ = set()
for i in list:
    for j in list:
        if i != j:
            set_.add(i)
print(set_)
print(set(list))
"""

# Convert list to set

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a value for the list = "))
    list.append(list_item)
print(list)
set_ = set()
for i in list:
    set_.add(i)
print(set_)
"""

# Convert set to list

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
list = []
for i in set_:
    list.append(i)
print(list)
"""

# Create a set of squares

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
for i in set_:
    set1_.add(i**2)
print(set1_)
"""

# Find common elements between two sets

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
set2 = set()
for i in  set_:
    for j in set1_:
        if i == j:
            set2.add(i)
print(set2)
print(set_.intersection(set1_))
"""

# Check if two sets are equal

"""set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
if set_ == set1_: print("these set are equal")
else: print("these set are not equal")
"""

# Find elements present in one set but not in another

set_ = set()
num = int(input("enter a range of set = "))
while num > 0:
    set_item = int(input("enter a value for the set = "))
    set_.add(set_item)
    num=num-1
print(set_)
set1_ = set()
num1 = int(input("enter a range of set = "))
while num1 > 0:
    set_item1 = int(input("enter a value for the set = "))
    set1_.add(set_item1)
    num1=num1-1
print(set1_)
check_element = int(input("enter a value for check the element = "))
if check_element in set_: print("this elemnt are present in set 1")
else: print("these elemnt are present in set 2")
 