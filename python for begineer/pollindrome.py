"""list = []
num = int(input("enter a range of list = "))
for i in range(num):
    list_item = int(input("enter a value for list = "))
    list.append(list_item)
print(list)
new_list = []
for i in range(len(list)-1,-1,-1):
    new_list.append(list[i])
print(new_list)
if list == new_list:
    print("polindrome")
else:
    print("not pilindrome")"""

"""n=int(input("enter a number = "))
temp = n
rev = 0
for i in range(1,n+1):
    digit = n%10
    rev = rev*10+digit
    n = n//10
if temp == rev:
    print("polindrome")
else:
    print("not")
"""

"""num = int(input("enter a value = "))
temp = num
factor = 0
for i in range(1,num+1):
    if num%i==0:
        factor = factor+1

if factor == 2 :
    print("is a prime number")
else:
    print("not a prime number") 
"""

"""

n=int(input("enter a number = "))
temp = n
rev = 0
while n > 0:
    digit = n%10
    rev = rev+digit*digit*digit
    n = n//10
if temp == rev:
    print("arm")
else:
    print("not")
"""

def polindrome(n):
    temp = n
    rev = 0
    while (n>0):
        digit = n%10
        rev = rev*10+digit
        n = n//10
    if temp == rev:
        print("polindrome")
    else:
        print("not")
polindrome(n=int(input("enter a number")))


