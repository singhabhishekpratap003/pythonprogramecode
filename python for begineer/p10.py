# find the factorial
# num = int(input("enter a value = "))
# fact = 1

# for i in range(1 , num+1):
#     fact = fact*i
    
# print(fact)

# check polindrome or not

# num = int(input("enter a value =  "))
# rev=0
# orig_num = num

# while num > 0:
#     digit= num%10
#     rev = rev*10+digit
#     num = num//10
#if orig_num == rev:
#     print("is polindrome")
# else:
#     print("not npolindrome")


# reverse the number

# num = int(input("enter a value = "))

# rev=0

# while num >0:
#     digit = num%10
#     rev = rev*10+digit
#     num = num//10
# print(rev)

# count the digit

#num = int(input("enter a value = "))

# count = 0
# while num >0:
#     num = num//10
#   count+=1
# print(count)

# count the value

# num = int(input("enter a value = "))

# sum = 0

# while num >0:
#     digit = num%10
#     sum+=digit
#     num = num//10
# print(sum)

# find the power without using pow()

# num = int(input("enter a value = "))
# base = int(input(" enter a value = "))

# total = 1

# for i in range(base):
#     total= total*num
# print(total)

# generate the random number

import random

num = random.randint(1,100)

print(num)