# Create a tuple and print it

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
"""

# Access first element

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
for i in tup:
    print(i)
    break
print(tup[0])
"""

# Access last element

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
for i in range(len(tup)-1,-1,-1):
    print(tup[i])
    break
print(tup[-1])
"""

# Find length of tuple

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
count = 0
for i in tup:
    count+=1
print(count)
print(len(tup))
"""

# Check element exists in tuple

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for tuple = "))
    tup+=(t,)
print(tup)
element_exits = int(input("enter a value for check thevalue in  tuple = "))
if element_exits in tup:
    print("this value exits in tuple")
else:
    print("this value not exists in tuple")
 """   

# Count occurrences using count()

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
count = 0
occu_num = int(input("enter a value for check the occurences = "))
for i in tup:
    if i == occu_num:
        count+=1
print(count)
"""

# Find index using index()

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
print(tup.index(5))
target = int(input("enter a value for find index = "))
index = 0 
for i in tup:
    if i == target:
        print("index : ",index)
        break
    index+=1
"""

# Convert tuple to list

"""tup = ()
num = int(input("enter a range of tup = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
print(type(tup))
li = []
for i in tup:
    li.append(i)
print(li)
print(type(li))
"""

# Convert list to tuple

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
tup = ()
for i in list:
    tup+=(i,)
print(tup)
print(type(tup))
"""

# Print elements using loop

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
for i in  tup:
    print(i)
"""

# Find maximum element

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
max_tup = 0
for i in tup:
    if i > max_tup:
        max_tup = i
print(max_tup)
"""

# Find minimum element

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for tuple = "))
    tup+=(t,)
print(tup)
min_tup = tup[0]
for i in tup:
    if i < min_tup:
        min_tup = i
print(min_tup)
"""

# Find sum of elements

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
sum = 0
for i in tup:
    sum = sum + i
print(sum)
"""

# Find average of elements

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
sum = 0
count = 0
for i in range(len(tup)):
    sum = sum + tup[i]
    count = count+1
print(sum)
print(count)
ave = sum /count
print(ave)
"""

# Count even numbers()

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
even_count = 0
for i in tup:
    if i%2==0:
        even_count = even_count+1
print(even_count)
"""

# Count odd numbers

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("ente4r a value for the tuple = "))
    tup+=(t,)
print(tup)
odd_count = 0
for i in tup:
    if i%2!=0:
        odd_count = odd_count+1
print(odd_count)
"""

# Create tuple of squares

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
squ_tup = ()
for i in tup:
    squ_tup+=(i**2,)
print(squ_tup)
"""

# Merge two tuples

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
tup1 = ()
num1 = int(input("enter a range of tuple = "))
for i in range(num1):
    t1 = int(input("enter a value for the tuple = "))
    tup1+=(t1,)
print(tup)
print(tup1)
tup2 = tup 
for i in tup1:
    tup2+=(i,)
print(tup2)
"""

# Repeat tuple

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
repeat_tuple = ()
num1 = int(input("enter a range for repeat the tuple = "))
for i in range(num1):
    repeat_tuple+=tup
print(repeat_tuple)
"""

# Slice first 3 elements

"""tup = ()

num = int(input("enter a range of tuple = "))

for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup += (t,)

print("Original tuple =", tup)

# slice first 3 elements
slice_tuple = tup[:3]

print("First 3 elements =", slice_tuple)"""


# Remove duplicates

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
new_tup = ()
for i in tup:
    if i not in new_tup:
        new_tup+=(i,)
print(new_tup)
"""

# Find second largest element

"""tup = ()
num = int(input("enter a ranghe of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
li = list(tup)
print(list)
maximum_list = max(li)
secend_maximum = 0
for i in li:
    if i < maximum_list and i > secend_maximum:
        secend_maximum = i
print(secend_maximum)
"""

# Sort tuple elements

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tule = "))
    tup+=(t,)
print(tup)
list = list(tup)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i] , list[j] = list[j] , list[i]
print(list)
print(sorted(tup))
print(tuple(list))
"""

# Reverse tuple

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
rev_tuple = ()
for i in range(len(tup)-1,-1,-1):
    rev_tuple+=(tup[i],)
print(rev_tuple)"""

# Check tuple is palindrome

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
rev_tuple = ()
for i in range(len(tup)-1,-1,-1):
    rev_tuple+=(tup[i],)
print(rev_tuple)
if tup == rev_tuple:
    print("tuple is polindrome")
else:
    print("not polindrome")
"""

# Find common elements

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
common_tup_ele = ()
for i in range(len(tup)):
    for j in range(i+1,len(tup)):
        if tup[i] == tup[j]:
            common_tup_ele+=(tup[i],)
print(common_tup_ele)
"""

# Unpack tuple


# Create tuple of even numbers

"""tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    if t%2==0:
        tup+=(t,)
print("even tuple = ", tup)
"""

# Count frequency of elements

"""tup = ()
num = int(input("enter a range of list = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
count = 0
for i in range(len(tup)):
    count+=1
print(count)
"""

# Convert tuple to dictionary

tup = ()
num = int(input("enter a range of tuple = "))
for i in range(num):
    t = int(input("enter a value for the tuple = "))
    tup+=(t,)
print(tup)
dict = {}
for i in range(len(tup)):
    dict[i] = tup[i]
print(dict)