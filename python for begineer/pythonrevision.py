'''num = int(input("enter a number to check number is prime or not = "))

if num > 1:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("this number is not a prime number")
            break
        else:
            print("this number is a prime number")
else:
    print("not a prime number please enter a valid number")

'''

#check the alphabet is upper case are not

"""
val = input("enter a string = ")
if val.isupper():
    print("this string is upper case",val)
elif val.islower():
    print("this string is lower case",val)
else:
    print("enter a valid string",val)
"""

#check the number is in range 10-50
"""
num = int(input("enter a number = "))

if num>=10 and num<=50:
    print("this number is in range 10-50")
else:
    print("this number is not in range")
"""

# find the tringle are valid and not with given triangle

"""
num1 = int(input("enter a deegre = "))
num2 = int(input("enter a deegre = "))
num3 = int(input("enter a deegre = "))
if num1+num2+num3 == 180:
    print("valid degree")
else:
    print("not a valid degree")"""

#check the century year are not

"""num = int(input("emter a number for the check the century year are not = "))
if num%100==0:
    print("this is a century year")
else:
    print("not a century year")"""


#check in string alphabet , digit , soecial character

"""val = input("enter a string = ")

if val.isalpha():
    print("this is a alphabet")
elif val.isdigit():
    print("this is a digit")
else:
    print("this is a special chartacter")"""

#calculate the electricity bill

"""num = int(input("enter the units = "))
if num <=100:
    total=num*5
elif num<=200:
    total=100*5+(num-200)*7
else:
    total = 100*5+100*7+(num-200)*10
print(f"total payment of bill amount = RS.{total}")"""

#check the person is senior citizen
"""
num = int(input("enter a age = "))

if num >=60:
    print("this is a senior citizen")
else:
    print("not a senior citizen")"""

#determine the bmi 


height1 = int(input("enter a height = "))
weight1 = int(input("enter a weight = "))
bmi = weight1/height1**2
if bmi < 18.5:
    print("under weight")
elif bmi >18.5 and bmi <24.9:
    print("normal weight")
elif bmi >25 and bmi <29.9:
    print("over weight")
else:
    print("mehnat aur karo babu")

   