# Create a string and print it

"""str_ = "abhishek"
print(str_)
str1 = ""
num = int(input("enter a range of string = "))
while num > 0:
    str2 = input("enter a character = ")
    str1 = str1 + str2
    num-=1
print(str1)
"""

# Find length of string

"""str1 = ""
num = int(input("enter a range of string = "))
while num > 0:
    str2 = input("enter a character = ")
    str1 = str1 + str2
    num-=1
print(str1)
count = 0
for i in str1:
    count = count + 1
print(count)
print(len(str1))
"""

# Print first and last character

"""str1 = ""
num = int(input("enter a range of string = "))
while num > 0:
    str2 = input("enter a character = ")
    str1 = str1 + str2
    num-=1
print(str1)
print(str1[0])
print(str1[-1])
"""

# Convert string to uppercase

"""str1 = ""
num = int(input("enter a range of string = "))
for i in range(num):
    ch = input("enter a character for the string = ")
    str1 = str1+ch
print(str1)
print(str1.upper())
"""

# Convert string to lowercase

"""str1 = ""
num = int(input("enter a range of string = "))
for i in range(num):
    ch = input("enter a character for the string = ")
    str1 = str1+ch
print(str1)
print(str1.lower())
"""

# Check if character exists

"""str1 = ""
num = int(input("enter a range of string = "))
for i in range(num):
    ch = input("enter a character for the string = ")
    str1 = str1+ch
print(str1)
ch1 = input("enter a character for check exists or not = ")
if ch1 in str1: print("exists")
else: print("not exists")
"""

# Concatenate two strings

"""str1 = ""
num = int(input("enter a range of string = "))
for i in range(num):
    ch = input("enter a character for the string = ")
    str1 = str1+ch
print(str1)
str2 = ""
num1 = int(input("enter a range of string = "))
for i in range(num1):
    ch1 = input("enter a character for the string = ")
    str2 = str2+ch1
print(str2)
for i in str2:
    str1 = str1 + i
print(str1)
print(str1+str2)
"""

# Repeat string multiple times

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
print(str1*3)
"""
# Print each character using loop

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
for i in str1:
    print(i)
"""

# Count vowels in string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
count = 0
for i in str1:
    if i in "aeiouAEIOU":
        count = count + 1
print(count)
"""

# Count consonants in string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
count = 0
for i in str1:
    if i not in "AEIOUaeiou":
        count+=1
print(count)
"""

# Count digits in string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
count = 0
for i in str1:
    if i >= '0' and i <= '9':
        count+=1
print(count)
"""

# Count spaces in string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
count = 0
for i in str1:
    if i == " ":
        count+=1
print(count)
"""

# Reverse string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
rev_str = ""
for i in range(len(str1)-1,-1,-1):
    rev_str = rev_str + str1[i]
print(rev_str)
"""

# Check string is palindrome

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
rev_str = ""
for i in range(len(str1)-1,-1,-1):
    rev_str = rev_str + str1[i]
print(rev_str)
if str1 == rev_str: print("string is polindrome")
else: print("string is not polindrome")
"""

# Find frequency of a character

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = input("enter a string for check the frequecy of string = ")
freq_count = 0
if str3 in str1:
    freq_count+=1
print(freq_count)
"""

# Remove spaces from string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = input("enter a string for remove from the string = ")
str4 = ""
for i in str1:
    if i != str3:
        str4 = str4 + i
print(str4)
"""

# Replace vowels with *

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = ""
for i in str1:
    if i in "aeiouAEIOU": str3 = str3+"*"
    else: str3 = str3+i 
print(str3)
"""

# Count uppercase and lowercase

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
lower = 0
upper = 0
for i in str1:
    if i.islower(): lower+=1
    else: upper+=1
print(lower)
print(upper)
"""
    

# Find longest word in sentence

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
split_str = str1.split()
longest = ""
for i in split_str:
    if len(i) > len(longest): longest = i
print(longest)
print(len(longest))
"""

# Find shortest word in sentence

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
split_str = str1.split()
smallest = split_str[0                   ]
for i in split_str:
    if len(i) < len(smallest): smallest = i
print(smallest)
print(len(smallest))
"""

# Count number of words

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
count = 0
for i in str1:
    count+=1
print(count)
print(len(str1))
"""

# Capitalize first letter of each word

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
split_str = str1.split()
capital_str = ""
for i in  split_str:
    capital_str = capital_str + i.capitalize() + " "
print(capital_str)
"""

# Remove duplicate characters

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = ""
for i in str1:
    if i not  in str3: str3 = str3 + i
print(str3)
"""

# Check two strings are anagram

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = ""
num1 = int(input("enter a range of string  = "))
for i in range(num1):
    str4 = input("enter a string = ")
    str3 = str3 + str4
print(str3)
sorted_str1 = sorted(str1)
soreted_str2 = sorted(str3)
if sorted_str1 == soreted_str2: print("string are anagram")
else: print("string are not anagram")
"""

# Find most frequent character

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
dict = {}
count = 0
for i in range(len(str1)):
    dict[i] = str1[i]
print(dict)

s = input("Enter a string = ")

freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max_char = ""
max_count = 0

for i in freq:
    if freq[i] > max_count:
        max_count = freq[i]
        max_char = i

print("Most frequent character =", max_char)
print("Count =", max_count)
"""

# Sort characters of string

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
print(sorted(str1))
"""

# Remove specific character

"""str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
str3 = ""
remove_string = input("enter a string for remove the specific character = ")
for i in str1:
    if i != remove_string:
        str3 = str3 + i
print(str3)
"""


# Reverse words in sentence

str1 = ""
num = int(input("enter a range of string  = "))
for i in range(num):
    str2 = input("enter a string = ")
    str1 = str1 + str2
print(str1)
split_str = str1.split()
revsre_str = ""
for i in range(len(split_str)-1,-1,-1):
    revsre_str = revsre_str+split_str[i]
print(revsre_str)

# Count special characters

s = input("Enter a string = ")

count = 0

for i in s:
    if not i.isalnum() and i != " ":
        count += 1

print("Special characters =", count)