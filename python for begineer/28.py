# 1. Write a function to add two numbers

"""def sum_of_two_number():
    num = int(input("enter a number for addition = "))
    num1 = int(input("enter a number for the addition = "))
    sum = num+num1
    #return sum
    print(sum)
sum_of_two_number()
"""

# 2. Write a function to find the maximum of three numbers

"""def find_max():
    num = int(input("enter a value = "))
    num1 = int(input("enter a value = "))
    num2 = int(input("enter a value = "))
    if num > num1 and num > num2:
        return num
    elif num1 > num and num1 > num2:
        return num1
    else:
        return num2
result = find_max()
print(result)
"""

# 3. Write a function to check if a number is even or odd

"""def check_even_or_odd():
    num = int(input("enter a number for check even or odd = "))
    if num%2==0: return "this value is even"
    else: return "this value is odd"
print(check_even_or_odd())
"""

# 4. Write a function to calculate factorial using loop

"""def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
result = fact(int(input("enter a value for fact = ")))
print(result)
"""

# 5. Write a function to find the sum of elements in a list

"""def sum_list():
    list = []
    num = int(input("enter arange of list = "))
    for i in range(1,num+1):
        list_item = int(input("enter a value for the list = "))
        list.append(list_item)
    sum = 0
    for i in  list:
        sum = sum+i
    return sum
result = sum_list()
print(result)
"""

# 6. Write a function to find the average of numbers in a list

"""def sum_list():
    list = []
    num = int(input("enter arange of list = "))
    for i in range(1,num+1):
        list_item = int(input("enter a value for the list = "))
        list.append(list_item)
    sum = 0
    count = 0
    for i in range(len(list)):
        sum = sum+list[i]
        count = count+1
    average = sum/count
    return average
result = sum_list()
print(result)
"""

# 7. Write a function to check if a string is palindrome

"""def polindrome_str():
    str1 = input("enter a string = ")
    if str1 == str1[::-1]: return "polindrome" 
    else: return "not polindrome"
print(polindrome_str())
"""

# 8. Write a function to count vowels in a string

"""def polindrome_str():
    str1 = input("enter a string = ")
    count = 0
    for i in str1:
        if i in "aeiou":
            count = count + 1
    return count
print(polindrome_str())
"""

# 9. Write a function to reverse a string

"""def polindrome_str():
    str1 = input("enter a string = ")
    return str1[::-1]
print(polindrome_str())
"""

# 10. Write a function to find the largest element in a list

"""def largest():
    list = []
    num = int(input("enter a range = "))
    for i in range(1,num+1):
        list_item = int(input("enter avalue for the list = "))
        list.append(list_item)
    largest1 = 0
    for i in list:
        if i > largest1:
            largest1 = i
    return largest1
print(largest()) 
"""

# 11. Write a function to find the smallest element in a list

"""def smallest():
    list = []
    num = int(input("enter a range = "))
    for i in range(1,num+1):
        list_item = int(input("enter avalue for the list = "))
        list.append(list_item)
    smallest1 = list[0]
    for i in list:
        if i < smallest1:
            smallest1 = i
    return smallest1
print(smallest()) 
"""

# 12. Write a function to calculate simple interest

"""def simple_intrest():
    p = int(input("entrer a value for the p = "))
    r = int(input("entrer a value for the r = "))
    t = int(input("entrer a value for the t = "))
    si = p*r*t/100
    return si
print(simple_intrest())
"""

# 13. Write a function to check if a number is prime

"""def check_prime():
    num = int(input("enter a number for check prime number = "))
    for i in range(2, num):
        if num % i == 0:
            return "this is not prime number"
    return "this number is prime"
print(check_prime())
"""

# 14. Write a function to print multiplication table of a number

"""def table():
    num = int(input("enter a range of table = "))
    num1 = int(input("enter a number for print the table = "))
    for i in range(1,num+1):
        tab = num1*i
        print(f"this table of {num1} = {num1} * {i} =  ",tab)
table()
"""

# 15. Write a function to remove duplicates from a list

"""def remove_duplicates():
    list = []
    num = int(input("enter a range of list = "))
    for i in range(num):
        list_item = int(input("enter a value for the list = "))
        list.append(list_item)
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_duplicates())
"""

# 16. Write a function to count words in a string

