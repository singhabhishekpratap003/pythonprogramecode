# Create a dictionary and print it

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
"""

# Access value using key

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
print(dic["age"])"""

# Add new key-value pair

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
dic["add"] = "Raebareli"
print(dic)
"""

# Update value

"""
dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
dic["age"] = "26"
print(dic)"""

# Remove element using pop()

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
dic.pop("add")
print(dic)
"""

# Print all keys

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
print(dic.keys())
"""

# Print all values

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
print(dic.values())
"""

# Print all key-value pairs

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a value for key = ")
    value = input("enter a value for value = ")
    dic[key] = value
print("dictionary : " , dic)
print(dic.items())
for key in dic:
    print(key , ":" , dic[key])
"""

# Check if key exists

"""dic = {}
num = int(input("enter a range of the dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
print(dic)
print(dic.get("age"))
print(dic.get("add"))
if "name" in dic:
    print("exists")
else:
    print("none")
"""    

# Find length of dictionary

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
print(dic)
print(len(dic))
"""

# Iterate dictionary using loop

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
print(dic)
for key in dic:
    print({key , ":" , dic[key]} , end=",")
"""

# Count total keys

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
print(dic)
print(len(dic))
count = 0
for i in range(len(dic)):
    count = count+1
print(count)
"""

# Sum all values

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = int(input("enter a value = "))
    dic[key] = value
print(dic)
print(sum(dic.values()))
total = 0
for key in dic:
    total = total + dic[key]
print(total)
"""

# Find maximum value

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = int(input("enter a value = "))
    dic[key] = value
print(dic)
print(max(dic.values()))
max_val = list(dic.values())[0]
for key in dic:
    val = dic[key]
    if max_val < val:
        max_val = val
print(max_val)
"""

# Find minimum value

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
print(dic)
print(min(dic.values()))
min_val = list(dic.values())[0]
for key in dic:
    val = dic[key]
    if min_val > val:
        min_val = val
print(min_val)
"""

# Create dictionary from two lists

"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = input("enter a value for list item = ")
    list.append(list_item)
print(list)
list1 = []
num1 = int(input("enter a range of list = "))
for i in  range(num1):
    list_item1 = input("enter a list item value = ")
    list1.append(list_item1)
print(list1)
dic = dict(zip(list,list1))
print(dic)
dic1 = {}
for i in range(len(list)):
    dic1[list[i]] = list1[i]
print(dic1)
"""

# Merge two dictionaries

"""dic = {}
num = int(input("enter a value for the range of dict = "))
for i in range(num):
    key = input("enter a key = ")
    value = input("enter a value = ")
    dic[key] = value
dic1 = {}
num1 = int(input("enter a value for the range of dict = "))
for i in range(num1):
    key1 = input("enter a key = ")
    value1 = input("enter a value = ")
    dic1[key1] = value1
print(dic)
print(dic1)
print(dic.update(dic1))
new_dic1 = {}
for key in dic:
    new_dic1[key] = dic[key]
    for key in dic1:
        new_dic1[key] = dic1[key]
print(new_dic1)
"""

# Count frequency using dictionary

"""list = []
num = int(input("enter a range of list = "))
for i in  range(num):
    list_item = int(input("enter a list item value = "))
    list.append(list_item)
print(list)
freq = {}
for i in list:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
"""

# Create dictionary of squares

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    number = int(input("enter a number for creating square dict = "))
    key = number
    value = number * number
    dict[key] = value
print(dict)
"""

# Remove duplicate values

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    key = int(input("enter a value of key = "))
    value = int(input("eneter a value for value = "))
    dict[key]=value
print(dict)
rev_dup = {}
for k,v in dict.items():
    if v not in rev_dup.values():
        rev_dup[k] = v
print(rev_dup)
"""

# Sort dictionary by keys

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    key = int(input("enter a value for the key = "))
    value = int(input("enter a value for the value = "))
    dict[key] = value
print(dict)
for k in sorted(dict):
    print(k , dict[k])
"""

# Sort dictionary by values

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    key = int(input("enter a value for key = "))
    value = int(input("enter a value for value = "))
    dict[key] = value 
print(dict)
sorted_dict = sorted(dict , key=dict.get)
for i in sorted_dict:
    print( i , dict[i] )
"""

# Find key with maximum value

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    key = int(input("enter a value for key = "))
    value = int(input("enter a value for value = "))
    dict[key] = value
print(dict)
max_dict = max(dict,key=dict.get)
print(max_dict)
"""

# Invert dictionary

"""dict = {}
num = int(input("enter a range of dict = "))
for i in range(num):
    key = int(input("enter a value for key = "))
    value = int(input("enter a value for the value = "))
    dict[key] = value
print(dict)
invert_dict = {}
for key,val in dict.items():
    invert_dict[val] = key
print(invert_dict)
"""

# Group words by length

# Count characters in string

"""strin = input("enter a string = ")
str_count_ch = {}
for i in strin:
    if i in str_count_ch:
        str_count_ch[i]+=1
    else:
        str_count_ch[i] = 1
print(str_count_ch)
"""

# Create nested dictionary

# Access nested dictionary

# Combine dictionaries with same keys

# Count word frequency in sentence