"""def count():
    str1 = input("enter a string = ")
    counta = 0
    for i in str1:
        counta+=1
    return counta
print(count())
"""

# 17. Write a function to find common elements in two lists

"""def remove_duplicates():
    list = []
    num = int(input("enter a range of list = "))
    for i in range(num):
        list_item = int(input("enter a value for the list = "))
        list.append(list_item)
    new_list = []
    num1 = int(input("enter arange of secend list = "))
    for i in range(num1):
        list_item1 = int(input("enter a value for the secend list = "))
        new_list.append(list_item1)
    common_elements = []
    for i in list:
        if i in new_list:
            common_elements.append(i)
    return common_elements
print(remove_duplicates())
"""

# 18. Write a function to convert Celsius to Fahrenheit

"""def converter():
    num = int(input("enter a number for convert the value = "))
    fahrenheit = 9/5*num+32
    return fahrenheit
print(converter())
"""

# 19. Write a function to sort a list without using sort()

"""def sort():
    list = []
    num = int(input("enter a range of list = "))
    for i in range(num):
        list_item = int(input("enter a value for the list = "))
        list.append(list_item)
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[j],list[i] = list[i],list[j]
    return list
print(sort())
"""

# 20. Write a function to find second largest number in a list



# 21. Write a function to count digits in a number

"""def count():
    num = int(input("emter a number = "))
    counta = 0
    while num > 0:
        num = num  // 10
        counta+=1
    return counta
print(count())
"""

# 22. Write a function to check Armstrong number

"""def armstrong():
    num = int(input("enter a number = "))
    temp = num
    sum = 0
    while num > 0:
        digit = num%10
        sum = sum+digit**3
        num = num//10
    if sum == temp: return "true"
    else: return "false"
print(armstrong())
"""

# 23. Write a function to generate Fibonacci series using loop

"""def fibonic():
    num = int(input("enter a value for print the fibonic series = "))
    a = 0
    b = 1
    while num > 0:
        print(a , end=" ")
        c = a+b
        a = b
        b = c
        num-=1
fibonic()
"""

# 24. Write a function to merge two lists

"""def merge_list():
    list = []
    num = int(input("enter a range = "))
    while num > 0:
        list_item = int(input("entera value = "))
        list.append(list_item)
        num-=1
    print(list)
    list1 = []
    num1 = int(input("enter a range = "))
    while num1 > 0:
        list_item1 = int(input("entera value = "))
        list1.append(list_item1)
        num1-=1
    print(list1)
    for i in range(len(list1)):
        list.append(list1[i])
    return list
print(merge_list())
"""

# 25. Write a function to find length of string without len()

"""def find_lenght():
    str1 = input("enter a string = ")
    count = 0
    for i in range(len(str1)):
        count+=1
    return count
print(find_lenght())
"""

# 26. Write a function to check anagram strings

"""def check_anagram():
    str1 = input("enter a string 1 = ")
    str2 = input("enter a string 2 = ")
    srted = sorted(str1)
    srted1 = sorted(str2)
    if srted == srted1:
        return "string are anagram"
    else:
        return "not anagram"
print(check_anagram())
"""

# 27. Write a function to sum all even numbers in a list

"""def sum_of_even_num():
    list = []
    num = int(input("enter a range of list = "))
    for i in range(num):
        list_item = int(input("enter a value = "))
        list.append(list_item)
    sum = 0
    for i in list:
        if i%2==0:
            sum = sum+i
    return sum
print(sum_of_even_num())
"""

# 28. Write a function to find GCD of two numbers

"""def find_gcd():
    num = int(input("enter a value for find gcd = "))
    num1 = int(input("enter a value for find gcd = "))
    while num1 != 0:
        num , num1 = num1, num%num1
    return num
print(find_gcd())
"""

# 29. Write a function to print all prime numbers in a range


# 30. Write a function to create a dictionary from two lists

def create_dict():
    list = []
    num = int(input("enter a range = "))
    for i in range(num):
        list_item = int(input("enter a value of list = "))
        list.append(list_item)
    list1 = []
    num1 = int(input("enter a range = "))
    for i in range(num1):
        list_item1 = int(input("enter a value of list = "))
        list1.append(list_item1)
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = list1[i]
    return dict
print(create_dict())

print(create_dict())
print(create_dict())
    